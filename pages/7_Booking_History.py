import streamlit as st
import pandas as pd
import os

st.title("📖 Booking History")

file_path = "data/bookings.csv"

# Check if bookings.csv exists
if not os.path.exists(file_path):
    st.info("No booking history found yet.")
else:
    try:
        df = pd.read_csv(file_path)

        if df.empty:
            st.warning("Booking history is currently empty.")
        else:
            # Sort by BookingDate and show recent first
            if "BookingDate" in df.columns:
                df["BookingDate"] = pd.to_datetime(df["BookingDate"], errors='coerce')
                df = df.sort_values(by="BookingDate", ascending=False)

            # Show recent bookings
            st.success(f"Total bookings: {len(df)}")
            st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error(f"Error reading booking history: {e}")
