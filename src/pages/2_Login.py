import streamlit as st

HEADER: str = """# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic
"""

def main()  ->  None:
    st.set_page_config(page_title="Login")
    st.write(HEADER)
    st.divider()
    name: str = st.text_input(label="Name", help="Your first and last name",)


if __name__ == "__main__":
    main()

