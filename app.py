import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Debate EF Castilla y León 2026", layout="wide")

# Estilos personalizados para las tarjetas
st.markdown("""
    <style>
    .psoe-card { border-left: 10px solid #EF3B2C; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-bottom: 20px; }
    .pp-card { border-left: 10px solid #0054A6; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-bottom: 20px; }
    .vox-card { border-left: 10px solid #63BE21; padding: 20px; background-color: #f9f9f9; border-radius: 10px; margin-bottom: 20px; }
    .time-link { color: #555; font-weight: bold; text-decoration: none; background: #eee; padding: 2px 5px; border-radius: 4px; }
    </style>
    """, unsafe_allow_html=True) # <-- Aquí estaba el error, ahora está corregido