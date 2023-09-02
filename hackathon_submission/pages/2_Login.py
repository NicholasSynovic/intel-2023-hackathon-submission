import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from hackathon_submission.conf import pageState, hideSidebarCSS, dbPath
from pathlib import Path
from hackathon_submission.schemas.sql import SQL
import pandas
from pandas import DataFrame


HEADER: str = """# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## Login

Test username: `user`\n
Test password: `password`
"""

def searchForUser(username: str) ->  bool:
    # MOVE TO BACKEND
    sql: SQL = SQL(sqliteDBPath=dbPath)
    df: DataFrame = pandas.read_sql_table(table_name="Users", con=sql.conn)
    sql.closeConnection()
    
    row: DataFrame = df[df["Username"] == username]
    
    if row.shape[0] > 0:
        return True
    return False

def checkPassword(username: str, password: str)    ->  bool:
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

def main()  ->  None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)
    username: str = st.text_input(label="Username", max_chars=30, type="default", help="Username",)
    password: str = st.text_input(label="Password", max_chars=30, type="password", help="Password",)

    col1, _, _, _, _, col2 = st.columns(spec=[1,1,1,1,1,1], gap="large")

    with col1:
        backButton: bool = st.button(label="Back")
        if backButton:
            switch_page(page_name="About")
    
    with col2:
        loginButton: bool = st.button(label="Login")

    if loginButton:
        if searchForUser(username=username):
            st.write("Valid username")
            if checkPassword(username=username, password=password):
                st.write("Valid password")
            else:
                st.write("Invalid password")
        else:
            st.write("Invalid username")


    st.divider()

if __name__ == "__main__":
    main()

