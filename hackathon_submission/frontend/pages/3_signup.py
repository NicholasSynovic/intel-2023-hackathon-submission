import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission.frontend.utils import api, common

MESSAGE: str = "## Sign Up"


def main() -> None:
    st.set_page_config(**common.SITE_STATE)
    st.markdown(**common.HIDDEN_SIDEBAR_CSS)

    st.write(common.PAGE_HEADER)
    st.write(MESSAGE)

    if common.checkServerConnection():
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

        col1, col2 = st.columns(spec=[4, 1], gap="small")

        with col1:
            backButton: bool = st.button(label="Back")
            if backButton:
                switch_page(page_name="Login")

        with col2:
            createAccountButton: bool = st.button(label="Create Account")

        if createAccountButton:
            signup: bool = api.signup(username=username, password=password)
            if signup:
                st.session_state["username"] = signup
                switch_page(page_name="report")
            else:
                st.write(common.ACCOUNT_ERROR_MESSAGE.format("Account Credentials"))

    st.divider()
    st.write(common.PAGE_FOOTER)


if __name__ == "__main__":
    main()
