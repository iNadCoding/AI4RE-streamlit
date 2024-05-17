import streamlit as st
import requests

from tab_collaborative import render_tab_collaborative
from tab_harmonised import render_tab_harmonised
from tab_personal import render_tab_personal

st.title("KI4RE - REMOTE WORKSHOPS")


# Beispielbutton -----------------------------------------
tab_personal, tab_collaborative, tab_harmonised = st.tabs(["Persönlich", "Kollaborativ", "KI-Harmonisiert"])

with tab_personal:
   render_tab_personal()

with tab_collaborative:
   render_tab_collaborative()

with tab_harmonised:
   render_tab_harmonised()

