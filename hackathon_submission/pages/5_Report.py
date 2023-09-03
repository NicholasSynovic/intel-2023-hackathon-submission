import streamlit as st
from streamlit_extras.switch_page_button import switch_page

from hackathon_submission.conf import hideSidebarCSS, pageState

HEADER: str = """# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## Report

Below are your *estimated* prognoses with their probabilities.
Please know that these are only estimations by an automated system.
No medical professional has verified the legitamacy of these prognoses.

To talk to a professional at Empire General Hospital, call `(xxx) xxx-xxxx`
For medical emergencies, call `911`
"""


def main() -> None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)

    st.divider()


if __name__ == "__main__":
    main()
