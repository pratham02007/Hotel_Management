import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("🔧 Advanced Booking")

name = st.text_input("Name")
room_type = st.selectbox("Room Type", ["Single", "Double", "Deluxe"])
room_prices = {
    "Single": 1500,
    "Double": 2200,
    "Deluxe": 3000
}
st.markdown(f"💰 Price per day for {room_type} room: ₹{room_prices[room_type]}")
days = st.number_input("Duration (days)", min_value=1)

cost_per_day = 2500
meal_cost = 500
pickup_cost = 1000

base_cost = days * cost_per_day
total_cost = base_cost

booking_date = datetime.now().strftime("%Y-%m-%d")

if st.button("Confirm Booking"):
    if name.strip() == "":
        st.warning("Please enter your name.")
    else:
        booking_data = {
            "BookingID": f"AB{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "Name": name,
            "RoomType": room_type,
            "Days": days,
            "MealIncluded": "Yes" if with_meal else "No",
            "AirportPickup": "Yes" if airport_pickup else "No",
            "TotalCost": total_cost,
            "BookingDate": booking_date
        }

        file_path = "data/bookings.csv"
        df = pd.DataFrame([booking_data])
        if os.path.exists(file_path):
            df.to_csv(file_path, mode='a', header=False, index=False)
        else:
            df.to_csv(file_path, index=False)

        st.success(f"{name}, your {room_type} room is booked for ₹{total_cost}")
        st.info(f"📅 Booking ID: {booking_data['BookingID']}")
