import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_modal import Modal

from hackathon_submission.frontend.utils import new_api

URL: str = "http://localhost:8000"
# URL: str = "http://172.22.0.3:8000"

HEADERS: dict = {"Content-type": "application/json"}


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

SERVER_ERROR_MESSAGE: str = f":red[Unable to reach server at: {URL}]"

ACCOUNT_MODAL: Modal = Modal(title="Account Settings", key="modal")


def logout(username: str, password: str) -> None:
    new_api.logout(username=username, password=password)
    st.session_state["username"] = ""
    st.session_state["symptoms"] = ""
    switch_page(page_name="about")


def checkServerConnection() -> bool:
    try:
        new_api.checkOnline
    except ConnectionError:
        st.write(SERVER_ERROR_MESSAGE)
        return False
    return True


def checkSessionState() -> None:
    try:
        st.session_state["username"]
    except KeyError:
        switch_page(page_name="about")
