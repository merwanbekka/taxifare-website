import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
date = st.date_input("Date")

time = st.time_input("Time")

pickup_longitude = st.number_input("Pickup longitude")

pickup_latitude = st.number_input("Pickup latitude")

dropoff_longitude = st.number_input("Dropoff longitude")

dropoff_latitude = st.number_input("Dropoff latitude")

passenger_count = st.number_input(
    "Passenger count",
    min_value=1,
    max_value=8,
    value=1
)

import requests
url = "https://taxifare.lewagon.ai/predict"
params = {
    "pickup_datetime": f"{date} {time}",
    "pickup_longitude": pickup_longitude,
    "pickup_latitude": pickup_latitude,
    "dropoff_longitude": dropoff_longitude,
    "dropoff_latitude": dropoff_latitude,
    "passenger_count": passenger_count
}

response = requests.get(url, params=params)
prediction = response.json()

fare = prediction["fare"]
st.write(f"Predicted fare: ${fare:.2f}")
