import sys
import os
import time
import streamlit as st
import random
from streamlit_autorefresh  import st_autorefresh
import streamlit.components.v1 as components


st.set_page_config(layout="wide", page_title="CACC Dashboard")
st.markdown(
    """
    <style>
    /* Override the gap for the classes in question */
    .st-emotion-cache-cdgltb {
        gap: 0rem !important;
    }
    .st-emotion-cache-12h60ca {
        gap: 0rem !important;
    }
    .st-emotion-cache-1b1b1b1 {
        gap: 0rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Remove padding and allow full width for the main container */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
        width: 100%;
    }
    /* Optionally, hide the header if you want to reclaim even more space */
    header { 
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* Hide the scrollbar for Chrome, Safari and Opera */
    ::-webkit-scrollbar {
        display: none;
    }
    /* Hide scrollbar for IE, Edge and Firefox */
    body, .main, .block-container {
        overflow: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.set_option('client.toolbarMode', 'minimal')

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

# Toggle for simulation or real data
streamlit_only = True

#----------------------------------------------

from data.tad_data import *
from network import ethernet
from application import streamlit_app

if not streamlit_only:
    from hardware import gpio

# Main function
def main():
    if streamlit_only:
        run_streamlit_only()
    else:
        run_with_real_data()


def run_with_real_data():
    # Set up an auto-refresh every 500 ms (0.5 seconds). Adjust as needed.
    count = st_autorefresh(interval=2000, limit=None, key="sim_auto_refresh")
    streamlit_app.create_app()
    # Network socket setup
    with ethernet.start_socket() as s:
        try:
            ethernet.connect_socket(s)
        except OSError:
            print("re-run detected")
            
        while True:
            try:
                # Fetch data from network
                ethernet.get_tad_data(s)

                # Refresh indicator panel based on real switch data
                gpio.refreshIndicatorPanel(getIndicatorPanelValues())
                updateSwitchData(gpio.getSwitchData())

                # Update UI with new data
                streamlit_app.update_app()
                
                # Send data back to network
                ethernet.send_tad_data(s)
            except (ethernet.socket.timeout, BlockingIOError):
                print("No data received")
                continue

            #time.sleep(0.1)  # Polling interval

# Function for Streamlit-only operation
def run_streamlit_only():
    """
    Replaces the old `while True:` loop with a timed auto-refresh.
    Each run, we generate new random data to simulate updates.
    """

    # Set up an auto-refresh every 500 ms (0.5 seconds). Adjust as needed.
    count = st_autorefresh(interval=2000, limit=None, key="sim_auto_refresh")

    # Generate new random values on each re-run
    number_C_ACC = random.randint(1, 100)
    Lead_Distance = random.randint(1, 10)
    Lead_Headway = random.randint(1, 20)

    streamlit_app.create_app()
    # Update global tad_data with simulated values
    tad_data.update({
        "PSS": 12,
        "HVSS": 2,
        "CAVLongCS": 0,
        "CAVLatCS": 1, # no TAD Visualization
        "CAVV2XS": 2,  # no TAD Visualization
        "InstPF": number_C_ACC,
        "WheelPF": 1,
        "RESSBattSOC": 2.00,
        "RESSBattAvgCellTemp": 32.50,
        "EDUDriveTemp": 42,
        "DrvMode": 1,
        "APIndStat": 3,
        "TrafficLightState": 1,
        "IntersectAct": 2,
        "DMSCtrlSw": 1,
        "BusVoltage": 1.0,
        "C-ACC_Mileage": number_C_ACC,
        "Lead_Distance": Lead_Distance,
        "Lead_Headway": Lead_Headway,
        "Object_Injection": 1,
        "Dyno_Mode": 0
    })

    # Simulate switch data
    switch_data = [True, False, True, False]  # Example states
    updateSwitchData(switch_data)
    print("Simulated data updated in main line: 111")

    #time.sleep(0.5)  # Polling interval

    # Create the Streamlit app layout (once per run)

    # Then do partial (in-code) updates, if needed.
    # But DO NOT do st.rerun() in update_app() (see below).
    streamlit_app.update_app()

        

#----------------------------------------------

if __name__ == "__main__":
    main()
