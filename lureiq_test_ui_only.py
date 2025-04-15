import streamlit as st
import datetime

lake_coords = {
    "Lake Keowee": (34.8011, -82.8921),
    "Lake Norman": (35.5110, -80.8929),
    "Lake Wylie": (35.1020, -81.0438),
    "Lake Hartwell": (34.4458, -82.8576),
    "Lake Lanier": (34.2166, -83.8687),
    "Lake Clarks Hill": (33.6606, -82.1608),
    "Lake Murray": (34.0490, -81.2162)
}

if "catch_log" not in st.session_state:
    st.session_state["catch_log"] = []

# Basic fallback lure data
lake_data = {}
lure_set = {
    "spring": {
        "clear": {"sunny": ["Swimbaits", "Jerkbaits"], "cloudy": ["Spinnerbaits"]},
        "stained": {"sunny": ["Texas rig"], "cloudy": ["Creature baits"]},
        "murky": {"sunny": ["Dark spinnerbaits"], "cloudy": ["Black jigs"]}
    }
}
for lake in lake_coords:
    lake_data[lake] = lure_set

st.set_page_config(page_title="LureIQ - Test", layout="centered")
st.title("🎣 LureIQ – Test Version")

tabs = st.tabs(["Lure Picker", "Catch Log"])

with tabs[0]:
    lake = st.selectbox("Select Lake", list(lake_coords.keys()))
    season = st.selectbox("Season", ["spring"])
    clarity = st.selectbox("Water Clarity", ["clear", "stained", "murky"])
    weather = st.selectbox("Weather", ["sunny", "cloudy"])
    st.text_input("Water Temp (°F)", placeholder="optional")

    if st.button("Find Lures"):
        try:
            lures = lake_data[lake][season][clarity][weather]
            st.markdown("### Recommended Lures:")
            for lure in lures:
                st.write(f"- {lure}")
        except KeyError:
            st.warning("No lures found for that combo.")

with tabs[1]:
    st.subheader("Log a Catch")
    catch_date = st.date_input("Date", datetime.date.today())
    log_lake = st.selectbox("Lake", list(lake_coords.keys()), key="log_lake")
    lure_used = st.text_input("Lure Used")
    weight = st.text_input("Fish Weight (lbs)", placeholder="optional")
    notes = st.text_area("Notes")
    log_temp = st.text_input("Water Temp (°F)", placeholder="optional")

    if st.button("Save Catch"):
        st.session_state["catch_log"].append({
            "date": catch_date,
            "lake": log_lake,
            "lure": lure_used,
            "weight": weight,
            "notes": notes,
            "temp": log_temp
        })
        st.success("Catch logged!")

    if st.session_state["catch_log"]:
        st.subheader("Catch History")
        for entry in reversed(st.session_state["catch_log"]):
            st.markdown(f"""**{entry['date']} – {entry['lake']}**
- Lure: *{entry['lure']}*
- Weight: {entry['weight']} lbs
- Temp: {entry['temp']}°F
- Notes: {entry['notes']}
---
""")
