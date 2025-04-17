import streamlit as st
from datetime import date

st.title("📅 Book an Appointment")

# Let the user select a pet from a dropdown
pet = st.selectbox("Select your pet", ["Buddy", "Milo", "Nala"])

# Let the user select a type of service
service = st.radio("Select service type", ["Vet Checkup", "Grooming"])

# Let the user pick a date for the appointment
appointment_date = st.date_input("Choose a date", date.today())

# When the user clicks submit, show confirmation
if st.button("Submit Appointment"):
    st.success(f"Appointment booked for {pet} - {service} on {appointment_date}")