from pandas import DataFrame

from hackathon_submission.backend.utils import common
from hackathon_submission.schemas.sql import SQL


def main() -> None:
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)

    df: DataFrame = DataFrame(data={"Username": ["user"], "Password": ["password"]})

    sql.createSchema_Users()
    sql.createSchema_Reports()
    sql.writeDFToDB(df=df, tableName="Users", keepIndex=False)
    sql.closeConnection()


if __name__ == "__main__":
    main()
