import streamlit as st

def render_tab_collaborative():
    st.header("Eure gemeinsamen Notizen")

    # Initialize session state variables if not already set
    if 'edit_mode' not in st.session_state:
        st.session_state.edit_mode = False
    if 'text' not in st.session_state:
        st.session_state.text = "Dies ist der ursprüngliche Text."

    # Function to toggle edit mode
    def toggle_edit_mode():
        st.session_state.edit_mode = not st.session_state.edit_mode

    # Function to submit the edited text
    def submit_text():
        st.session_state.text = st.session_state.new_text
        st.session_state.edit_mode = False

    if st.session_state.edit_mode:
        st.session_state.new_text = st.text_area("Bearbeite den Text", st.session_state.text)
        st.button("Absenden", on_click=submit_text)
    else:
        st.markdown(st.session_state.text)
        st.button("Bearbeiten", on_click=toggle_edit_mode)
