import streamlit as st
import asyncio

from GUI import render_gui


async def main():
    st.title("KI4RE - RoboNote")
    await render_gui()

if __name__ == "__main__":
    asyncio.run(main())