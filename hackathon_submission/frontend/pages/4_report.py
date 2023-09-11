from ast import literal_eval
from datetime import datetime

import numpy as np
import streamlit as st
from pandas import DataFrame, Series
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

            df["Prognosis"].replace("", np.nan, inplace=True)
            df.dropna(subset=["Prognosis"], inplace=True)

            if df.shape[0] == 1:
                prog: str = df.iloc[0][["Prognosis"]].to_list()[0]
                imgSeries: Series = df.iloc[0][["Image"]]
                imgDF: DataFrame = DataFrame.from_dict(
                    data=literal_eval(imgSeries[0]),
                    orient="index",
                )
                imgDF[0].replace("", np.nan, inplace=True)
                imgDF.dropna(ignore_index=True, inplace=True)
                imgDF.reset_index(drop=True, inplace=True)

                if prog == "Ill":
                    st.write(
                        f"\n**Overview**: :red[You are at risk for **pneumonia**. Please seek medical attention.]"
                    )
                else:
                    st.write(
                        f"\n**Overview**: :green[Good news! You most likely do not have **pneumonia**. If your sympyoms worsen, please seek medical attention.]"
                    )

                print(imgDF)

                rawImg = imgDF.iloc[0]
                imgDF.drop([0], inplace=True)
                imgDF.reset_index(drop=True, inplace=True)

                img: bytes = literal_eval(rawImg.values[0])
                st.image(image=img)

            else:
                topProgProb: list = df.iloc[0][["Prognosis", "Probability"]].to_list()

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
                    data=df[["Prognosis", "Probability"]],
                    use_container_width=True,
                    hide_index=True,
                )

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

            deleteAccountButton = st.button(label="Delete Account")
            if deleteAccountButton:
                api.deleteAccount(username=st.session_state["username"])
                common.ACCOUNT_MODAL.close()
                common.logout()

            downloadData = st.button(label="Download data")
            if downloadData:
                api.downloadReports(username=st.session_state["username"])
                st.write(f"Data saved to {st.session_state['username']}_reports.json")

            changeUsername = st.button(label="Change Username")
            if changeUsername:
                newUsername = st.text_input(label="New username")
                submitUsername = st.button(label="Submit new username")
                if submitUsername:
                    api.changeUsername(
                        username=st.session_state["username"],
                        newUsername=newUsername,
                    )
                    st.session_state["username"] = newUsername

    st.write(common.PAGE_FOOTER)
    st.divider()


if __name__ == "__main__":
    main()
