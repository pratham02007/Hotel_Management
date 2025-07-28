import streamlit as st
from PIL import Image

st.set_page_config(page_title="Hotel Management", layout="wide")
st.title("🏨 Hotel Management System")
st.write("Welcome! Please select a page from the sidebar.")

img = Image.open("images/room.png")

img_hd = img.resize((img.width * 2, img.height * 2), Image.LANCZOS)

img_hd.save("images/room_hd.png")
st.image("images/room_hd.png", caption="Relax in comfort at our luxury suite", width=250)

