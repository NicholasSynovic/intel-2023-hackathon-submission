from pathlib import Path

import pandas
import streamlit as st
from hackathon_submission.conf import dbPath, hideSidebarCSS, pageState
from hackathon_submission.schemas.sql import SQL
from pandas import DataFrame
from streamlit_extras.switch_page_button import switch_page

HEADER: str = """# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## Report Symptoms
"""

def main() -> None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)

    st.divider()


if __name__ == "__main__":
    main()
