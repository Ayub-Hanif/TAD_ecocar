import streamlit as st
from data.tad_data import *
from streamlit_app import enum_to_path
def display_pcm_data():

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

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.image(enum_to_path(1), "Propulsion sys", width=55),
    a2.image(enum_to_path(2), "HV Sys", width=55),
    a3.image(enum_to_path(0), "Long. Cntrl", width=55),
    a4.image(enum_to_path(1), "Lat. Ctrl", width=55),
    a5.image(enum_to_path(2), "V2X", width=55)


    left_side,right_side= st.columns(2)

    with left_side:
            # Replace st.metric with custom HTML
            st.markdown(f"""
                <div class="custom-metric-container">
                    <div class="custom-metric-label">Inst. Power Flow</div>
                    <div class="custom-metric-value">{tad_data["PSS"]}</div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                <div class="custom-metric-container">
                    <div class="custom-metric-label">HV Battery SOC (%)</div>
                    <div class="custom-metric-value">{tad_data["RESSBattSOC"]}%</div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                <div class="custom-metric-container">
                    <div class="custom-metric-label">HV Battery AVG Cell Temp (°C)</div>
                    <div class="custom-metric-value">{tad_data["RESSBattAvgCellTemp"]}°C</div>
                </div>
            """, unsafe_allow_html=True)

    with right_side:
        st.markdown(f"""
            <div class="custom-metric-container">
                <div class="custom-metric-label">Motor Temp (°C)</div>
                <div class="custom-metric-value">{tad_data["EDUDriveTemp"]}°C</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="custom-metric-container">
                <div class="custom-metric-label">Drive Mode</div>
                <div class="custom-metric-value">{map_DrvMode[tad_data["DrvMode"]]}</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
            <div class="custom-metric-container">
                <div class="custom-metric-label">Bus Voltage</div>
                <div class="custom-metric-value">{tad_data["BusVoltage"]}V</div>
            </div>
        """, unsafe_allow_html=True)