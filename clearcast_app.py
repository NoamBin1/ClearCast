import streamlit as st
import requests
import datetime

API_KEY = "e4645f9e139082f99ac7c6f704fc9044"

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

def get_weather(lat, lon):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
        response = requests.get(url)
        data = response.json()
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        condition = data["weather"][0]["main"].lower()
        weather = "sunny" if "clear" in condition else "cloudy"
        return weather, temp, wind
    except:
        return "unknown", None, None

# Placeholder for full lake_data (can be expanded)
lake_data = {
    "Lake Keowee": {
        "spring": {
            "clear": {
                "sunny": ["Swimbaits", "Jerkbaits", "Ned rig"],
                "cloudy": ["Spinnerbaits", "Chatterbaits", "Finesse jigs"]
            }
        },
        "summer": {
            "clear": {
                "sunny": ["Drop shot", "Shaky head", "Topwater (early/late)"],
                "cloudy": ["Swim jigs", "Underspins", "Flukes"]
            }
        }
    }
}

# --- Streamlit App UI ---
st.set_page_config(page_title="ClearCast", layout="centered")
st.title("🎣 ClearCast – Smart Lure Picker + Catch Log")

tabs = st.tabs(["Lure Picker", "Catch Log"])

with tabs[0]:
    lake = st.selectbox("Select Lake", list(lake_coords.keys()))
    season = st.selectbox("Season", ["spring", "summer", "fall", "winter"])
    clarity = st.selectbox("Water Clarity", ["clear", "stained", "murky"])

    if st.button("Get Weather"):
        lat, lon = lake_coords[lake]
        weather, temp, wind = get_weather(lat, lon)
        st.success(f"Weather at {lake}: **{weather}**, {temp}°F, Wind {wind} mph")
    else:
        weather = "sunny"

    if st.button("Find Lures"):
        lures = []
        try:
            lures = lake_data[lake][season][clarity][weather]
        except KeyError:
            if clarity == "murky":
                lures = ["Black/blue jigs", "Loud crankbaits", "Dark spinnerbaits"]
            elif season == "fall":
                lures = ["Squarebill crankbaits", "Buzzbaits", "Topwater walking baits"]
            elif season == "winter":
                lures = ["Blade baits", "Jerkbaits", "Jigs near structure"]
        if lures:
            st.markdown("### Recommended Lures:")
            for lure in lures:
                st.write(f"- {lure}")
        else:
            st.warning("No lure data found for that combination yet.")

with tabs[1]:
    st.subheader("Log a Catch")
    catch_date = st.date_input("Date", datetime.date.today())
    log_lake = st.selectbox("Lake", list(lake_coords.keys()), key="log_lake")
    lure_used = st.text_input("Lure Used")
    weight = st.text_input("Fish Weight (lbs)", placeholder="optional")
    notes = st.text_area("Notes")

    if st.button("Save Catch"):
        st.session_state["catch_log"].append({
            "date": catch_date,
            "lake": log_lake,
            "lure": lure_used,
            "weight": weight,
            "notes": notes
        })
        st.success("Catch logged successfully!")

    if st.session_state["catch_log"]:
        st.subheader("Catch History")
        for entry in reversed(st.session_state["catch_log"]):
            st.markdown(f"""
                **{entry['date']} – {entry['lake']}**
                - Lure: *{entry['lure']}*
                - Weight: {entry['weight']} lbs
                - Notes: {entry['notes']}
                ---
            """)
        
