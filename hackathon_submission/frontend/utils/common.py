import streamlit as st
from requests.exceptions import ConnectionError
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission.frontend.utils import api

SITE_STATE = {
    "page_title": "DiagnoEase",
    "initial_sidebar_state": "collapsed",
}

HIDDEN_SIDEBAR_CSS = {
    "body": """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    "unsafe_allow_html": True,
}

PAGE_HEADER: str = """# Empire General Hospital DiagnoEase
> A prototype developed by Nicholas M. Synovic ([nsynovic@luc.edu](mailto:nsynovic@luc.edu))"""

PAGE_FOOTER: str = """To speak to a medical professional at Empire General Hospital, call `(xxx) xxx-xxxx`\n
For all medical emergencies, call `911`"""

ACCOUNT_ERROR_MESSAGE: str = ":red[Invalid {}]"

SERVER_ERROR_MESSAGE: str = f":red[Unable to reach server at: {api.URL}]"


def logout() -> None:
    api.logout()
    st.session_state["username"] = ""
    st.session_state["symptoms"] = ""
    switch_page(page_name="about")


def checkServerConnection() -> bool:
    try:
        api.check()
    except ConnectionError:
        st.write(SERVER_ERROR_MESSAGE)
        return False
    return True
