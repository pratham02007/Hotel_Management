import streamlit as st
import pandas as pd
from datetime import datetime
import os



st.title("⚡ Fast Booking")

# Input fields
name = st.text_input("Enter your full name")
days = st.selectbox("Select number of days", options=list(range(1, 16)))
room_type = st.selectbox("Room Type", ["Single", "Double", "Deluxe"])
# room_type = "Standard"
cost_per_day = 2000
st.write(f"The one day Price , {cost_per_day}")
total_cost = cost_per_day * days
booking_date = datetime.now().strftime("%Y-%m-%d")

# Booking action
if st.button("Book Now"):
    if name.strip() == "":
        st.warning("Please enter your name to proceed.")
    else:
        # Booking record
        booking_data = {
            "BookingID": f"FB{datetime.now().strftime('%Y%m%d%H%M%S')}",
            "Name": name,
            "RoomType": room_type,
            "Days": days,
            "MealIncluded": "No",
            "AirportPickup": "No",
            "TotalCost": total_cost,
            "BookingDate": booking_date
        }

        # Save to CSV
        file_path = "data/bookings.csv"
        df = pd.DataFrame([booking_data])
        if os.path.exists(file_path):
            df.to_csv(file_path, mode='a', header=False, index=False)
        else:
            df.to_csv(file_path, index=False)
            
        

        # Confirmation
        st.success(f"✅ {name}, your {room_type} room has been booked for ₹{total_cost} for {days} day(s)!")
        st.info(f"📅 Booking ID: {booking_data['BookingID']}")

