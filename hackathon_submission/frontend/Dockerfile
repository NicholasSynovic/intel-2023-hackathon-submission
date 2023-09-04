FROM python:3.8

COPY . /frontend

# set the working directory
WORKDIR /frontend

# install dependancies
RUN pip3 install --user --no-cache-dir -r requirements.txt

# set PATH
ENV PATH="/root/.local/bin:${PATH}"

# exposing endpoint port
EXPOSE 5005

ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port", "5005", "--server.address", "0.0.0.0"]
