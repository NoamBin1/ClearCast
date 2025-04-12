import streamlit as st
import requests

API_KEY = "your_api_key_here"

lake_coords = {
    "Lake Keowee": (34.8011, -82.8921),
    "Lake Norman": (35.5110, -80.8929)
}

st.set_page_config(page_title="LureIQ", layout="centered")
st.title("🎣 LureIQ – Smart Lure Picker")

lake = st.selectbox("Select a Lake", list(lake_coords.keys()))
st.write(f"You selected: {lake}")