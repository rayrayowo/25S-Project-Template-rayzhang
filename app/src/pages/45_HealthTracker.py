import streamlit as st
import requests

st.title("📊 Health Tracker")
st.write("Monitor pet health data like weight, diet, and main meals.")

# Fetch health records
try:
    response = requests.get("http://localhost:3111/health-records")
    if response.status_code == 200:
        data = response.json()
        st.dataframe(data)
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
except Exception as e:
    st.error(f"Error fetching data: {e}")

# Add Main Meals Section (主食)
st.subheader("Main Meals (主食)")
meal_name = st.text_input("Enter the meal name")
meal_description = st.text_area("Enter a brief description of the meal")

if st.button("Add Main Meal"):
    if meal_name and meal_description:
        st.success(f"Meal '{meal_name}' added successfully!")
        st.write(f"**Meal Name:** {meal_name}")
        st.write(f"**Description:** {meal_description}")
    else:
        st.warning("Please provide both a meal name and description.")

