import streamlit as st

def display_driver_page():
    st.title("Driver Page")
    sub_page = st.radio("Driver Options", options=["Overview", "Contactors"], index=0, horizontal=True)

    if sub_page == "Overview":
        st.write("This is the Driver Overview page.")
    elif sub_page == "Contactors":
        st.write("Displaying contactor information...")
    
    return None, None, None, None
