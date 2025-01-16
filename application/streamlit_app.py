import os
import streamlit as st
from data.tad_data import *


# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Paths to resource directories
style_sheet = os.path.join(current_dir, '..', 'assets', 'style.css')
yellow_ind  = os.path.join(current_dir, '..', 'assets', 'yellow_ind.png')
green_ind   = os.path.join(current_dir, '..', 'assets', 'green_ind.png')
gray_ind    = os.path.join(current_dir, '..', 'assets', 'gray_ind.png')
#----------------------------------------------

# Indicator helper function
def enum_to_path(i):
    if i == 2: return yellow_ind
    if i == 1: return green_ind
    else: return gray_ind
#----------------------------------------------

ind1, ind2, ind3, ind4, ind5 = None, None, None, None, None
pcm1, pcm2, pcm3, pcm4, pcm5, pcm6 = None, None, None, None, None, None
cav1, cav2, cav3, cav4 = None, None, None, None

#----------------------------------------------

def create_app():
    
    st.set_page_config(layout="wide", page_title="CACC Dashboard")


    # Initialize session state for current page if not set
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'Home'

    # Function to change page
    def change_page(page_name):
        st.session_state['current_page'] = page_name
        st.session_state['content_placeholder'] = st.empty()  # Reset the content container
        st.rerun()

    with st.container(border=True):

        with st.container(border=True):
            col1, col2, col3, col4 = st.columns(spec= 4, border=False, gap="small", vertical_alignment="center")
            with col1:
                st.image("car_warning.png")
                
            with col2:
                st.image("warning.png")

            with col3.container(border=True):
                st.write("HANDS ON WHEEL")

            with col4.container(border=True):
                st.write("EYES ON ROAD")


        # Create a layout with a fixed sidebar on the left and main content area on the right
        left_column, right_column = st.columns([1, 3], vertical_alignment ="center" ,gap="medium")

        # Left Column - Acting as a Fixed Sidebar
        with left_column:
            with st.container(border=True):
                st.write("CACC")
                st.write("MILEAGE")
                with st.container(border=True):
                    st.write("25.3 mi")

            
            with st.container(border=True):
                st.write("LCC")
                st.write("STATUS")
                with st.container(border=True):
                    st.write("STANDBY")

            with st.container(border=True):
                st.write("LEAD CAR DISTANCE")
                
                #we have to change the values into the actual values after!!
                col1, col2 = st.columns(2, border=True)
                with col1:
                    st.write("300")

                with col2:
                    st.write("100")
            
            with st.container(border=True):
                st.write("AIN")

            with st.container(border=True):
                st.write("NEXT RIGHT:", "RED")
                
                col1, col2 = st.columns(2, border=False)
                with col1: 
                    st.write("AUTOPARK:")
                with col2.container(border=True):
                    st.write("READY")

                



    
        with right_column:
            # Placeholder for content that will be dynamically cleared on page change
            content_placeholder = st.empty()

            # Navigation bar at the bottom
            with st.container(border=True):
                nav_box = st.columns(4, gap="large")
                with nav_box[0]:
                    if st.button('Home'):
                        indicators, pcm_metrics, cav_metrics, ape_metrics = change_page('Home')
                with nav_box[1]:
                    if st.button('CAV'):
                        change_page('CAV')
                        indicators, pcm_metrics, cav_metrics, ape_metrics = None, None, None, None
                with nav_box[2]:
                    if st.button('PCM'):
                        change_page('PCM')
                        indicators, pcm_metrics, cav_metrics, ape_metrics = None, None, None, None
                with nav_box[3]:
                    if st.button('Driver'):
                        change_page('Driver')
                        indicators, pcm_metrics, cav_metrics, ape_metrics = None, None, None, None

        # Clear content for previous pages
        with content_placeholder.container():
            # Display page content based on the selected page
            if st.session_state['current_page'] == 'Home':
                from navigation.home_page import display_main_content
                indicators, pcm_metrics, cav_metrics, ape_metrics = display_main_content()
            elif st.session_state['current_page'] == 'CAV':
                from navigation.cav_page import display_cav_data
                indicators, pcm_metrics, cav_metrics, ape_metrics = display_cav_data()
            elif st.session_state['current_page'] == 'PCM':
                from navigation.pcm_page import display_pcm_data
                indicators, pcm_metrics, cav_metrics, ape_metrics = display_pcm_data()
            elif st.session_state['current_page'] == 'Driver':
                from navigation.driver_page import display_driver_page
                indicators, pcm_metrics, cav_metrics, ape_metrics = display_driver_page()
    return indicators, pcm_metrics, cav_metrics, ape_metrics

#----------------------------------------------

def update_app(tad_data, indicators, pcm_metrics, cav_metrics, ape_metrics):
    if indicators:
        indicators["ind1"].image(enum_to_path(tad_data["PSS"]), "Propulsion System Status", width=92)
        indicators["ind2"].image(enum_to_path(tad_data["HVSS"]), "HV System Status", width=92)
        indicators["ind3"].image(enum_to_path(tad_data["CAVLongCS"]), "CAV Long. Cntrl. Status", width=92)
        indicators["ind4"].image(enum_to_path(tad_data["CAVLatCS"]), "CAV Lat. Cntrl. Status", width=92)
        indicators["ind5"].image(enum_to_path(tad_data["CAVV2XS"]), "CAV V2X Status", width=92)

    if pcm_metrics:
        pcm_metrics["pcm1"].metric("Inst. Power Flow", '%.3f' % (tad_data["InstPF"]))
        pcm_metrics["pcm2"].metric("Wheel Power Flow", map_WheelPF(tad_data["WheelPF"]))
        pcm_metrics["pcm3"].metric("HV Battery SOC", '%.3f' % (tad_data["RESSBattSOC"]))
        pcm_metrics["pcm4"].metric("HV Battery Avg. Cell Temp.", '%.3f' % (tad_data["RESSBattAvgCellTemp"]))
        pcm_metrics["pcm5"].metric("Motor Temp.", '%.3f' % (tad_data["EDUDriveTemp"]))
        pcm_metrics["pcm6"].metric("Drive Mode", map_DrvMode[tad_data["DrvMode"]])

    if cav_metrics:
        cav_metrics["cav1"].metric("APIndStat", map_APIndStat[tad_data["APIndStat"]])
        cav_metrics["cav2"].metric("TrafficLightState", map_TrafficLightState[tad_data["TrafficLightState"]])
        cav_metrics["cav3"].metric("IntersectAct", map_IntersectAct[tad_data["IntersectAct"]])
        cav_metrics["cav4"].metric("DMCSCtrlSw", map_DMSCtrlSw[tad_data["DMSCtrlSw"]])

    return indicators, pcm_metrics, cav_metrics
