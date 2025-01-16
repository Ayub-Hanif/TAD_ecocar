import streamlit as st

def display_cav_data():
    st.title("CAV Data")
    st.write("This is the CAV data page. Explore the CAV metrics and actions.")

    st.subheader("Current Metrics")
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

    st.subheader("Actions")
    if st.button("Start CAV System"):
        st.success("CAV System started!")
    if st.button("Stop CAV System"):
        st.warning("CAV System stopped!")
    if st.button("Restart CAV System"):
        st.info("CAV System restarted!")
    
    return None, None, None, None
