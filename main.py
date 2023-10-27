import streamlit as st

def run():
    st.set_page_config(
        page_title="Industry Tracker",
        page_icon="😆",
    )
    
    st.write("# Welcome! 👋")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This is a sample demo of multiple streamlit dashboards for different industries.

        **👈 Select a demo from the sidebar** to see some examples
        of what we created!
    """
    )

if __name__ == "__main__":
    run()