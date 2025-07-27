import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("🛏 Room Booking")

# Define room prices
room_prices = {
    "Single": 1500,
    "Double": 2200,
    "Deluxe": 3000,
    "Suite": 4500
}

# Input fields
name = st.text_input("Enter your name")
room_type = st.selectbox("Room Type", list(room_prices.keys()))

# Show selected room price
st.markdown(f"💰 Price per day for {room_type} room: ₹{room_prices[room_type]}")

days = st.number_input("How many days?", min_value=1, step=1)
booking_date = datetime.now().strftime("%Y-%m-%d")

# Calculate total cost
cost_per_day = room_prices[room_type]
total_cost = days * cost_per_day

# Booking action
if st.button("Book Now"):
    if name.strip() == "":
        st.warning("Please enter your name to proceed.")
    else:
        booking_data = {
            "BookingID": f"RB{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "Name": name,
            "RoomType": room_type,
            "Days": days,
            "MealIncluded": "No",
            "AirportPickup": "No",
            "TotalCost": total_cost,
            "BookingDate": booking_date
        }

        # Save to bookings.csv
        file_path = "data/bookings.csv"
        df = pd.DataFrame([booking_data])
        if os.path.exists(file_path):
            df.to_csv(file_path, mode='a', header=False, index=False)
        else:
            df.to_csv(file_path, index=False)

        st.success(f"✅ {name}, your {room_type} room has been booked for ₹{total_cost}")
        st.info(f"📅 Booking ID: {booking_data['BookingID']}")
