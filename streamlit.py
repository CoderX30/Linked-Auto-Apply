import streamlit as st
from main import automation
import traceback
import sys

st.title("Google Maps Search")

# Create input field
search_query = st.text_input("Enter location to search on Google Maps:")

# Create a submit button
if st.button("Search on Google Maps"):
    if search_query:
        # Call the automation function with user input
        st.info(f"Searching for '{search_query}' on Google Maps...")
        try:
            with st.spinner("Performing search..."):
                result_url = automation(None, None, search_query)
            if result_url:
                st.success("Search completed successfully!")
                st.markdown(f"[Click here to view the results on Google Maps]({result_url})")
            else:
                st.error("An error occurred during the search. Please check the logs for more details.")
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.error("Detailed error information:")
            st.code(traceback.format_exc())
            st.error("System Information:")
            st.code(f"Python version: {sys.version}\n"
                    f"Platform: {sys.platform}\n"
                    f"Executable: {sys.executable}")
    else:
        st.warning("Please enter a location before searching.")

# Add debug information to the app
if st.checkbox("Show Debug Info"):
    st.write("Debug Information:")
    st.json({
        "Python Version": sys.version,
        "Platform": sys.platform,
        "Executable": sys.executable,
        "Working Directory": os.getcwd(),
        "Directory Contents": os.listdir(),
        "Environment Variables": dict(os.environ)
    })
