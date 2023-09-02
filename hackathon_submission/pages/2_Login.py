import streamlit as st
from hackathon_submission.conf import pageState, hideSidebarCSS

HEADER: str = """# Empire General Hospital Patient Portal
> A prototype developed by Nicholas M. Synovic

## Login

Test username: `user`\n
Test password: `password`
"""

def main()  ->  None:
    st.set_page_config(**pageState)
    st.markdown(**hideSidebarCSS)

    st.write(HEADER)
    name: str = st.text_input(label="Username", max_chars=30, type="default", help="Username",)
    password: str = st.text_input(label="Password", max_chars=30, type="password", help="Password",)

    col1, _, _, _, _, col2 = st.columns(spec=[1,1,1,1,1,1], gap="large")

    with col1:
        backButton: bool = st.button(label="Back")
    
    with col2:
        loginButton: bool = st.button(label="Login")

    st.divider()

if __name__ == "__main__":
    main()

