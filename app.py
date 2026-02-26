import streamlit as st

# 1. Configuración de la página (DEBE SER LA PRIMERA LÍNEA DE STREAMLIT)
st.set_page_config(page_title="Debate EF Castilla y León 2026", layout="wide")

# 2. Estilos CSS corregidos
st.markdown("""
    <style>
    .psoe-card { border-left: 10px solid #EF3B2C; padding: 15px; background-color: #f1f1f1; border-radius: 8px; margin-bottom: 20px; color: black; }
    .pp-card { border-left: 10px solid #0054A6; padding: 15px; background-color: #f1f1f1; border-radius: 8px; margin-bottom: 20px; color: black; }
    .vox-card { border-left: 10px solid #63BE21; padding: 15px; background-color: #f1f1f1; border-radius: 8px; margin-bottom: 20px; color: black; }
    .time-link { color: #ffffff !important; font-weight: bold; text-decoration: none; background: #333; padding: 4px 8px; border-radius: 4px; font-size: 0.8em; }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado
st.title("🏃‍♂️ Análisis: Educación Física en Castilla y León")
st.write("Propuestas políticas sobre EF Escolar y 2º de Bachillerato.")

# 4. Vídeo
st.video("https://www.youtube.com/watch?v=-KQeQzYw_xw")

st.divider()

# --- BLOQUE PSOE ---
with st.container():
    c1, c2 = st.columns([1, 4])
    c1.image("https://upload.wikimedia.org/wikipedia/commons/b/b8/Logotipo_del_PSOE.svg", width=120)
    c1.subheader("PSOE")
    c2.markdown(f"""
    <div class="psoe-card">
        <strong>Postura sobre 2º de Bachillerato:</strong><br>
        "Fue una iniciativa del grupo socialista en junio del 2025... ahora hay que estar a la Junta para que se implemente." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=2050" target="_blank">Minuto 34:10</a><br><br>
        <strong>Educación Física Escolar:</strong><br>
        "Sería bueno una tercera hora en secundaria y 1º de bachillerato." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=2081" target="_blank">Minuto 34:41</a>
    </div>
    """, unsafe_allow_html=True)

# --- BLOQUE PP ---
with st.container():
    c1, c2 = st.columns([1, 4])
    c1.image("https://upload.wikimedia.org/wikipedia/commons/d/de/Logo_del_Partido_Popular_%282019%29.svg", width=120)
    c1.subheader("PP")
    c2.markdown(f"""
    <div class="pp-card">
        <strong>Postura sobre 2º de Bachillerato:</strong><br>
        "Es un año de apretar... aunque solo sea por tener un momento de poder hacer deporte... fomentarlo en el programa curricular es importante." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1962" target="_blank">Minuto 32:42</a><br><br>
        <strong>Enfoque Educativo:</strong><br>
        "Nos preocupa impulsar un programa de fomento del deporte que tiene que nacer de esas escuelas." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1860" target="_blank">Minuto 31:00</a>
    </div>
    """, unsafe_allow_html=True)

# --- BLOQUE VOX ---
with st.container():
    c1, c2 = st.columns([1, 4])
    c1.image("https://upload.wikimedia.org/wikipedia/commons/d/df/Vox_logo.svg", width=120)
    c1.subheader("VOX")
    c2.markdown(f"""
    <div class="vox-card">
        <strong>Postura sobre 2º de Bachillerato:</strong><br>
        "Damos un componente curricular importante a la optativa de actividad física y salud en segundo de bachillerato." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1313" target="_blank">Minuto 21:53</a><br><br>
        <strong>Calidad Docente:</strong><br>
        "Apostaremos por más horas y más especialización... profesionalización y no al intrusismo profesional." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1740" target="_blank">Minuto 29:00</a>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.success("App cargada correctamente.")