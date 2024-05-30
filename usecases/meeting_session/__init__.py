import asyncio

from Services.data_loader import simulate_fetch_data
from usecases.meeting_session.tab_collaborative import render_tab_collaborative
from usecases.meeting_session.tab_data import render_tab_data
from usecases.meeting_session.tab_experiments import render_tab_experiments
from usecases.meeting_session.tab_harmonised import render_tab_harmonised
from usecases.meeting_session.tab_personal import render_tab_personal
import streamlit as st


async def render_meeting_session():

    if 'personal_prompts' not in st.session_state:
        st.session_state.personal_prompts = []

        data = await simulate_fetch_data()
        st.session_state.personal_prompts = data[0]
        st.session_state.collaborative_prompts = data[1]
        st.session_state.harmonised_prompts = data[2]

    tab_personal, tab_collaborative, tab_harmonised, tab_experiments, tab_data = st.tabs(
        ["Persönlich", "Kollaborativ", "KI-Harmonisiert", "Experimente", "Daten"])

    with tab_personal:
        render_tab_personal()

    with tab_collaborative:
        render_tab_collaborative()

    with tab_harmonised:
        render_tab_harmonised()

    with tab_experiments:
        render_tab_experiments()

    with tab_data:
        await render_tab_data()