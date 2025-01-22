import sys
import os
import time
import streamlit as st


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
    indicators, pcm_metrics, cav_metrics, ape_metrics = streamlit_app.create_app()
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
                streamlit_app.update_app(tad_data, indicators, pcm_metrics, cav_metrics, ape_metrics)
                
                # Send data back to network
                ethernet.send_tad_data(s)
            except (ethernet.socket.timeout, BlockingIOError):
                print("No data received")
                continue

            time.sleep(0.15)  # Polling interval

# Function for Streamlit-only operation
def run_streamlit_only():
    indicators, pcm_metrics, cav_metrics, ape_metrics = streamlit_app.create_app()
    global tad_data
    
    # Simulate data update loop
    while True:
        tad_data.update({
            "PSS": 1,
            "HVSS": 2,
            "CAVLongCS": 0,
            "CAVLatCS": 1, #no TAD Visualization
            "CAVV2XS": 2, #no TAD Visualization
            "InstPF": 1.14112321312, 
            "WheelPF": 1,
            "RESSBattSOC": 2.0,
            "RESSBattAvgCellTemp": 32.5,
            "EDUDriveTemp": 42.1,
            "DrvMode": 2,
            "APIndStat": 2,
            "TrafficLightState": 1,
            "IntersectAct": 2,
            "DMSCtrlSw": 3,
            "BusVoltage": 325.2,
            "C-ACC_Mileage" : 32.3
        })

        # Simulate switch data
        switch_data = [True, False, True, False]  # Simulated switch states
        updateSwitchData(switch_data)
        
        # Update Streamlit display with new data
        streamlit_app.update_app(tad_data, indicators, pcm_metrics, cav_metrics, ape_metrics)
        time.sleep(0.2)  # Polling interval

#----------------------------------------------

if __name__ == "__main__":
    main()
