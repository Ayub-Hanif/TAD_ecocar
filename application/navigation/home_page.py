from data.tad_data import *
import streamlit as st
from streamlit_app import enum_to_path

def display_main_content():

    # Define custom CSS for metric styling
    st.markdown("""
        <style>
        .custom-metric-container {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
            text-align: center;
        }
        .custom-metric-label {
            font-size: 16px; /* Smaller label font size */
            color: #ffffff;
        }
        .custom-metric-value {
            font-size: 18px; /* Larger value font size */
            font-weight: bold;
            color: #ffffff;
        }
        </style>
    """, unsafe_allow_html=True)


    c1, c2, c3 = st.columns([3,1.5, 1.5])


    color_mapping = {
        "Red": "#ff0000",    # Red
        "Yellow": "#ffff00", # Yellow
        "Green": "#00ff00",  # Green
        "None Detected": "#000000", # Black or default
        "Error": "#808080"        # Gray for fallback
    }
    # Get the color for the current traffic light state
    text_color = color_mapping.get(map_TrafficLightState[tad_data["TrafficLightState"]], "black")
    c1.markdown(f"""
        <div class="custom-metric-container">
            <div class="custom-metric-label">Next light is:</div>
            <!-- inline style sets the text color -->
            <div class="custom-metric-value" style="color: {text_color};">
                {map_TrafficLightState[tad_data["TrafficLightState"]]}
            </div>
        </div>
    """, unsafe_allow_html=True)
    #c1.markdown(f"""<style>.big-font
    #             {{font-size:30px !important;
    #                color: {text_color};
    #            }}</style>""", unsafe_allow_html=True)
    #c1.markdown(f'<p class="big-font">{traffic_light_state}</p>', unsafe_allow_html=True)
#
    c1.subheader("Distance to next light")
    with c1.container(border=True):
        st.write("Coming soon!!")

    
    c2.subheader("AUTO PARK")
    with c2.container(border=True):
            st.write(map_APIndStat[tad_data["APIndStat"]])
    with c2.container(border=True,):
        if st.button("Activate"):
            tad_data["AutoP_Activate"] = 1

        if st.button("Start"):
            tad_data["AutoP_Start"] = 1
        
        if st.button("Cancel"):
            tad_data["AutoP_Cancel"] = 1
        
        if st.button("Finish"):
            tad_data["AutoP_Finish"] = 1   