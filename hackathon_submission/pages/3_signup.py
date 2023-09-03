from pathlib import Path

import pandas
import streamlit as st
from hackathon_submission import common
from hackathon_submission.schemas.sql import SQL
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page

MESSAGE: str = "## Sign Up"

LOGIN_ERROR: str = ":red[Invalid {}]"

def searchForUser(username: str) -> bool:
    # MOVE TO BACKEND
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.conn)
    sql.closeConnection()

    row: DataFrame = df[df["Username"] == username]

    if row.shape[0] > 0:
        return True
    return False


def createAccount(username: str, password: str) -> bool:
    # MOVE TO BACKEND
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.conn)

    df.set_index("index", inplace=True)
    df = df.append(
        other={"Username": username, "Password": password},
        ignore_index=True,
    )

    sql.writeDFToDB(df=df, tableName="Users", keepIndex=True)
    sql.closeConnection()


def main() -> None:
    LOGIN_SUCCESS: bool = False

    st.set_page_config(**common.SITE_STATE)
    st.markdown(**common.HIDDEN_SIDEBAR_CSS)

    st.write(common.PAGE_HEADER)
    st.write(MESSAGE)

    username: str = st.text_input(
        label="Username",
        max_chars=30,
        type="default",
        help="Username",
    )
    password: str = st.text_input(
        label="Password",
        max_chars=30,
        type="password",
        help="Password",
    )

    col1, col2 = st.columns(spec=[5, 1], gap="small")

    with col1:
        backButton: bool = st.button(label="Back")
        if backButton:
            switch_page(page_name="Login")

    with col2:
        createAccountButton: bool = st.button(label="Create Account")

    if createAccountButton:
        # REPLACE WITH ASYNC CODE FROM BACKEND
        if searchForUser(username=username):
            st.write(LOGIN_ERROR.format("Username"))
        else:
            LOGIN_SUCCESS = True

    if LOGIN_SUCCESS:
        createAccount(username=username, password=password)
        st.session_state["username"] = username
        switch_page(page_name="symptoms")

    st.write(common.PAGE_FOOTER)
    st.divider()


if __name__ == "__main__":
    main()
