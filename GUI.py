import asyncio
import random

from Services.websocket import listen_to_websocket
from usecases.meeting_session import render_meeting_session
import streamlit as st


async def render_gui():
    st.title("KI4RE - RoboNote")

    if st.button("Verbinden"):
        await asyncio.create_task(listen_to_websocket())

    #await check_into_meeting()
    await render_meeting_session()

