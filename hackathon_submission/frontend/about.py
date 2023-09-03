import streamlit as st
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission import common
from hackathon_submission.utils import api

MESSAGE: str = """## About

Empire General Hospital is commited to providing patients with state-of-the-art
resources to assist in the diagnosis of medical symptoms.
We utilize deep learning models to provide patients with fast access to 
prognosis predictions. 
While we do provide this technology free of charge, we remind patients that this
technology does not replace practicioners and that the predicted prognosis might
be incorrect.
Furthermore, this technology is still in development and is subject to buggy
behavior.
"""


def main() -> None:
    st.set_page_config(**common.SITE_STATE)
    st.markdown(**common.HIDDEN_SIDEBAR_CSS)

    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "report" not in st.session_state:
        st.session_state["report"] = DataFrame()

    st.write(common.PAGE_HEADER)
    st.write(MESSAGE)


    if api.check():
        nextPage: bool = st.button(label="Login")
        if nextPage:
            switch_page(page_name="login")
    else:
        st.write(common.SERVER_ERROR_MESSAGE)

    st.divider()
    st.write(common.PAGE_FOOTER)


if __name__ == "__main__":
    main()
