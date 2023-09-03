import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission.conf import hideSidebarCSS, pageState
from pandas import DataFrame

HEADER: str = """# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## About

Empire General Hospital is commited to providing patients with state-of-the-art
resources to assist in the diagnosis of medical symptoms.
We utilize deep learning models to provide patients with fast access to 
prognosis predictions. 
While we do provide this technology free of charge, we remind patients that this
technology does not replace practicioners and that the predicted prognosis might
be incorrect.
Furthermore, this technology is still in development and is subject to buggy
behavior.

To speak to a doctor at Empire General Hospital, call: `(xxx) xxx-xxxx`\n

For medical emergencies, call `911`

"""


def main() -> None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "report" not in st.session_state:
        st.session_state["report"] = DataFrame()

    st.write(HEADER)

    nextPage: bool = st.button(label="Login")
    if nextPage:
        switch_page(page_name="Login")

    st.divider()


if __name__ == "__main__":
    main()
