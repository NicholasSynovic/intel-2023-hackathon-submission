from pathlib import Path
from typing import Literal, Tuple

from pandas import DataFrame
from sqlalchemy import (Column, Connection, Engine, Float, ForeignKey, Integer,
                        MetaData, String, Table, create_engine, text, TextClause)


class SQL:
    def __init__(self, sqliteDBPath: Path) -> None:
        self.sqliteURI: str = f"sqlite:///{sqliteDBPath.absolute().__str__()}"

        self.usersTableName: str = "Users"

        self.metadata: MetaData = MetaData()

        self.engine: Engine = create_engine(url=self.sqliteURI)
        self.conn: Connection = self.engine.connect()

    def closeConnection(self) -> bool:
        self.conn.close()
        return self.conn.closed

    def createSchema_Users(self) -> None:
        Table(
            self.usersTableName,
            self.metadata,
            Column(
                name="ID",
                type_=Integer,
                primary_key=True,
                unique=True,
                autoincrement=True,
            ),
            Column(name="Username", type_=String, unique=True),
            Column(name="Password", type_=String),
        )

    def createTables(self) -> None:
        self.metadata.create_all(bind=self.conn)

    def writeDFToDB(
        self,
        df: DataFrame,
        tableName: Literal["Users"],
        keepIndex: bool,
        indexColumn: None = None,
    ) -> None:
        df.to_sql(
            name=tableName,
            con=self.engine,
            if_exists="replace",
            index=keepIndex,
            index_label=indexColumn,
        )
