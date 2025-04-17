import streamlit as st
import pandas as pd

st.title("🐾 Pet Overview")

# Sample data for demonstration
pets_data = [
    {"Name": "Buddy", "Species": "Dog", "Age": 3, "Last Check-up": "2025-03-10"},
    {"Name": "Milo", "Species": "Cat", "Age": 2, "Last Check-up": "2025-01-20"},
]

# Display the pet data in a table
df = pd.DataFrame(pets_data)
st.dataframe(df)

# Informational message for users
st.info("Click on a pet to view more details (feature coming soon!)")
