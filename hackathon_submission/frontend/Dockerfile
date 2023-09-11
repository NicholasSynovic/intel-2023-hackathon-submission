FROM intel/oneapi-aikit

# copy project to folder
COPY . /app

# set the working directory
WORKDIR /app

# install dependancies
RUN pip3 install -r requirements.txt --user

# build and install project
RUN python3 -m poetry build
RUN python3 -m pip install dist/hackathon_submission-0.1.0.tar.gz --force-reinstall

# set PATH
ENV PATH="/root/.local/bin:${PATH}"

# exposing endpoint port
EXPOSE 8000
EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "hackathon_submission/frontend/about.py", "--server.port=8501", "--server.address=0.0.0.0"]
