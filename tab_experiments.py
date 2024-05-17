import streamlit as st
import random
import time

def render_tab_experiments():
    st.header("Eure gemeinsamen Notizen")


    # CUSTOM BUTTON
    st.markdown(
        """
        <style>
        .stButton > button {
            background-color: green;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button('Styled Button'):
        st.write("Button clicked!")



    # ---------------------------------------------------------------------------------------------------------
    st.title("Echo Bot")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Streamed response emulator
    def response_generator():
        response = random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
        for word in response.split():
            yield word + " "
            time.sleep(0.05)

    st.title("Simple chat")

    # Accept user input
    if prompt := st.chat_input("What is up?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator())
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
    # ---------------------------------------------------------------------------------------------------------
