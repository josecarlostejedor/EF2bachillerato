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
    """, unsafe_allow_value=True)

st.title("🏃‍♂️ Análisis del II Encuentro Político: Educación Física en CyL")
st.write("Propuestas sobre la materia de EF en los centros educativos y su inclusión en 2º de Bachillerato.")

# Vídeo principal
st.video("https://www.youtube.com/watch?v=-KQeQzYw_xw")

st.divider()

# --- BLOQUE PSOE ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b8/Logotipo_del_PSOE.svg", width=100)
    st.subheader("PSOE")
    st.caption("Iñaki Gómez")
with col2:
    st.markdown(f"""
    <div class="psoe-card">
        <h4>Postura sobre 2º de Bachillerato</h4>
        <p>"Ahora mismo ya se aprobaron las cortes... eso fue una iniciativa del grupo socialista en junio del 2025... ahora hay que estar a la Junta para que se implemente." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=2050" target="_blank">⏱️ 34:10</a></p>
        <h4>Educación Física Escolar</h4>
        <p>"El Partido Socialista quiere que haya más educación física en las aulas... sería bueno una tercera hora en secundaria y 1º de bachillerato." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=2081" target="_blank">⏱️ 34:41</a></p>
    </div>
    """, unsafe_allow_html=True)

# --- BLOQUE PP ---
col3, col4 = st.columns([1, 4])
with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/de/Logo_del_Partido_Popular_%282019%29.svg", width=100)
    st.subheader("PP")
    st.caption("Borja del Barrio")
with col4:
    st.markdown(f"""
    <div class="pp-card">
        <h4>Postura sobre 2º de Bachillerato</h4>
        <p>"Ese año es un año complicado (Selectividad)... aunque solo sea por tener un momento de poder hacer deporte... el fomentarlo en el programa curricular es importante." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1962" target="_blank">⏱️ 32:42</a></p>
        <h4>Enfoque Educativo</h4>
        <p>"Nos preocupa impulsar un programa de fomento del deporte que tiene que nacer de esas escuelas." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1860" target="_blank">⏱️ 31:00</a></p>
    </div>
    """, unsafe_allow_html=True)

# --- BLOQUE VOX ---
col5, col6 = st.columns([1, 4])
with col5:
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/df/Vox_logo.svg", width=100)
    st.subheader("VOX")
    st.caption("Enrique Jiménez")
with col6:
    st.markdown(f"""
    <div class="vox-card">
        <h4>Postura sobre 2º de Bachillerato</h4>
        <p>"Agradecemos al COLEF el trabajo en el desarrollo curricular de las optativas... de actividad física y salud en segundo de bachillerato dándole un componente importante." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1313" target="_blank">⏱️ 21:53</a></p>
        <h4>Calidad Docente</h4>
        <p>"Apostaremos por más horas, más calidad y más especialización... profesionalización y no al intrusismo profesional." 
        <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1740" target="_blank">⏱️ 29:00</a></p>
    </div>
    """, unsafe_allow_html=True)

st.sidebar.info("Esta herramienta facilita la comparación de propuestas políticas para el sector de la Educación Física.")