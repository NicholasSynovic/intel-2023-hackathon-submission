FROM intel/oneapi-aikit

# copy project to folder
COPY . /app

# set the working directory
WORKDIR /app

# install dependancies
RUN pip3 install torch torchvision torchaudio --user --index-url https://download.pytorch.org/whl/cu118
RUN pip3 install -r requirements.txt --user

# build and install project
RUN python3 -m poetry build
RUN python3 -m pip install dist/hackathon_submission-0.1.0.tar.gz --force-reinstall

RUN wget --directory-prefix /app/hackathon_submission/backend/cvModel https://huggingface.co/NicholasSynovic/intel-2023-student-ambassador-hackathon-cv/resolve/main/updated_model.pb

# set PATH
ENV PATH="/root/.local/bin:${PATH}"

# exposing endpoint port
EXPOSE 8000

WORKDIR /app/hackathon_submission/backend

# create DB
RUN python3 createDB.py

ENTRYPOINT ["uvicorn", "server:app", "--port=8000", "--host=0.0.0.0", "--proxy-headers"]
