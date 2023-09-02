import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from hackathon_submission.conf import pageState, hideSidebarCSS
from pathlib import Path
from hackathon_submission.schemas.sql import SQL
from sqlalchemy import Connection, text, TextClause
import pandas
from pandas import DataFrame


HEADER: str = """# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## Login

Test username: `user`\n
Test password: `password`
"""

def searchForUser(username: str, password: str) ->  bool:
    dbPath: Path = Path("../data.db")

    print(dbPath.is_file())

    sql: SQL = SQL(sqliteDBPath=dbPath)

    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.engine)
    print(df)

def main()  ->  None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)
    name: str = st.text_input(label="Username", max_chars=30, type="default", help="Username",)
    password: str = st.text_input(label="Password", max_chars=30, type="password", help="Password",)

    col1, _, _, _, _, col2 = st.columns(spec=[1,1,1,1,1,1], gap="large")

    with col1:
        backButton: bool = st.button(label="Back")
        if backButton:
            switch_page(page_name="About")
    
    with col2:
        loginButton: bool = st.button(label="Login")

        if loginButton:
            searchForUser(username="user", password="password")

    st.divider()

if __name__ == "__main__":
    main()

