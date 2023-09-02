import streamlit as st
from ..conf import hideSidebarCSS, pageState

HEADER: str = """# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic
"""

def main()  ->  None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)
    name: str = st.text_input(label="Name", help="Your first and last name",)

    st.divider()

if __name__ == "__main__":
    main()

