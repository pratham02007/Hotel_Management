import streamlit as st

st.title("💳 Payment & Invoice")

booking_id = st.text_input("Booking ID")
amount = st.number_input("Amount to Pay", min_value=0)

if st.button("Pay Now"):
    st.success(f"Payment of ₹{amount} successful for Booking ID: {booking_id}")
