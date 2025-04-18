import streamlit as st
import requests

st.title("📋 Prescription Log")
st.write("Prescription records for checkups.")

try:
    response = requests.get("http://localhost:3111/prescriptions")
    if response.status_code == 200:
        data = response.json()
        st.dataframe(data)
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
except Exception as e:
    st.error(f"Error fetching data: {e}")
