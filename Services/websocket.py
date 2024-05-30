import asyncio
import websockets
import json
import streamlit as st

import streamlit as st
import asyncio
import websockets
from websockets import InvalidStatusCode, ConnectionClosedError
import logging

logging.basicConfig(level=logging.INFO)
async def listen_to_websocket():
    uri = "ws://localhost:8000"

    logging.info(f"Streamlit-App läuft auf Port: {st.config.get_option('server.port')}")
    try:
        async with websockets.connect(uri) as websocket:
            while True:
                message = await websocket.recv()
                st.write(f"Nachricht vom Server: {message}")
    except websockets.exceptions.InvalidStatusCode as e:
        if e.status_code == 403:
            st.error("Verbindung abgelehnt: Fehlercode 403")
        else:
            st.error(f"Verbindung abgelehnt: Fehlercode {e.status_code}")
    except websockets.exceptions.ConnectionClosedError as e:
        st.error(f"Verbindung geschlossen: {str(e)}")
    except Exception as e:
        st.error(f"Ein Fehler ist aufgetreten: {str(e)}")

st.title("Websocket Client")
st.write("Verbinde zu Websocket Server...")
