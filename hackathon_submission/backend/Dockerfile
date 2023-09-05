FROM python:3.8

# install git
RUN apt update && apt install git -y

# clone project
RUN git clone https://github.com/NicholasSynovic/intel-2023-hackathon-submission /app

# set the working directory
WORKDIR /app

# install dependancies
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip3 install -r requirements.txt

# build and install project
RUN python3.8 -m poetry build
RUN pip3 install dist/*.tar.gz

# set PATH
ENV PATH="/root/.local/bin:${PATH}"

# exposing endpoint port
EXPOSE 8000

ENTRYPOINT ["uvicorn", "hackathon_submission/backend/server:app"]
