import streamlit as st

def display_pcm_data():
    st.title("PCM Data")
    st.write("This is the PCM data page. Here you can monitor PCM metrics.")

    st.subheader("PCM Metrics")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Inst. Power Flow", value="3.5 kW")
    with col2:
        st.metric(label="Wheel Power Flow", value="2.8 kW")
    with col3:
        st.metric(label="Battery Level", value="78%")

    col4, col5 = st.columns(2)
    with col4:
        st.metric(label="HV Battery Avg. Cell Temp.", value="32°C")
    with col5:
        st.metric(label="Motor Temp.", value="44°C")

    st.subheader("PCM Actions")
    if st.button("Enable Power Flow Monitoring"):
        st.success("Power Flow Monitoring Enabled")
    if st.button("Disable Power Flow Monitoring"):
        st.warning("Power Flow Monitoring Disabled")
    
    return None, None, None, None
