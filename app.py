import streamlit as st
import asyncio

from GUI import render_gui
from data_loader import simulate_fetch_data


async def main():
    st.title("KI4RE - REMOTE WORKSHOPS")

    if 'personal_prompts' not in st.session_state:
        st.session_state.personal_prompts = []

        data = await simulate_fetch_data()
        st.session_state.personal_prompts = data[0]

    render_gui()

if __name__ == "__main__":
    asyncio.run(main())