import json

file = open("states.json" , "w")
states_dict = {
    "Madhya Pradesh" : "Bhopal",
    "Maharashtra" : "Mumbai",
    "Rajasthan" : "Jaipur",
    "Gujarat" : "Gandhinagar",
    "Karnataka" : "Bengaluru",
    "Punjab" : "Chandigarh",
    "West Bengal" : "Kolkata"
    }
json.dump(states_dict , file)