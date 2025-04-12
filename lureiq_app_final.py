
import streamlit as st
import requests
import datetime

API_KEY = "e4645f9e139082f99ac7c6f704fc9044"
MOON_API = "https://api.weatherapi.com/v1/astronomy.json"

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
        data = requests.get(url).json()
        temp = data["main"]["temp"]
        wind = data["wind"]["speed"]
        condition = data["weather"][0]["main"].lower()
        weather = "sunny" if "clear" in condition else "cloudy"
        return weather, temp, wind
    except:
        return "unknown", None, None

def get_moon_phase(lake_name, date):
    try:
        lat, lon = lake_coords[lake_name]
        moon_response = requests.get(f"{MOON_API}?key={API_KEY}&q={lat},{lon}&dt={date}")
        moon_data = moon_response.json()
        return moon_data["astronomy"]["astro"]["moon_phase"]
    except:
        return "Unavailable"

# Define full 4-season lure data for all lakes
lake_data = {}
lure_set = {
    "spring": {
        "clear": {"sunny": ["Swimbaits", "Jerkbaits"], "cloudy": ["Spinnerbaits", "Chatterbaits"]},
        "stained": {"sunny": ["Texas rig"], "cloudy": ["Creature baits"]},
        "murky": {"sunny": ["Dark spinnerbaits"], "cloudy": ["Black jigs"]}
    },
    "summer": {
        "clear": {"sunny": ["Drop shot"], "cloudy": ["Flukes"]},
        "stained": {"sunny": ["Spinnerbaits"], "cloudy": ["Crankbaits"]},
        "murky": {"sunny": ["Frogs"], "cloudy": ["Heavy jigs"]}
    },
    "fall": {
        "clear": {"sunny": ["Topwater walkers"], "cloudy": ["Squarebills"]},
        "stained": {"sunny": ["Crankbaits"], "cloudy": ["Texas rigs"]},
        "murky": {"sunny": ["Buzzbaits"], "cloudy": ["Rattling crankbaits"]}
    },
    "winter": {
        "clear": {"sunny": ["Blade baits"], "cloudy": ["Underspins"]},
        "stained": {"sunny": ["Slow-rolled spinnerbaits"], "cloudy": ["Creature baits"]},
        "murky": {"sunny": ["Rattling lipless cranks"], "cloudy": ["Black/blue jigs"]}
    }
}
for lake in lake_coords:
    lake_data[lake] = lure_set

st.set_page_config(page_title="LureIQ", layout="centered")
st.title("🎣 LureIQ – Smart Lure Picker + Catch Log")

tabs = st.tabs(["Lure Picker", "Catch Log"])

with tabs[0]:
    lake = st.selectbox("Select Lake", list(lake_coords.keys()))
    season = st.selectbox("Season", ["spring", "summer", "fall", "winter"])
    clarity = st.selectbox("Water Clarity", ["clear", "stained", "murky"])
    manual_temp = st.text_input("Water Temp (°F)", placeholder="optional")

    if st.button("Get Weather & Moon"):
        lat, lon = lake_coords[lake]
        today = datetime.date.today()
        weather, air_temp, wind = get_weather(lat, lon)
        moon_phase = get_moon_phase(lake, today)
        st.success(f"Weather: **{weather}**, {air_temp}°F, Wind {wind} mph")
        st.info(f"Moon Phase: **{moon_phase}**")
    else:
        weather = "sunny"

    if st.button("Find Lures"):
        try:
            lures = lake_data[lake][season][clarity][weather]
            st.markdown("### Recommended Lures:")
            for lure in lures:
                st.write(f"- {lure}")
        except KeyError:
            st.warning("No lures found for that combination. Try changing a condition.")

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
