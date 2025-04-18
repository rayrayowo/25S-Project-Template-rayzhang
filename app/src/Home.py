##################################################
# This is the main/entry-point file for the 
# PetHub application
##################################################

# Set up basic logging infrastructure
import logging
logging.basicConfig(format='%(filename)s:%(lineno)s:%(levelname)s -- %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# import the main streamlit library as well
# as SideBarLinks function from src/modules folder
import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Reset authentication status
st.session_state['authenticated'] = False
SideBarLinks(show_home=True)

logger.info("Loading the Home page of the PetHub app")
st.title('🐾 Welcome to PetHub')
st.write('\n\n')
st.write('### Who are you today? Choose your role to begin.')

# Persona 1: Alex Chen - New Pet Owner
if st.button("🐶 Log in as Alex, a New Pet Owner", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'new_pet_owner'
    st.session_state['first_name'] = 'Alex'
    logger.info("Logging in as New Pet Owner")
    st.switch_page('pages/10_Alex_Home.py')

# Persona 2: Emily Wong - Experienced Pet Enthusiast
if st.button("🐱 Log in as Emily, a Pet Blogger", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'pet_blogger'
    st.session_state['first_name'] = 'Emily'
    logger.info("Logging in as Experienced Pet Owner")
    st.switch_page('pages/20_Emily_Home.py')

# Persona 3: Michael Davis - Veterinarian
if st.button("🩺 Log in as Dr. Michael, a Veterinarian", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'veterinarian'
    st.session_state['first_name'] = 'Michael'
    logger.info("Logging in as Veterinarian")
    st.switch_page('pages/30_Vet_Home.py')

# Persona 4: Sophia Miller - Grooming Salon Owner
if st.button("💇‍♂️ Log in as Sophia, a Grooming Salon Owner", type='primary', use_container_width=True):
    st.session_state['authenticated'] = True
    st.session_state['role'] = 'grooming_owner'
    st.session_state['first_name'] = 'Sophia'
    logger.info("Logging in as Grooming Salon Owner")
    st.switch_page('pages/40_Grooming_Owner_Home.py')



