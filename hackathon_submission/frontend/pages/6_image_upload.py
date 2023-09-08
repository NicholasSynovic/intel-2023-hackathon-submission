from os import listdir

import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission.frontend.utils import api, common

MESSAGE: str = """## {}'s X-Ray Image Upload

Please upload an X-Ray image and then press "Upload Image".\n

To view previous reports, press "View Reports".\n

If you have an image to submit for analysis, press "Upload Image".
"""


def main() -> None:
    st.set_page_config(**common.SITE_STATE)
    st.markdown(**common.HIDDEN_SIDEBAR_CSS)

    common.checkSessionState()

    st.write(common.PAGE_HEADER)
    st.write(MESSAGE.format(st.session_state["username"]))

    image = st.selectbox(
        label="Example Image File",
        options=listdir("pages/images"),
    )

    if common.checkServerConnection():
        topCol1, topCol2, topCol3 = st.columns(spec=[1, 1, 1], gap="large")

        with topCol1:
            accountSettingsButton = st.button(label="Account Settings")
            if accountSettingsButton:
                common.ACCOUNT_MODAL.open()
        with topCol2:
            viewReportsButton = st.button(label="View Reports")
            if viewReportsButton:
                switch_page(page_name="report")
        with topCol3:
            submitImageButton = st.button(label="Upload Image")
            if submitImageButton:
                st.write(image)  # Change this to API calls)

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

    st.write(common.PAGE_FOOTER)
    st.divider()


if __name__ == "__main__":
    main()
