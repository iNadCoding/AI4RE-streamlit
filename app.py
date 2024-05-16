import streamlit as st
import requests

st.title("KI4RE - REMOTE WORKSHOPS")


# Beispielbutton -----------------------------------------
user_input = st.text_input("Geben Sie Ihren Text ein:")
button_clicked = st.button("Absenden")

if button_clicked:
    # API-Aufruf hier einfügen
    st.write("Verarbeitung...")

# Beispielbutton -----------------------------------------
