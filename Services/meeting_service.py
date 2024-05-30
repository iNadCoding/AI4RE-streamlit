# frontend.py
import streamlit as st
import requests
import logging

url_prefix = "http://localhost:8000/"
backend_url = url_prefix + "meetings"


async def get_meetings():
    response = requests.get(f"{backend_url}/")
    if response.status_code == 200:
        logging.warning("get_meetings: successfull")
        return response.json()
    else:
        logging.warning("get_meetings: failed")
        st.error("Failed to retrieve meetings")
        return {}


async def get_meeting(meeting_id):
    response = requests.get(f"{backend_url}/{meeting_id}")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Meeting not found")
        return None
