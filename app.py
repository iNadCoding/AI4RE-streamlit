import streamlit as st
import requests

st.title("KI4RE - REMOTE WORKSHOPS")


# Beispielbutton -----------------------------------------
tab1, tab2, tab3 = st.tabs(["Persönlich", "Kollaborativ", "Zusammengeführt"])

with tab1:
   st.header("Deine persönlichen Notizen")

   if 'submissions' not in st.session_state:
      st.session_state.submissions = []

   if 'area_input' not in st.session_state:
      st.session_state.area_input = ''

   def submit():
      st.session_state.submissions.append(st.session_state.input)
      st.session_state.input = ''

   for submission in st.session_state.submissions:
      st.write(f'{submission}')

   st.text_area('Notizen hinzufügen', key='input', on_change=submit)

with tab2:
   st.header("Eure gemeinsamen Notizen")

with tab3:
   st.header("Eure harmonisierten Notizen")

