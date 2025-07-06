import streamlit as st
from datetime import date

# Konfigurasi halaman agar tidak terlalu besar
st.set_page_config(page_title="TrafficSync Widget", layout="centered")

# Kontainer agar tampil lebih ringkas
with st.container():
    st.title("🚦 TrafficSync Dashboard")
    
    # Widget date input
    selected_date = st.date_input("Select Date", date.today())

    # Tampilkan data dummy
    st.write(f"📅 You selected: {selected_date}")

