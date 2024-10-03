import streamlit as st
from trail import automation

st.title("LinkedIn Automation")


linkedin_username = st.text_input("Enter LinkedIn Username:")
linkedin_password = st.text_input("Enter LinkedIn Password:")
search_query = st.text_input("Enter Position:")

if st.button("Submit"):
    if linkedin_username and linkedin_password and search_query:
        # Call the automation function with user inputs
        st.info("Starting LinkedIn automation...")
        try:
            automation(linkedin_username, linkedin_password, search_query)
            st.success("Automation completed successfully!")
        except Exception as e:
            st.error(f"An error occurred during automation: {str(e)}")
    else:
        st.warning("Please fill in all fields before submitting.")

