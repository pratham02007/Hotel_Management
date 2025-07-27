import pandas as pd
import os
from datetime import datetime

BOOKINGS_FILE = "data/bookings.csv"

def load_bookings():
    """Load all bookings from CSV. Returns empty DataFrame if file not found."""
    if os.path.exists(BOOKINGS_FILE):
        return pd.read_csv(BOOKINGS_FILE)
    else:
        return pd.DataFrame(columns=[
            "BookingID", "Name", "RoomType", "Days",
            "MealIncluded", "AirportPickup", "TotalCost", "BookingDate"
        ])

def save_booking(booking_data: dict):
    """Append a new booking to the CSV file."""
    df = pd.DataFrame([booking_data])
    if os.path.exists(BOOKINGS_FILE):
        df.to_csv(BOOKINGS_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(BOOKINGS_FILE, index=False)

def generate_booking_id(prefix="BK"):
    """Generate a unique booking ID using timestamp."""
    return f"{prefix}{datetime.now().strftime('%Y%m%d%H%M%S')}"
