import random

import streamlit as st

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
