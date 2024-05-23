import streamlit as st

from utils import st_cache_tests


def render_tab_personal():
    st.header("Deine persönlichen Notizen")
    st_cache_tests("render_tab_personal")
    #Streamlit-Chatbot-Tutorial: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps


    # Alle Benutzereingaben anzeigen
    for p in st.session_state.personal_prompts:
        st.write(f'{p}')

        #with st.chat_message("Nadja"):
        #    st.write(f'{p}')

    # Chat-Box anzeigen
    prompt = st.chat_input("Notizen hinzufügen")

    # Neue Eingabe zum Array hinzufügen
    if prompt:
        st.session_state.personal_prompts.append(prompt)