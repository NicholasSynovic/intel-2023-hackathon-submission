import streamlit as st
from hackathon_submission.utils import api
from streamlit_extras.switch_page_button import switch_page
from hackathon_submission import common
from pandas import DataFrame

MESSAGE: str = f"""## {st.session_state["username"]}'s Report

Below are your estimated prognoses with their probabilities.
Please know that these are only estimations by an automated system.
No medical professional has verified the legitamacy of these prognoses.
"""


def main() -> None:
    st.set_page_config(**common.SITE_STATE)
    st.markdown(**common.HIDDEN_SIDEBAR_CSS)

    st.write(common.PAGE_HEADER)
    st.write(MESSAGE)

    st.dataframe(
        data=st.session_state["report"],
        use_container_width=True,
        hide_index=True,
    )

    col1, col2, col3 = st.columns(spec=[1, 1, 1], gap="small")

    with col1:
        logoutButton = st.button(label="Logout")
        if logoutButton:
            api.logout()
            st.session_state["username"] = ""
            st.session_state["report"] = DataFrame()
            switch_page(page_name="about")

    with col2:
        reportSymptomsButton = st.button(label="Return to Symptoms Page")
        if reportSymptomsButton:
            switch_page(page_name="symptoms")

    with col3:
        aiDoctor = st.button(label="Talk to an AI Doctor")
        if aiDoctor:
            switch_page(page_name="Talk")

    st.write(common.PAGE_FOOTER)
    st.divider()


if __name__ == "__main__":
    main()
