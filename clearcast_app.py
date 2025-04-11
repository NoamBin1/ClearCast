import streamlit as st
import requests

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

lake_data = {
    "Lake Keowee": {
        "spring": {
            "clear": {
                "sunny": ["Swimbaits", "Jerkbaits", "Ned rig"],
                "cloudy": ["Spinnerbaits", "Chatterbaits", "Finesse jigs"]
            },
            "stained": {
                "sunny": ["Texas rig", "Jigs", "Spinnerbaits"],
                "cloudy": ["Chatterbaits", "Creature baits", "Squarebills"]
            }
        },
        "summer": {
            "clear": {
                "sunny": ["Drop shot", "Shaky head", "Topwater (early/late)"],
                "cloudy": ["Swim jigs", "Underspins", "Flukes"]
            },
            "stained": {
                "sunny": ["Spinnerbaits", "Buzzbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Texas rig", "Crankbaits"]
            }
        }
    },
    "Lake Norman": {
        "spring": {
            "clear": {
                "sunny": ["Finesse swimbaits", "Jerkbaits", "Shaky head"],
                "cloudy": ["Spinnerbaits", "Ned rig", "Chatterbaits"]
            },
            "stained": {
                "sunny": ["Jigs", "Creature baits", "Spinnerbaits"],
                "cloudy": ["Chatterbaits", "Squarebills", "Buzzbaits"]
            }
        },
        "summer": {
            "clear": {
                "sunny": ["Drop shot", "Spybaits", "Topwater (early/late)"],
                "cloudy": ["Underspins", "Soft jerkbaits", "Swim jigs"]
            },
            "stained": {
                "sunny": ["Texas rig", "Buzzbaits", "Crankbaits"],
                "cloudy": ["Chatterbaits", "Jigs", "Squarebills"]
            }
        }
    },
    "Lake Wylie": {
        "spring": {
            "clear": {
                "sunny": ["Alabama rigs", "Jerkbaits", "Swimbaits"],
                "cloudy": ["Spinnerbaits", "Square-billed crankbaits", "Jigs"]
            },
            "stained": {
                "sunny": ["Lipless crankbaits", "Spinnerbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Square-billed crankbaits", "Jigs"]
            }
        },
        "summer": {
            "clear": {
                "sunny": ["Drop shots", "Shaky heads", "Topwater (early/late)"],
                "cloudy": ["Swim jigs", "Underspins", "Flukes"]
            },
            "stained": {
                "sunny": ["Spinnerbaits", "Buzzbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Texas rigs", "Crankbaits"]
            }
        }
    },
    "Lake Hartwell": {
        "spring": {
            "clear": {
                "sunny": ["Jerkbaits", "Carolina rigs", "Swimbaits"],
                "cloudy": ["Lipless crankbaits", "Spinnerbaits", "Jigs"]
            },
            "stained": {
                "sunny": ["Chatterbaits", "Square-billed crankbaits", "Jigs"],
                "cloudy": ["Spinnerbaits", "Texas rigs", "Crankbaits"]
            }
        },
        "summer": {
            "clear": {
                "sunny": ["Drop shots", "Shaky heads", "Deep-diving crankbaits"],
                "cloudy": ["Swim jigs", "Underspins", "Flukes"]
            },
            "stained": {
                "sunny": ["Spinnerbaits", "Buzzbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Texas rigs", "Crankbaits"]
            }
        }
    },
    "Lake Lanier": {
        "spring": {
            "clear": {
                "sunny": ["Jerkbaits", "Swimbaits", "Spinnerbaits"],
                "cloudy": ["Crankbaits", "Chatterbaits", "Finesse jigs"]
            },
            "stained": {
                "sunny": ["Lipless crankbaits", "Spinnerbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Square-billed crankbaits", "Jigs"]
            }
        },
        "summer": {
            "clear": {
                "sunny": ["Drop shots", "Shaky heads", "Topwater (early/late)"],
                "cloudy": ["Swim jigs", "Underspins", "Flukes"]
            },
            "stained": {
                "sunny": ["Spinnerbaits", "Buzzbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Texas rigs", "Crankbaits"]
            }
        }
    },
    "Lake Clarks Hill": {
        "spring": {
            "clear": {
                "sunny": ["Jerkbaits", "Swimbaits", "Spinnerbaits"],
                "cloudy": ["Crankbaits", "Chatterbaits", "Finesse jigs"]
            },
            "stained": {
                "sunny": ["Lipless crankbaits", "Spinnerbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Square-billed crankbaits", "Jigs"]
            }
        },
        "summer": {
            "clear": {
                "sunny": ["Drop shots", "Shaky heads", "Topwater (early/late)"],
                "cloudy": ["Swim jigs", "Underspins", "Flukes"]
            },
            "stained": {
                "sunny": ["Spinnerbaits", "Buzzbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Texas rigs", "Crankbaits"]
            }
        }
    },
    "Lake Murray": {
        "spring": {
            "clear": {
                "sunny": ["Jerkbaits", "Swimbaits", "Topwater lures"],
                "cloudy": ["Crankbaits", "Chatterbaits", "Finesse jigs"]
            },
            "stained": {
                "sunny": ["Lipless crankbaits", "Spinnerbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Square-billed crankbaits", "Jigs"]
            }
        },
        "summer": {
            "clear": {
                "sunny": ["Drop shots", "Shaky heads", "Topwater lures"],
                "cloudy": ["Swim jigs", "Underspins", "Flukes"]
            },
            "stained": {
                "sunny": ["Spinnerbaits", "Buzzbaits", "Jigs"],
                "cloudy": ["Chatterbaits", "Texas rigs", "Crankbaits"]
            }
        }
    }
}
        }
    }
    # You can expand this dictionary to include all other lakes as we did earlier
}

def get_weather(lat, lon):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
        response = requests.get(url)
        condition = response.json()["weather"][0]["main"].lower()
        return "sunny" if "clear" in condition else "cloudy"
    except:
        return "unknown"

# --- Streamlit Interface ---
st.set_page_config(page_title="ClearCast", layout="centered")
st.title("🎣 ClearCast – Smart Lure Picker")

lake = st.selectbox("Select Lake", list(lake_coords.keys()))
season = st.selectbox("Season", ["spring", "summer"])
clarity = st.selectbox("Water Clarity", ["clear", "stained"])

if st.button("Get Weather"):
    lat, lon = lake_coords[lake]
    weather = get_weather(lat, lon)
    st.success(f"Current weather at {lake}: **{weather}**")
else:
    weather = "sunny"

if st.button("Find Lures"):
    try:
        lures = lake_data[lake][season][clarity][weather]
        st.markdown("### Recommended Lures:")
        for lure in lures:
            st.write(f"- {lure}")
    except KeyError:
        st.error("No lure data for that combination yet.")
