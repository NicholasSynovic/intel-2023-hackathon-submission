from typing import List

import pandas
from fastapi import FastAPI
from pandas import DataFrame

from hackathon_submission.backend.utils import common, models

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

# CV Preprocess Data

# NLP Infrence

# CV Infrence

# Create A Report


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
