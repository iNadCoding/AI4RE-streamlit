import streamlit as st
import asyncio
from GUI import render_gui


async def main():
    await render_gui()

if __name__ == "__main__":
    asyncio.run(main())