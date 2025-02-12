import os
import streamlit as st
import base64
from data.tad_data import tad_data, map_TrafficLightState, map_APIndStat
# ... other imports as needed ...

current_dir = os.path.dirname(os.path.abspath(__file__))

style_sheet = os.path.join(current_dir, '..', 'assets', 'style.css')
yellow_ind  = os.path.join(current_dir, '..', 'assets', 'yellow_ind.png')
green_ind   = os.path.join(current_dir, '..', 'assets', 'green_ind.png')
gray_ind    = os.path.join(current_dir, '..', 'assets', 'gray_ind.png')
car_warning = os.path.join(current_dir, '..', 'assets', 'car_warning.png')
warning     = os.path.join(current_dir, '..', 'assets', 'warning.png')

def enum_to_path(i):
    if i == 2: return yellow_ind
    if i == 1: return green_ind
    else: return gray_ind

def create_app():
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

    # Keep track of last TAD data in session_state
    if 'tad_data_last' not in st.session_state:
        st.session_state['tad_data_last'] = tad_data.copy()

    # Keep track of current page in session_state
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'Home'

    # Simple function to switch pages
    def change_page(page_name):
        st.session_state['current_page'] = page_name
        # No forced st.rerun() here — a button click triggers re-run anyway.

    st.markdown("""
        <style>
        .custom-metric-container_main {
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin-bottom: 10px;
            
            /* Center horizontally and space out items */
            display: flex;
            justify-content: space-around;
            align-items: top;
        }
        
        /* Each sub-block in the row */
        .metric-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 0 20px; /* Optional extra spacing */
        }
        
        .metric-item-label {
            font-weight: bold;
            margin-bottom: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    def file_to_base64(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode("utf-8")
    
    green_b64 = file_to_base64(green_ind)
    yellow_b64 = file_to_base64(yellow_ind)
    
    # Example top-row container
    with st.container():
        with st.container():
            st.markdown(f"""
                <div class="custom-metric-container_main">
                
                  <!-- 1) Object Injection -->
                  <div class="metric-item">
                    <div class="metric-item-label">Obj Inject</div>
                    <img src="data:image/png;base64,{file_to_base64(enum_to_path(tad_data["Object_Injection"]))}" 
                         alt="Obj Inject" width="50" />
                  </div>
                
                  <!-- 2) Dyno Mode -->
                  <div class="metric-item">
                    <div class="metric-item-label">DYNO MODE</div>
                    <img src="data:image/png;base64,{file_to_base64(enum_to_path(tad_data["Dyno_Mode"]))}" 
                         alt="Dyno Mode" width="50" />
                  </div>
                
                  <!-- 3) Hands on Wheel -->
                  <div class="metric-item">
                    <div class="metric-item-label">HANDS ON WHEEL</div>
                    <!-- If you eventually want an image, you can place it below; 
                         or for text only, just leave it as is. -->
                  </div>
                
                  <!-- 4) Eyes on Road -->
                  <div class="metric-item">
                    <div class="metric-item-label">EYES ON ROAD</div>
                  </div>
                
                </div>
            """, unsafe_allow_html=True)

        left_column, right_column = st.columns([1, 3], gap="medium")

        with left_column:
            st.markdown(f"""
                <div class="custom-metric-container">
                    <div class="custom-metric-label">CACC MILEAGE</div>
                    <div class="custom-metric-value">{tad_data["C-ACC_Mileage"]}</div>
                </div>
            """, unsafe_allow_html=True)

            colA, colB = st.columns([1,1])
            with colA:
                st.markdown(f"""
                <div class="custom-metric-container">
                    <div class="custom-metric-label">Lead_Distance</div>
                    <div class="custom-metric-value">{tad_data["Lead_Distance"]}</div>
                </div>
            """, unsafe_allow_html=True)
            with colB:
                st.markdown(f"""
                <div class="custom-metric-container">
                    <div class="custom-metric-label">Lead_Headway</div>
                    <div class="custom-metric-value">{tad_data["Lead_Headway"]}</div>
                </div>
            """, unsafe_allow_html=True)
            
            traffic_light_colors = {
                "None Detected": "grey",
                "Red": "red",
                "Yellow": "Yellow",
                "Green": "green",
                "Error": "black"
            }

            text_color = traffic_light_colors.get(map_TrafficLightState[tad_data["TrafficLightState"]], "black")  # default to black if not found
            st.markdown(f"""
                <div class="custom-metric-container">
                    <div class="custom-metric-label">NEXT RIGHT:</div>
                    <!-- inline style sets the text color -->
                    <div class="custom-metric-value" style="color: {text_color};">
                        {map_TrafficLightState[tad_data["TrafficLightState"]]}
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
                <div class="custom-metric-container">
                    <div class="custom-metric-label">AUTOPARK:</div>
                    <div class="custom-metric-value">{map_APIndStat[tad_data["APIndStat"]]}</div>
                </div>
            """, unsafe_allow_html=True)

        with right_column:
            # We create a placeholder to hold page-specific content
            content_placeholder = st.empty()

            # Navigation container at bottom
            with st.container():
                nav_box = st.columns(4)
                with nav_box[0]:
                    if st.button('Home'):
                        change_page('Home')
                with nav_box[1]:
                    if st.button('CAV'):
                        change_page('CAV')
                with nav_box[2]:
                    if st.button('PCM'):
                        change_page('PCM')
                with nav_box[3]:
                    if st.button('Driver'):
                        change_page('Driver')
                        

        # Now display page content
        with content_placeholder.container():
            if st.session_state['current_page'] == 'Home':
                from navigation.home_page import display_main_content
                display_main_content()
            elif st.session_state['current_page'] == 'CAV':
                from navigation.cav_page import display_cav_data
                display_cav_data()
            elif st.session_state['current_page'] == 'PCM':
                from navigation.pcm_page import display_pcm_data
                display_pcm_data()
            elif st.session_state['current_page'] == 'Driver':
                from navigation.driver_page import display_driver_page
                display_driver_page()

def update_app():
    print("Simulated data updated in streamlit_app line: 218")
    if tad_data != st.session_state["tad_data_last"]:
        st.session_state["tad_data_last"] = tad_data.copy()
