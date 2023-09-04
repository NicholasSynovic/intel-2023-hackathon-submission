FROM python:3.8

COPY . /frontend

# set the working directory
WORKDIR /frontend

# install dependancies
RUN pipe install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 --user --no-cache-dir
RUN pip3 install --user --no-cache-dir -r requirements.txt

# setup DB
RUN python3.8 createDB.py

# set PATH
ENV PATH="/root/.local/bin:${PATH}"

# exposing endpoint port
EXPOSE 8000

ENTRYPOINT ["uvicorn","server:app", "--reload"]
