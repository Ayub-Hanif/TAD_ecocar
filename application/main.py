import sys
import os
import time
import streamlit as st

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

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
        # Network socket setup
        with ethernet.start_socket() as s:
            try:
                ethernet.connect_socket(s)
            except OSError:
                print("re-run detected")
                
            indicators, pcm_metrics, cav_metrics, ape_metrics = streamlit_app.create_app()
            while True:
                time.sleep(0.5)

                try:
                    ethernet.get_tad_data(s)
                    gpio.refreshIndicatorPanel(getIndicatorPanelValues())
                    updateSwitchData(gpio.getSwitchData())

                except (ethernet.socket.timeout, BlockingIOError):
                    print("No data received")
                    continue

                #either streamlit_app or st
                st.update_app(tad_data, indicators, pcm_metrics, cav_metrics, ape_metrics)
                ethernet.send_tad_data(s)

# Function for Streamlit-only operation
def run_streamlit_only():
    indicators, pcm_metrics, cav_metrics, ape_metrics = streamlit_app.create_app()
    
    # Simulate data update loop
    while True:
        tad_data = {
            "PSS": 1,
            "HVSS": 2,
            "CAVLongCS": 0,
            "CAVLatCS": 1, #no TAD Visualization
            "CAVV2XS": 2, #no TAD Visualization
            "InstPF": 3.141, 
            "WheelPF": 1,
            "RESSBattSOC": 75.0,
            "RESSBattAvgCellTemp": 32.5,
            "EDUDriveTemp": 42.1,
            "DrvMode": 1,
            "APIndStat": 0,
            "TrafficLightState": 1,
            "IntersectAct": 2,
            "DMSCtrlSw": 3
            
        }
        
        # Update Streamlit display with new data
        streamlit_app.update_app(tad_data, indicators, pcm_metrics, cav_metrics, ape_metrics)
        time.sleep(0.5)  # Update interval

#----------------------------------------------

if __name__ == "__main__":
    main()
