import pandas
import streamlit as st
from hackathon_submission.conf import dbPath, hideSidebarCSS, pageState
from hackathon_submission.schemas.sql import SQL
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page

HEADER: str = """# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## Login

Test username: `user`\n
Test password: `password`
"""


LOGIN_ERROR: str = ":red[Invalid {}]"


def searchForUser(username: str) -> bool:
    # MOVE TO BACKEND
    sql: SQL = SQL(sqliteDBPath=dbPath)
    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.conn)
    sql.closeConnection()

    row: DataFrame = df[df["Username"] == username]

    if row.shape[0] > 0:
        return True
    return False


def checkPassword(username: str, password: str) -> bool:
    # MOVE TO BACKEND
    sql: SQL = SQL(sqliteDBPath=dbPath)
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
   
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)
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

    col1, _, _, _, col2, col3 = st.columns(spec=[1, 1, 1, 1, 1, 1], gap="small")

    with col1:
        backButton: bool = st.button(label="Back")
        if backButton:
            switch_page(page_name="About")
    
    with col2:
        signUpButton: bool = st.button(label="Sign Up")
        if signUpButton:
            switch_page(page_name="SignUp")

    with col3:
        loginButton: bool = st.button(label="Login")

    if loginButton:
        # REPLACE WITH ASYNC CODE FROM BACKEND
        if searchForUser(username=username):
            if checkPassword(username=username, password=password):
                LOGIN_SUCCESS = True
            else:
                st.write(LOGIN_ERROR.format("Password"))
        else:
            st.write(LOGIN_ERROR.format("Username"))

    if LOGIN_SUCCESS:
        st.session_state["username"] = username
        switch_page(page_name="Portal")

    st.divider()


if __name__ == "__main__":
    main()
