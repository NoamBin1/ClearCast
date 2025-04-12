lake_data = {}
spring = {
    "spring": {
        "clear": {
            "sunny": ["Swimbaits", "Jerkbaits", "Ned rig"],
            "cloudy": ["Spinnerbaits", "Chatterbaits", "Finesse jigs"]
        },
        "stained": {
            "sunny": ["Texas rig", "Jigs", "Spinnerbaits"],
            "cloudy": ["Chatterbaits", "Creature baits", "Squarebills"]
        },
        "murky": {
            "sunny": ["Dark spinnerbaits", "Black/blue jigs", "Slow-rolled buzzbaits"],
            "cloudy": ["Black jigs", "Rattling crankbaits", "Bladed jigs"]
        }
    }
}
summer = {
    "summer": {
        "clear": {
            "sunny": ["Drop shot", "Shaky head", "Topwater (early/late)"],
            "cloudy": ["Swim jigs", "Underspins", "Flukes"]
        },
        "stained": {
            "sunny": ["Spinnerbaits", "Buzzbaits", "Jigs"],
            "cloudy": ["Chatterbaits", "Texas rig", "Crankbaits"]
        },
        "murky": {
            "sunny": ["Loud spinnerbaits", "Black/blue jigs", "Topwater frogs"],
            "cloudy": ["Dark chatterbaits", "Squarebills", "Heavy jigs"]
        }
    }
}
fall = {
    "fall": {
        "clear": {
            "sunny": ["Topwater walkers", "Jerkbaits", "Spinnerbaits"],
            "cloudy": ["Buzzbaits", "Chatterbaits", "Squarebill crankbaits"]
        },
        "stained": {
            "sunny": ["Crankbaits", "Spinnerbaits", "Flukes"],
            "cloudy": ["Chatterbaits", "Texas rigs", "Bladed jigs"]
        },
        "murky": {
            "sunny": ["Dark spinnerbaits", "Black buzzbaits", "Loud squarebills"],
            "cloudy": ["Black/blue jigs", "Rattling crankbaits", "Chatterbaits"]
        }
    }
}
winter = {
    "winter": {
        "clear": {
            "sunny": ["Jerkbaits", "Drop shot", "Blade baits"],
            "cloudy": ["Jigs", "Shaky heads", "Underspins"]
        },
        "stained": {
            "sunny": ["Deep crankbaits", "Slow-rolled spinnerbaits", "Football jigs"],
            "cloudy": ["Chatterbaits", "Jigs", "Creature baits"]
        },
        "murky": {
            "sunny": ["Dark jigs", "Heavy spinnerbaits", "Rattling lipless cranks"],
            "cloudy": ["Black/blue jigs", "Chatterbaits", "Slow Texas rigs"]
        }
    }
}

lake_names = [
    "Lake Keowee", "Lake Norman", "Lake Wylie",
    "Lake Hartwell", "Lake Lanier", "Lake Clarks Hill", "Lake Murray"
]

# Apply full seasonal data to all lakes
for lake in lake_names:
    lake_data[lake] = {}
    lake_data[lake].update(spring)
    lake_data[lake].update(summer)
    lake_data[lake].update(fall)
    lake_data[lake].update(winter)
