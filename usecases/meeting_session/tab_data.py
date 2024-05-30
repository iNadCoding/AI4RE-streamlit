import streamlit as st

from Services.meeting_service import get_meetings
from components.st_chat_card import st_chat_card
from utils import st_cache_tests

#https://docs.streamlit.io/develop/concepts/architecture/fragments
#Fragment bewirkt, dass nicht immer die ganze Seite neu geladen wird
@st.experimental_fragment
async def render_tab_data():
    if 'meetings' not in st.session_state:
        st.session_state.meetings = await get_meetings()

        # Alle Benutzereingaben anzeigen
        for p in st.session_state.meetings:
            st.write(f'{p}')

        #with st.chat_message("Nadja"):
        #    st.write(f'{p}')