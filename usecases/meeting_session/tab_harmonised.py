import random

import streamlit as st

from components.st_chat_card import st_chat_card


#https://docs.streamlit.io/develop/concepts/architecture/fragments
#Fragment bewirkt, dass nicht immer die ganze Seite neu geladen wird
@st.experimental_fragment
def render_tab_harmonised():
    st.header("Eure harmonisierten Notizen")
    st.session_state.changed = False

    # Alle Benutzereingaben anzeigen
    for idx, p in enumerate(st.session_state.harmonised_prompts):
        with st.expander(label=f'{idx}.) {p}'):
            key = "Schnippsel_" + str(random.randint(100000, 999999))

            edited = st.text_area(label=key, value=p, key=key)
            if edited:
                if st.session_state.harmonised_prompts[idx] != edited:
                    st.session_state.changed = True

                st.session_state.harmonised_prompts[idx] = edited
                st.warning(f'{edited}', icon="⚠️")

                if (st.session_state.changed):
                    edited.value = edited
                    st.rerun()

    for idx, p in enumerate(st.session_state.harmonised_prompts):
        key = "Schnippsel_" + str(random.randint(100000, 999999))

        edited = st_chat_card(label=key, value=p, key=key)
        if edited:
            if st.session_state.harmonised_prompts[idx] != edited:
                st.session_state.changed = True

                st.session_state.harmonised_prompts.append(edited)

            if (st.session_state.changed):
                edited.value = edited
                st.rerun()
