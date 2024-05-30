import aiohttp
import asyncio
import streamlit as st

from aioresponses import aioresponses

from utils import st_cache_tests

# Testfunktion zum Mocken der Antwort
async def simulate_fetch_data():
    st_cache_tests("simulate_fetch_data")
    # Simulation von Warten auf Daten
    # await asyncio.sleep(2)

    return [
        ["Geladene Eigene Notizen", "Notizenbeispiel"],  #Persönliche Notizen
        ["Geladene Gemeinsame Notizen", "Notizenbeispiel"],  #Kollaborative Notizen
        ["KI-Aufbereitetes", "Notizenbeispiel"], #Ki-Harmonisierte Notizen
    ]


