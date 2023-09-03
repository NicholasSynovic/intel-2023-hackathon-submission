from fastapi import FastAPI

app: FastAPI = FastAPI()

@app.get(path="/")
def check() ->  dict:
    return {"status": True}

@app.post(path="/api/account/login")
def login() ->  bool:
    pass

@app.post(path="/api/account/logout")
def logout()    ->  bool:
    pass

@app.post(path="/api/account/signup")
def signup()    ->  bool:
    pass

@app.post(path="/api/inference/prognosis")
def inferencePrognosis()    ->  bool:
    pass

@app.get(path="/api/storage/symptoms")
def getSymptoms()   ->  bool:
    pass

@app.get(path="/api/storage/prognosis")
def getPrognosis()  ->  bool:
    pass

@app.post(path="/api/generate/report")
def generateReport()    ->  bool:
    pass


