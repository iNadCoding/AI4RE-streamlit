import aiohttp
import asyncio
import streamlit as st

from aioresponses import aioresponses




# Testfunktion zum Mocken der Antwort
async def simulate_fetch_data():

    # Simulation von Warten auf Daten
    await asyncio.sleep(2)

    return [
        ["Geladene Eigene Notizen", "Notizenbeispiel"],
        ["Geladene Gemeinsame Notizen", "Notizenbeispiel"],
        ["KI-Aufbereitetes", "Notizenbeispiel"],
    ]