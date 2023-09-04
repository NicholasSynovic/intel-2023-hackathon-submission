import streamlit as st
from hackathon_submission.frontend.utils import api, common
from streamlit_extras.switch_page_button import switch_page

MESSAGE: str = """## Login

Test username: `user`\n
Test password: `password`
"""


def main() -> None:
    st.set_page_config(**common.SITE_STATE)
    st.markdown(**common.HIDDEN_SIDEBAR_CSS)

    st.write(common.PAGE_HEADER)
    st.write(MESSAGE)

    if api.check():
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

        col1, col2, col3 = st.columns(spec=[5, 1, 1], gap="small")

        with col1:
            backButton: bool = st.button(label="Back")
            if backButton:
                switch_page(page_name="about")

        with col2:
            signUpButton: bool = st.button(label="Sign Up")
            if signUpButton:
                switch_page(page_name="signup")

        with col3:
            loginButton: bool = st.button(label="Login")

        if loginButton:
            if api.login(username=username, password=password):
                st.session_state["username"] = username
                switch_page(page_name="symptoms")
            else:
                st.write(common.ACCOUNT_ERROR_MESSAGE.format("Account Credentials"))

    else:
        st.write(common.SERVER_ERROR_MESSAGE)

    st.divider()
    st.write(common.PAGE_FOOTER)


if __name__ == "__main__":
    main()
