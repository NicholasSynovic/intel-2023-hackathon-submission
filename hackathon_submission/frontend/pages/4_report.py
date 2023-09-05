from datetime import datetime
from random import randint

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission.frontend.utils import api, common

MESSAGE: str = """## {}'s Report

Below are your estimated prognoses with their probabilities.
Please know that these are only estimations by an automated system.
No medical professional has verified the legitamacy of these prognoses.
"""


def main() -> None:
    st.set_page_config(**common.SITE_STATE)
    st.markdown(**common.HIDDEN_SIDEBAR_CSS)

    common.checkSessionState()

    st.write(common.PAGE_HEADER)
    st.write(MESSAGE.format(st.session_state["username"]))
    st.divider()

    if common.checkServerConnection():
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
            aiDoctor = st.button(label="Download reports")
            if aiDoctor:
                switch_page(page_name="Talk")

        keys: list = []
        while len(keys) < len(dfs):
            key: int = randint(a=0, b=10000)
            if key not in keys:
                keys.append(key)

        df: dict
        for df in dfs:
            st.write(
                f"### Report From {datetime.utcfromtimestamp(df['time']).strftime('%A, %B %d %Y @ %I:%M %p')}",
            )
            st.write(f"**Symptoms**: {df['symptoms']}")

            topProgProb: list = df["df"].iloc[0][["Prognosis", "Probability"]].to_list()

            prob: float = float(topProgProb[1][0:3])
            if prob <= 30:
                st.write(
                    f"\n**Overview**: :green[Good news! You most likely do not have {topProgProb[0]}. If your sympyoms worsen, please seek medical attention.]"
                )
            elif (prob > 30) and (prob < 50):
                st.write(
                    f"\n**Overview**: :yellow[You are at moderate risk for {topProgProb[0]}. If your sympyoms worsen, please seek medical attention.]"
                )
            else:
                st.write(
                    f"\n**Overview**: :red[You are at risk for {topProgProb[0]}. Please seek medical attention.]"
                )

            st.dataframe(data=df["df"], use_container_width=True, hide_index=True)
            deleteReportButton = st.button(label="Delete Report", key=keys.pop())
            if deleteReportButton:
                api.deleteReport(uuid=df["time"])
                switch_page(page_name="report")

            st.divider()

    st.write(common.PAGE_FOOTER)
    st.divider()


if __name__ == "__main__":
    main()
