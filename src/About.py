import streamlit as st
from streamlit_extras.switch_page_button import switch_page

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

## For Intel Hackathon Judges

I was unable to permently hide the sidebar for this submission. You are free to
navigate pages with it, however, I am unsure how the application state will 
change as you do so.
"""

def main()  ->  None:
    st.set_page_config(page_title="About", initial_sidebar_state="collapsed")
    st.write(HEADER)
    st.divider()

    nextPage: bool = st.button(label="Login")
    if nextPage:
        switch_page(page_name="Login")

if __name__ == "__main__":
    main()

