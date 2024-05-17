from meeting_session.data_loader import simulate_fetch_data
from meeting_session.tab_collaborative import render_tab_collaborative
from meeting_session.tab_experiments import render_tab_experiments
from meeting_session.tab_harmonised import render_tab_harmonised
from meeting_session.tab_personal import render_tab_personal
import streamlit as st


async def render_meeting_session():

    if 'personal_prompts' not in st.session_state:
        st.session_state.personal_prompts = []

        data = await simulate_fetch_data()
        st.session_state.personal_prompts = data[0]

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