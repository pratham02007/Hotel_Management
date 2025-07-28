import streamlit as st

st.title("🔐 Admin Panel")

st.warning("Restricted Access")
password = st.text_input("Enter admin password", type="password")

if password == "admin123":
    st.success("Access granted")
    st.write("🧾 All Bookings | 💸 Payments | 📈 Analytics coming soon...")
else:
    st.error("Incorrect password")
