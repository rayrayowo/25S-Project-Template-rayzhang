# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Persona: Alex (New Pet Owner) ------------------------
def AlexNav():
    st.sidebar.page_link("pages/10_Alex_Home.py", label="Alex's Dashboard", icon="🐶")
    st.sidebar.page_link("pages/11_Reminder_Setup.py", label="Set Daily Reminders", icon="⏰")
    st.sidebar.page_link("pages/12_Beginner_Guide.py", label="Pet Care Guide", icon="📘")
    st.sidebar.page_link("pages/13_Health_Input.py", label="Log Pet Health", icon="💊")
    st.sidebar.page_link("pages/14_Clinic_Finder.py", label="Find Vet & Grooming", icon="🏥")

#### ------------------------ Persona: Emily (Pet Blogger) ------------------------
def EmilyNav():
    st.sidebar.page_link("pages/20_Emily_Home.py", label="Emily's Dashboard", icon="🐱")
    st.sidebar.page_link("pages/21_Health_Tracker.py", label="Health Tracker", icon="📈")
    st.sidebar.page_link("pages/22_Community_Board.py", label="Community Board", icon="🗣️")
    st.sidebar.page_link("pages/23_Custom_Reminders.py", label="Custom Reminders", icon="📝")
    st.sidebar.page_link("pages/24_Events.py", label="Pet Events", icon="🎪")

#### ------------------------ Persona: Michael (Vet) ------------------------
def VetNav():
    st.sidebar.page_link("pages/30_Vet_Home.py", label="Vet Dashboard", icon="🩺")
    st.sidebar.page_link("pages/31_View_Records.py", label="View Pet Records", icon="📄")
    st.sidebar.page_link("pages/32_Reminder_Mgmt.py", label="Send Reminders", icon="📨")
    st.sidebar.page_link("pages/33_EMR_Entry.py", label="Log Medical Records", icon="📝")
    st.sidebar.page_link("pages/34_Consultations.py", label="Online Consults", icon="💬")

#### ------------------------ Persona: Sophia (Grooming Owner) ------------------------
def SophiaNav():
    st.sidebar.page_link("pages/40_Grooming_Owner_Home.py", label="Sophia's Dashboard", icon="💇‍♀️")
    st.sidebar.page_link("pages/41_View_Appointments.py", label="Grooming Appointments", icon="📅")
    st.sidebar.page_link("pages/42_Health_Status.py", label="Check Pet Health", icon="🩺")
    st.sidebar.page_link("pages/43_Grooming_Recommendations.py", label="Grooming Advice", icon="🧴")
    st.sidebar.page_link("pages/46_Clinic_Collaborations.py", label="Vet Collaborations", icon="🔗")


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    st.sidebar.image("assets/logo.png", width=150)

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        HomeNav()

    if st.session_state["authenticated"]:
        role = st.session_state.get("role")

        if role == "new_pet_owner":
            AlexNav()
        elif role == "pet_blogger":
            EmilyNav()
        elif role == "veterinarian":
            VetNav()
        elif role == "grooming_owner":
            SophiaNav()

    AboutPageNav()

    if st.session_state.get("authenticated"):
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")