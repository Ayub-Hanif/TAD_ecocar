from data.tad_data import *
import streamlit as st
from streamlit_app import enum_to_path
def display_cav_data():

    button_style = """ <style>.green-button
                    {
                    background-color: #4CAF50; /* Green color */
                    color: white; padding: 10px 20px;
                    border: none;
                    cursor: pointer;
                    }
                    .green-button:hover {
                    background-color: #45a049; /* Darker green on hover */
                    }
                    </style>"""
    st.markdown(button_style, unsafe_allow_html=True) 

    c1,c2,c3 = st.columns([2,0.5,2])

    with c1.container(border=True):
        st.write("CAV DYNO Mode")
        if st.toggle("Power On"):
            updateButtonData("Cav_Dyno")
    
    with c2.container(border=True):
        st.write("CACC")
        st.image(enum_to_path(2), width=55)

    

    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Speed", value="45 km/h", delta="+2 km/h")
    with col2:
        st.metric(label="Distance to Obstacle", value="120 m", delta="-5 m")

    col3, col4 = st.columns(2)
    with col3:
        st.metric(label="Battery Level", value="85%")
    with col4:
        st.metric(label="Signal Strength", value="Good")
