import streamlit as st

st.title("💬 Customer Feedback")

name = st.text_input("Name")
rating = st.slider("Rate us", 1, 5, 4)
comments = st.text_area("Your feedback")

if st.button("Submit"):
    st.success("Thank you for your feedback!")
