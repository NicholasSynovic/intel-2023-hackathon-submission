FROM python:3.8

# install git
RUN apt update && apt install git -y

# clone project
RUN git clone https://github.com/NicholasSynovic/intel-2023-hackathon-submission /app

# set the working directory
WORKDIR /app

# install dependancies
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 --user --no-cache-dir
RUN pip3 install -r requirements.txt --user --no-cache-dir

# build and install project
RUN python3.8 -m poetry build
RUN python3.8 -m pip install dist/hackathon_submission-0.1.0.tar.gz --force-reinstall

# set PATH
ENV PATH="/root/.local/bin:${PATH}"

# exposing endpoint port
EXPOSE 8000

WORKDIR /app/hackathon_submission/backend

# create DB
RUN python3.8 createDB.py

ENTRYPOINT ["uvicorn", "server:app", "--port=8000", "--host=0.0.0.0"]
