import streamlit as st

def render_tab_personal():
    st.header("Deine persönlichen Notizen")

    #Streamlit-Chatbot-Tutorial: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps

    # Speichern der Benutzereingaben
    if 'prompts' not in st.session_state:
        st.session_state.prompts = ["Alte Notizen", "Diese müssen zuerst noch richtig geladen werden"]

    # Alle Benutzereingaben anzeigen
    for p in st.session_state.prompts:
        st.write(f'{p}')

        #with st.chat_message("Nadja"):
        #    st.write(f'{p}')

    # Chat-Box anzeigen
    prompt = st.chat_input("Notizen hinzufügen")

    # Neue Eingabe zum Array hinzufügen
    if prompt:
        st.session_state.prompts.append(prompt)
        st.experimental_rerun()  #Page neu laden, um die Liste upzudaten
