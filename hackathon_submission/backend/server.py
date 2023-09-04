from typing import Any, Literal

import pandas
from fastapi import FastAPI
from hackathon_submission import common
from hackathon_submission.schemas.sql import SQL
from pandas import DataFrame

app: FastAPI = FastAPI()


def getUsersTable() -> DataFrame:
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.conn)
    sql.closeConnection()
    return df


def usernameExists(username: str, df: DataFrame) -> bool:
    return username in df["Username"].values


def checkPassword(username: str, password: str, df: DataFrame) -> bool:
    row: Any = df[df["Username"] == username]

    if row["Password"].to_list()[0] == password:
        return True
    return False


@app.get(path="/")
def check() -> Literal[True]:
    return True


@app.post(path="/api/account/login")
def login(username: str, password: str) -> bool:
    username = username.lower()
    df: DataFrame = getUsersTable()

    userExists: bool = usernameExists(username=username, df=df)
    if userExists:
        return checkPassword(username=username, password=password, df=df)
    return False


@app.post(path="/api/account/logout")
def logout() -> Literal[True]:
    return True


@app.post(path="/api/account/signup")
def signup(username: str, password: str) -> dict:
    username = username.lower()
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df: DataFrame = getUsersTable()

    userExists: bool = usernameExists(username=username, df=df)
    if userExists:
        return {"username": False}

    df.set_index("index", inplace=True)
    df = df.append(
        other={"Username": username, "Password": password},
        ignore_index=True,
    )

    sql.writeDFToDB(df=df, tableName="Users", keepIndex=True)
    sql.closeConnection()

    return {"username": username}


@app.post(path="/api/inference/prognosis")
def inferencePrognosis() -> bool:
    pass


@app.get(path="/api/storage/symptoms")
def getSymptoms() -> bool:
    pass


@app.get(path="/api/storage/prognosis")
def getPrognosis() -> bool:
    pass


@app.post(path="/api/generate/report")
def generateReport() -> bool:
    pass
