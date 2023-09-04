from datetime import datetime

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission.frontend.utils import api, common

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
    st.divider()

    dfs: list = api.getReports(username=st.session_state["username"])

    col1, col2, col3 = st.columns(spec=[1, 1, 1], gap="small")

    with col1:
        logoutButton = st.button(label="Logout")
        if logoutButton:
            common.logout()

    with col2:
        reportSymptomsButton = st.button(label="Report Symptoms")
        if reportSymptomsButton:
            switch_page(page_name="symptoms")

    with col3:
        aiDoctor = st.button(label="Talk to an AI Doctor")
        if aiDoctor:
            switch_page(page_name="Talk")

    df: dict
    for df in dfs:
        st.write(
            f"### Report From {datetime.utcfromtimestamp(df['time']).strftime('%Y-%m-%d %H:%M:%S')}"
        )
        st.write(f"**Symptoms**: {df['symptoms']}")
        st.dataframe(data=df["df"], use_container_width=True, hide_index=True)
        st.divider()

    st.write(common.PAGE_FOOTER)
    st.divider()


if __name__ == "__main__":
    main()
