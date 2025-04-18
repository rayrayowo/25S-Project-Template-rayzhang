import streamlit as st
import requests

st.title("📅 Book Appointment")
st.write("Book a new appointment for a pet.")

try:
    response = requests.get("http://localhost:3111/appointments")
    if response.status_code == 200:
        data = response.json()
        st.dataframe(data)
    else:
        st.error(f"Failed to fetch data: {response.status_code}")
except Exception as e:
    st.error(f"Error fetching data: {e}")


st.write("### Create New Appointment")
with st.form("appointment_form"):
    pet_id = st.number_input("Pet ID", min_value=1)
    appointment_date = st.date_input("Date")
    appointment_time = st.time_input("Time")
    appointment_type = st.text_input("Type (e.g., Grooming, Vet Checkup)")
    status = st.selectbox("Status", ["Scheduled", "Completed", "Cancelled"])
    submitted = st.form_submit_button("Book Appointment")

    if submitted:
        payload = {
            "pet_id": pet_id,
            "appointment_date": str(appointment_date),
            "appointment_time": str(appointment_time),
            "appointment_type": appointment_type,
            "status": status
        }
        post_resp = requests.post("http://localhost:3111/appointments", json=payload)
        if post_resp.status_code == 201:
            st.success("Appointment created successfully!")
        else:
            st.error("Failed to create appointment.")
