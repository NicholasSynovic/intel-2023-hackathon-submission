from pathlib import Path
from typing import Any, List, Literal

import pandas
from pandas import DataFrame

from hackathon_submission.schemas.sql import SQL

DB_PATH: Path = Path("storage/data.db")

CV_MODEL_PATH: str = "NicholasSynovic/intel-2023-student-ambassador-hackathon-cv"

NLP_MODEL_PATH: str = "NicholasSynovic/intel-2023-student-ambassador-hackathon-nlp"


def getTable(tableName: Literal["Users", "Reports"]) -> DataFrame:
    sql: SQL = SQL(sqliteDBPath=DB_PATH)

    df: DataFrame
    try:
        df = pandas.read_sql_table(table_name=tableName, con=sql.conn)
    except ValueError:
        df = DataFrame()
    except KeyError:
        df = DataFrame()

    sql.closeConnection()
    return df


def checkAccountStatus(df: DataFrame, username: str, password: str) -> List[bool]:
    data: List[bool] = [False, False]

    if username in df["Username"].values:
        data[0] = True
    else:
        return data

    userRow: Any = df[df["Username"] == username]
    if password in userRow["Password"].values:
        data[1] = True

    return data


def writeDataToTable(
    df: DataFrame,
    tableName=Literal["Users", "Reports"],
) -> None:
    sql: SQL = SQL(sqliteDBPath=DB_PATH)
    sql.writeDFToDB(df=df, tableName=tableName, keepIndex=False)
    sql.closeConnection()
