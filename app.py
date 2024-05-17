import streamlit as st
import requests
import asyncio

from tab_collaborative import render_tab_collaborative
from tab_experiments import render_tab_experiments
from tab_harmonised import render_tab_harmonised
from tab_personal import render_tab_personal

st.title("KI4RE - REMOTE WORKSHOPS")

tab_personal, tab_collaborative, tab_harmonised, tab_experiments = st.tabs(
   ["Persönlich", "Kollaborativ", "KI-Harmonisiert", "Experimente"])

with tab_personal:
   render_tab_personal()

with tab_collaborative:
   render_tab_collaborative()

with tab_harmonised:
   render_tab_harmonised()

with tab_experiments:
   render_tab_experiments()