import random

from meeting_session import render_meeting_session
import streamlit as st


async def render_gui():

    with st.expander("Neues Meeting organsieren"):
        if 'organise_meeting_clicked' not in st.session_state:
            st.session_state.organise_meeting_clicked = False
        if 'participation_pin' not in st.session_state:
            st.session_state.participation_pin = random.randint(100000,999999)  # Generiere eine Zufallszahl zwischen 100000 und 999999

        def submit_meeting():
            st.session_state.organise_meeting_clicked = True

        with st.form("organisation_form", border=False):

            remote_meeting_id = st.text_input(
                key="Besprechungs-ID-Organisation",
                label="Besprechungs-Id*",
                help="Besprechungs-ID deines Remote-Meetings",
            )

            organise_meeting_clicked = st.form_submit_button("Meeting erstellen", on_click=submit_meeting, disabled=st.session_state.organise_meeting_clicked)

            if organise_meeting_clicked:
                with st.container(border=True):
                    st.write("Besprechungs-Id: " + remote_meeting_id)
                    st.write("Teilnahme-Pin: " + str(st.session_state.participation_pin))
                    st.write("Zugangslink: https://somepath/" + remote_meeting_id + "/" + str(st.session_state.participation_pin))


    with (st.expander("Meeting beitreten")):
        def submit_participation_request():
            st.session_state.participation_request_clicked = True

        with st.form("participation_form", border=False):
            col1, col2 = st.columns(2)

            with col1:
               remote_meeting_id = st.text_input(
                   key="Besprechungs-ID-Teilnahme",
                   label="Besprechungs-ID*",
                   help="Besprechungs-ID deines Remote-Meetings",
                   value=remote_meeting_id
               )

            with col2:
               participation_pin = st.text_input(
                    key="Teilnahme-Pin-Teilnahme",
                    label="Teilnahme-Pin*",
                    help="Teilnehmer, welche diesen Pin kennen können dem RoboNote-Meeting beitreten",
               )

            tab_participate, tab_reparticipate= st.tabs(
                ["Erstbeitritt", "Wiedereintritt"])

            with tab_participate:
                name = st.text_input(
                    "Name*",
                )

            with tab_reparticipate:
                collaborator_id = st.text_input(
                    key="Mitwirkungs-ID",
                    label="Mitwirkungs-ID*",
                    help="Teilnehmer, welche diesen Pin kennen können dem RoboNote-Meeting beitreten",
                )

            participate_meeting_clicked = st.form_submit_button("Meeting beitreten", on_click=submit_participation_request)

        if participate_meeting_clicked:
            if 'personal_pin' not in st.session_state:
                if collaborator_id:
                    st.session_state.collaborator_id = collaborator_id
                else:
                    st.session_state.collaborator_id = random.randint(100000, 999999)  # Generiere eine Zufallszahl zwischen 100000 und 999999
            with st.container(border=True):
                st.write("Besprechungs-Id: " + remote_meeting_id)
                st.write("Teilnahme-Pin: " + str(participation_pin))
                st.write("Mitwirkungs-ID: " + str(st.session_state.collaborator_id))
                st.write("Zugangslink: https://somepath/" + remote_meeting_id + "/" + str(participation_pin) + "/" + str(st.session_state.collaborator_id))


    await render_meeting_session()