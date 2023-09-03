import streamlit as st
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission import common

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
    st.write(common.PAGE_FOOTER)

    nextPage: bool = st.button(label="Login")
    if nextPage:
        switch_page(page_name="login")

    st.divider()


if __name__ == "__main__":
    main()
