from ast import literal_eval
from datetime import datetime

import streamlit as st
from pandas import DataFrame
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
        jsonResp: list = api.getReports(username=st.session_state["username"])

        col1, col2 = st.columns(spec=[3, 1], gap="small")

        with col1:
            accountSettingsButton = st.button(label="Account Settings")
            if accountSettingsButton:
                common.ACCOUNT_MODAL.open()

        with col2:
            reportSymptomsButton = st.button(label="Report Symptoms")
            if reportSymptomsButton:
                switch_page(page_name="symptoms")

        dataDict: dict
        for dataDict in jsonResp:
            time: float = dataDict["time"]
            symptoms: str = dataDict["symptoms"]
            df: DataFrame = DataFrame(data=dataDict["df"])
            prognosis: str = df["Prognosis"].iloc[0]

            st.write(
                f"### Report From {datetime.utcfromtimestamp(time).strftime('%A, %B %d %Y @ %I:%M %p')}",
            )
            st.write(f"**Symptoms**: {symptoms}")

            if (prognosis == "Ill") or (prognosis == "Normal"):
                print(df)
                print("test")

            continue

            topProgProb: list = df["df"].iloc[0][["Prognosis", "Probability"]].to_list()

            try:
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

                st.dataframe(
                    data=df["df"][["Prognosis", "Probability"]],
                    use_container_width=True,
                    hide_index=True,
                )

            except ValueError:
                prog: str = df["df"].iloc[0][["Prognosis"]].to_list()[0]
                img_str: str = df["df"].iloc[0][["Image"]][0]

                data = literal_eval(img_str)

                if prog == "Ill":
                    st.write(
                        f"\n**Overview**: :red[You are at risk for **pneumonia**. Please seek medical attention.]"
                    )
                else:
                    st.write(
                        f"\n**Overview**: :green[Good news! You most likely do not have **pneumonia**. If your sympyoms worsen, please seek medical attention.]"
                    )

                st.image(image=data[1])
            st.divider()

    if common.ACCOUNT_MODAL.is_open():
        with common.ACCOUNT_MODAL.container():
            logoutButton = st.button(label="Logout")
            if logoutButton:
                common.ACCOUNT_MODAL.close()
                common.logout()

            deleteReportsButton = st.button(label="Delete Reports")
            if deleteReportsButton:
                api.deleteReport(uuid=st.session_state["username"])
                common.ACCOUNT_MODAL.close()
                st.experimental_rerun()
            deleteReportsButton = st.button(label="Delete Reports")

            deleteAccountButton = st.button(lable="Delete Account")
            if deleteAccountButton:
                api.deleteAccount(username=st.session_state["username"])
                common.ACCOUNT_MODAL.close()
                common.logout()

    st.write(common.PAGE_FOOTER)
    st.divider()


if __name__ == "__main__":
    main()
