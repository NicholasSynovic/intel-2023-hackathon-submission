from pathlib import Path

import pandas
import streamlit as st
from hackathon_submission.conf import dbPath, hideSidebarCSS, pageState
from hackathon_submission.schemas.sql import SQL
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page

HEADER: str = f"""# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## {st.session_state["username"]}'s Portal
"""


def main() -> None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)

    col1, _, col2, col3 = st.columns(spec=[1, 1, 1, 1], gap="small")

    with col1:
        logoutButton = st.button(label="Logout")
        if logoutButton:
            st.session_state["username"] = None
            switch_page(page_name="Login")

    with col2:
        newSymptomsButton = st.button(label="New Symptoms")
        if newSymptomsButton:
            switch_page(page_name="Symptoms")
    with col3:
        talkToDoctorButton = st.button(label="Talk to an AI Doctor")

    st.divider()


if __name__ == "__main__":
    main()
