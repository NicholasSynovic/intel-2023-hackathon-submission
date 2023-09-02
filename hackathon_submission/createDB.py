from pathlib import Path

from pandas import DataFrame

from hackathon_submission.schemas.sql import SQL


def main() -> None:
    dbPath: Path = Path("storage/data.db")
    sql: SQL = SQL(sqliteDBPath=dbPath)

    df: DataFrame = DataFrame(data={"Username": ["user"], "Password": ["password"]})

    sql.createSchema_Users()
    sql.writeDFToDB(df=df, tableName="Users", keepIndex=True)
    sql.closeConnection()


if __name__ == "__main__":
    main()
