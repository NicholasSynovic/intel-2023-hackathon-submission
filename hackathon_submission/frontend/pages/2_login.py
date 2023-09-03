import pandas
import streamlit as st
from hackathon_submission import common
from hackathon_submission.schemas.sql import SQL
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page
from hackathon_submission.utils import api

MESSAGE: str = """## Login

Test username: `user`\n
Test password: `password`
"""

def searchForUser(username: str) -> bool:
    # MOVE TO BACKEND
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.conn)
    sql.closeConnection()

    row: DataFrame = df[df["Username"] == username]

    if row.shape[0] > 0:
        return True
    return False


def checkPassword(username: str, password: str) -> bool:
    # MOVE TO BACKEND
    sql: SQL = SQL(sqliteDBPath=common.DB_PATH)
    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.conn)
    sql.closeConnection()

    row: DataFrame = df[df["Username"] == username]

    if row.shape[0] > 1:
        return False

    try:
        if row["Password"].to_list()[0] == password:
            return True
    except ValueError:
        return False
    return False


def main() -> None:
    LOGIN_SUCCESS: bool = False

    st.set_page_config(**common.SITE_STATE)
    st.markdown(**common.HIDDEN_SIDEBAR_CSS)

    st.write(common.PAGE_HEADER)
    st.write(MESSAGE)

    if api.check():
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

        col1, col2, col3 = st.columns(spec=[5, 1, 1], gap="small")

        with col1:
            backButton: bool = st.button(label="Back")
            if backButton:
                switch_page(page_name="about")

        with col2:
            signUpButton: bool = st.button(label="Sign Up")
            if signUpButton:
                switch_page(page_name="signup")

        with col3:
            loginButton: bool = st.button(label="Login")

        if loginButton:
            # REPLACE WITH ASYNC CODE FROM BACKEND
            if searchForUser(username=username):
                if checkPassword(username=username, password=password):
                    LOGIN_SUCCESS = True
                else:
                    st.write(common.ACCOUNT_ERROR_MESSAGE.format("Password"))
            else:
                st.write(common.ACCOUNT_ERROR_MESSAGE.format("Username"))

        if LOGIN_SUCCESS:
            st.session_state["username"] = username
            switch_page(page_name="symptoms")

    else:
        st.write(common.SERVER_ERROR_MESSAGE)

    st.divider()
    st.write(common.PAGE_FOOTER)


if __name__ == "__main__":
    main()
