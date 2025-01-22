import streamlit as st
from data.tad_data import *

def display_pcm_data():

    with st.container(border=False):
        col1, col2 = st.columns(spec= 2, border=False, gap="small", vertical_alignment="center")
        with col1.container():
            st.subheader("HV:#")

        with col2.container():
           st.subheader("LV:#")


    with st.container():
        st.metric(label="HV Battery SOC(%)", value=tad_data["RESSBattSOC"])

    with st.container():
        st.metric(label="HV Battery AVG Cell Temp (C)", value=tad_data["RESSBattAvgCellTemp"])
    with st.container():
        st.metric(label="Motor Temp (C)", value=tad_data["EDUDriveTemp"])
    with st.container():
        st.metric(label="Drive Mode", value=map_DrvMode[tad_data["DrvMode"]])
    return None, None, None, None
