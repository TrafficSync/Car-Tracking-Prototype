import streamlit as st
import json
import time

st.set_page_config(page_title="TrafficSync Realtime Counter", layout="centered")
st.title("🚦 TrafficSync Realtime Vehicle Count")

placeholder = st.empty()

while True:
    try:
        with open("count_data.json", "r") as f:
            data = json.load(f)
    except:
        data = {"left": 0, "right": 0}

    with placeholder.container():
        st.metric(label="🟢 Left Line Count", value=data["left"])
        st.metric(label="🔴 Right Line Count", value=data["right"])

    time.sleep(1)  # update setiap detik
