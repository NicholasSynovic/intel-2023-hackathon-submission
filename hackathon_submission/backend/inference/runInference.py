# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2022 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause

# pylint: disable=C0415,E0401,R0914

# Code originally from https://github.com/oneapi-src/disease-prediction/blob/main/src/run_inference.py

"""
Run inference benchmarks
"""

import argparse
import logging
import os
import pathlib
import time
from argparse import Namespace
from contextlib import nullcontext

import numpy as np
import torch
from hackathon_submission.backend.inference.processData import (REVERSE_MAPPING,
                                                    read_and_preprocess_data)
from transformers import (AutoModelForSequenceClassification, AutoTokenizer,
                          BertConfig, BertForSequenceClassification)


def inference(predict_fn, batch, flags) -> float:
    """Run inference using the provided `predict_fn`

    Args:
        predict_fn: prediction function to use
        batch: data batch from a data loader
        n_runs: number of benchmark runs to time

    Returns:
        float : Average prediction time
    """
    n_runs = flags.n_runs
    enable_bf16 = flags.bf16
    times = []
    predictions = []
    with torch.no_grad():
        # use mixed precision bf16 inference only if enabled
        with torch.cpu.amp.autocast() if enable_bf16 else nullcontext():
            for _ in range(2 + n_runs):
                start = time.time()
                res = predict_fn(batch)
                end = time.time()
                predictions.append(res)
                times.append(end - start)

    avg_time = np.mean(times[2:])
    return avg_time


def main(flags) -> list:
    """Setup model for inference and perform benchmarking

    Args:
        FLAGS: benchmarking flags
    """

    if flags.logfile == "":
        logging.basicConfig(level=logging.DEBUG)
    else:
        path = pathlib.Path(flags.logfile)
        path.parent.mkdir(parents=True, exist_ok=True)
        logging.basicConfig(filename=flags.logfile, level=logging.DEBUG)
    logger = logging.getLogger()

    if not os.path.exists(flags.saved_model_dir):
        logger.error("Saved model %s not found!", flags.saved_model_dir)
        return

    # Load dataset into memory
    tokenizer = AutoTokenizer.from_pretrained(flags.saved_model_dir)

    test_dataset = read_and_preprocess_data(
        flags.input_file,
        tokenizer,
        max_length=flags.seq_length,
        include_label=False,
    )
    test_loader = torch.utils.data.DataLoader(
        test_dataset, batch_size=flags.batch_size, shuffle=False
    )

    # Load model into memory, if INC, need special loading
    if flags.is_inc_int8:
        from neural_compressor.utils.pytorch import load

        config = BertConfig.from_json_file(
            os.path.join(flags.saved_model_dir, "config.json")
        )
        model = BertForSequenceClassification(config=config)
        model = load(flags.saved_model_dir, model)

        # re-establish logger because it breaks from above
        logging.getLogger().handlers.clear()

        if flags.logfile == "":
            logging.basicConfig(level=logging.DEBUG)
        else:
            logging.basicConfig(filename=flags.logfile, level=logging.DEBUG)
        logger = logging.getLogger()

    else:
        model = AutoModelForSequenceClassification.from_pretrained(
            flags.saved_model_dir
        )

    # JIT model for faster execution
    batch = next(iter(test_loader))
    token_ids = batch["input_ids"]
    mask = batch["attention_mask"]

    jit_inputs = (token_ids, mask)

    if flags.intel:
        # if using intel, optimize the model
        import intel_extension_for_pytorch as ipex

        logger.info("Using IPEX to optimize model")

        model.eval()

        # select dtype based on the flag
        if flags.bf16:
            dtype = torch.bfloat16
        else:
            dtype = None  # default dtype for ipex.optimize()

        with torch.no_grad(), torch.cpu.amp.autocast() if flags.bf16 else nullcontext():
            model = ipex.optimize(model, dtype=dtype)
            model = torch.jit.trace(model, jit_inputs, check_trace=False, strict=False)
            model = torch.jit.freeze(model)

    else:
        if flags.is_inc_int8:
            logger.info("Using INC Quantized model")
        else:
            logger.info("Using stock model")

        model.eval()
        model = torch.jit.trace(model, jit_inputs, check_trace=False, strict=False)
        model = torch.jit.freeze(model)

    def predict(batch) -> torch.Tensor:
        """Predicts the output for the given batch
            using the given PyTorch model.

        Args:
            batch (torch.Tensor): data batch from data loader
                transformers tokenizer

        Returns:
            torch.Tensor: predicted quantities
        """
        res = model(
            input_ids=batch["input_ids"], attention_mask=batch["attention_mask"]
        )
        return res

    if flags.benchmark_mode:
        logger.info(
            "Running experiment n = %d, b = %d, l = %d",
            flags.n_runs,
            flags.batch_size,
            flags.seq_length,
        )

        average_time = inference(predict, batch, FLAGS)
        logger.info("Avg time per batch : %.3f s", average_time)
    else:
        predictions = []
        index = 0
        for _, batch in enumerate(test_loader):
            pred_probs = (
                torch.softmax(predict(batch)["logits"], axis=1).detach().numpy()
            )
            for i in range(len(pred_probs)):
                probs = {
                    REVERSE_MAPPING[x]: pred_probs[i, x]
                    for x in np.argsort(pred_probs[i, :])[::-1][:5]
                }
                predictions.append({"id": index, "prognosis": probs})
                index += 1
        return predictions
