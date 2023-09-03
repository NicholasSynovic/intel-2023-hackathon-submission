import streamlit as st
from hackathon_submission.conf import hideSidebarCSS, pageState
from streamlit_extras.switch_page_button import switch_page

HEADER: str = f"""# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## {st.session_state["username"]}'s Report

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

    st.dataframe(
        data=st.session_state["report"],
        use_container_width=True,
        hide_index=True,
    )

    col1, col2 = st.columns(spec=[6, 2], gap="large")

    with col1:
        reportSymptomsButton = st.button(label="Report Symptoms")
        if reportSymptomsButton:
            switch_page(page_name="symptoms")

    with col2:
        aiDoctor = st.button(label="Talk to an AI Doctor")
        if aiDoctor:
            switch_page(page_name="Talk")

    st.divider()


if __name__ == "__main__":
    main()
