import streamlit as st
import requests

st.title("💊 Medication List")
st.write("List of medications with description.")

# Fetch medication data
try:
    response = requests.get("http://localhost:3111/medications")
    if response.status_code == 200:
        data = response.json()
        st.dataframe(data)
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
except Exception as e:
    st.error(f"Error fetching data: {e}")

# Add Medication Section (药物)
st.subheader("Add Medication (药物)")
medication_name = st.text_input("Enter medication name")
medication_description = st.text_area("Enter a brief description of the medication")

if st.button("Add Medication"):
    if medication_name and medication_description:
        st.success(f"Medication '{medication_name}'_

