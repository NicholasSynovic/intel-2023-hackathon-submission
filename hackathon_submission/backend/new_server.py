import time
from argparse import Namespace
from ast import literal_eval
from typing import Any, List

import pandas
from fastapi import FastAPI, File, UploadFile
from pandas import DataFrame, Series

from hackathon_submission.backend.inference import (cvInference, prepareData,
                                                    processData, runInference)
from hackathon_submission.backend.utils import models

app: FastAPI = FastAPI()


# Check to see if the server can send and recieve data
@app.get(path="/")
def checkOnline() -> dict:
    return {"status": True}


# Login
@app.post(path="/api/account/login")
def login(account: models.Account) -> dict:
    username: str = account.username.lower()
    password: str = account.password

    df: DataFrame = common.getTable(tableName="Users")

    accountStatus: List[bool] = common.checkAccountStatus(
        df=df,
        username=username,
        password=password,
    )

    if accountStatus == [True, True]:
        return {"username": username}
    else:
        return {"username": None}


# Logout
@app.post(path="/api/account/logout")
def logout(account: models.Account) -> dict:
    return {"username": None}


# Create Account
@app.post(path="/api/account/signup")
def signupAccount(account: models.Account) -> dict:
    username: str = account.username.lower()
    password: str = account.password

    df: DataFrame = common.getTable(tableName="Users")

    accountStatus: List[bool] = common.checkAccountStatus(
        df=df,
        username=username,
        password=password,
    )

    if accountStatus == [False, False]:
        newRow: DataFrame = DataFrame(
            data={
                "Username": [username],
                "Password": [password],
            }
        )
        newDF: DataFrame = pandas.concat(objs=[df, newRow], ignore_index=True)
        common.writeDataToTable(df=newDF, tableName="Users")

        return {"username": username}
    else:
        return {"username": None}


# Delete Account
@app.delete(path="/api/account/delete")
def deleteAccount(account: models.Account) -> dict:
    username: str = account.username.lower()
    password: str = account.password

    df: DataFrame = common.getTable(tableName="Users")

    accountStatus: List[bool] = common.checkAccountStatus(
        df=df,
        username=username,
        password=password,
    )

    if accountStatus == [True, True]:
        newDF: DataFrame = df[df["Username"] != username]
        newDF.reset_index(drop=True, inplace=True)
        common.writeDataToTable(df=newDF, tableName="Users")

    return {"username": None}


# NLP Preprocess Data
@app.post(path="/api/nlp/preprocess")
def preprocessNLP(data: models.SymptomsChecklist) -> dict:
    series: Series = Series(data.__dict__)
    processedData: str = prepareData.to_symptoms_string(row=series)
    return {"document": processedData, "image": None}


# CV Preprocess Data
@app.post(path="/api/cv/preprocess")
async def preprocessCV(data: UploadFile = File(...)) -> dict:
    imageBytes: bytes = await data.read()
    imageStr: str = imageBytes.decode()
    return {"document": None, "image": imageStr}


# NLP Infrence
@app.post(path="/api/nlp/inference")
def inferencePrognosisNLP(data: models.Inference) -> dict:
    df: DataFrame = DataFrame(data={"symptoms": [data.document]})

    FLAGS: Namespace = Namespace(
        batch_size=4,
        benchmark_mode=False,
        bf16=False,
        input_file=df,
        intel=True,
        is_inc_int8=False,
        logfile="",
        n_runs=100,
        saved_model_dir=common.NLP_MODEL_PATH,
        seq_length=64,
    )

    predictions: list = runInference.main(flags=FLAGS)

    pairs: dict[str, float] = predictions[0]["prognosis"]

    formattedPairs: dict[str, Any] = {
        "username": data.username.lower(),
        "symptoms": data.document,
        "reportTime": time.time(),
        "type_": "nlp",
        "Prognosis": [],
        "Probability": [],
        "Image": data.image,
    }

    prognosis: str
    for prognosis in pairs.keys():
        formattedPairs["Prognosis"].append(prognosis)
        formattedPairs["Probability"].append(str(pairs[prognosis] * 100) + "%")

    return formattedPairs


# CV Infrence
@app.post(path="/api/cv/inference")
def inferencePrognosisCV(data: models.Inference) -> dict:
    imageBytes: bytes = literal_eval(node_or_string=data.image)

    prediction: list = list(cvInference.main(imageBytes=imageBytes))

    if prediction == [1, 0]:
        prognosis = "Pneumonia"
    if prediction == [0, 1]:
        prognosis = "Normal"

    formattedPairs: dict[str, Any] = {
        "username": data.username.lower(),
        "symptoms": data.document,
        "reportTime": time.time(),
        "type_": "nlp",
        "Prognosis": [prognosis, "", "", "", ""],
        "Probability": ["", "", "", "", ""],
        "Image": data.image,
    }

    return formattedPairs


# Create A Report
@app.post(path="/api/report/create")
def createReport(report: models.Report) -> None:
    df: DataFrame = DataFrame(data=report.__dict__)
    reportDF: DataFrame = common.getTable(tableName="Reports")
    newDF: DataFrame = pandas.concat(objs=[reportDF, df], ignore_index=True)
    common.writeDataToTable(df=newDF, tableName="Reports")


# Delete All Reports
@app.delete(path="/api/report/delete")
def deleteAllReports(account: models.Account) -> dict:
    username: str = account.username.lower()
    password: str = account.password

    df: DataFrame = common.getTable(tableName="Users")

    accountStatus: List[bool] = common.checkAccountStatus(
        df=df,
        username=username,
        password=password,
    )

    if accountStatus == [True, True]:
        reportsDF: DataFrame = common.getTable(tableName="Reports")
        newDF: DataFrame = reportsDF[reportsDF["Username"] != username]
        newDF.reset_index(drop=True, inplace=True)
        common.writeDataToTable(df=newDF, tableName="Reports")

        return {"username": username}
    else:
        return {"username": None}


# Download All Reports
@app.post(path="/api/report/download")
def downloadAllReports(account: models.Account) -> dict:
    username: str = account.username.lower()
    password: str = account.password

    df: DataFrame = common.getTable(tableName="Users")

    accountStatus: List[bool] = common.checkAccountStatus(
        df=df,
        username=username,
        password=password,
    )

    if accountStatus == [True, True]:
        reportsDF: DataFrame = common.getTable(tableName="Reports")
        newDF: DataFrame = reportsDF[reportsDF["Username"] == username]
        newDF.reset_index(drop=True, inplace=True)
        return newDF.to_dict()

    else:
        return {"username": None}
