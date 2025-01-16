from data.tad_data import *
import streamlit as st
from streamlit_app import enum_to_path

def display_main_content():
    st.title("Home Page")

    st.header("ISP Indicators")
    c1 = st.container()
    a1, a2, a3, a4, a5 = c1.columns(5)
    indicators = {
        "ind1": a1.image(enum_to_path(1), "Propulsion System Status", width=92),
        "ind2": a2.image(enum_to_path(2), "HV System Status", width=92),
        "ind3": a3.image(enum_to_path(0), "CAV Long. Cntrl. Status", width=92),
        "ind4": a4.image(enum_to_path(1), "CAV Lat. Cntrl. Status", width=92),
        "ind5": a5.image(enum_to_path(2), "CAV V2X Status", width=92),
    }

    st.header("PCM Data")
    c2 = st.container()
    b1, b2, b3, b4, b5, b6 = c2.columns(6)
    pcm_metrics = {
        "pcm1": b1.metric("Inst. Power Flow", 0.0),
        "pcm2": b2.metric("Wheel Power Flow", map_WheelPF(0)),
        "pcm3": b3.metric("HV Battery SOC", 0.0),
        "pcm4": b4.metric("HV Battery Avg. Cell Temp.", 0.0),
        "pcm5": b5.metric("Motor Temp.", 0.0),
        "pcm6": b6.metric("Drive Mode", map_DrvMode[0]),
    }

    st.header("CAV Data")
    c3 = st.container()
    d1, d2, d3, d4 = c3.columns(4)
    cav_metrics = {
        "cav1": d1.metric("APIndStat", map_APIndStat[0]),
        "cav2": d2.metric("TrafficLightState", map_TrafficLightState[0]),
        "cav3": d3.metric("IntersectAct", map_IntersectAct[0]),
        "cav4": d4.metric("DMCSCtrlSw", map_DMSCtrlSw[0]),
    }

    st.header("Automatic Parking Engagement")
    c4 = st.container()
    e1, e2, e3, e4 = c4.columns(4)
    ape_metrics = {
        "ape1": e1.button("AP Activate"),
        "ape2": e2.button("AP Start"),
        "ape3": e3.button("AP Cancel"),
        "ape4": e4.button("AP Finish"),
    }

    return indicators, pcm_metrics, cav_metrics, ape_metrics