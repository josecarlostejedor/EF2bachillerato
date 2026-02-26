import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Análisis Educación Física CyL", layout="wide")

# 2. Estilos CSS Avanzados para tarjetas y lectura
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    html, body, [class*="st-"] { font-family: 'Inter', sans-serif; }

    .main-card { padding: 30px; border-radius: 15px; margin-bottom: 30px; line-height: 1.6; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .psoe-box { border-left: 10px solid #EF3B2C; background-color: #fdf2f2; border: 1px solid #f5dada; border-left-width: 10px; }
    .pp-box { border-left: 10px solid #0054A6; background-color: #f2f7fd; border: 1px solid #dce8f7; border-left-width: 10px; }
    .vox-box { border-left: 10px solid #63BE21; background-color: #f4faf0; border: 1px solid #e2f0d9; border-left-width: 10px; }
    
    .quote-text { font-style: italic; color: #222; background: rgba(255,255,255,0.7); padding: 15px; border-radius: 8px; display: block; margin: 10px 0; border: 1px dashed #ccc; }
    .section-title { font-weight: bold; color: #444; text-transform: uppercase; font-size: 0.85em; margin-top: 20px; display: block; letter-spacing: 0.5px; }
    
    .time-link { 
        display: inline-block; 
        background-color: #000; 
        color: white !important; 
        padding: 6px 15px; 
        border-radius: 50px; 
        text-decoration: none; 
        font-size: 0.8em; 
        font-weight: bold;
        transition: 0.3s;
    }
    .time-link:hover { background-color: #444; transform: scale(1.05); }
    
    .lema-box { text-align: center; padding: 25px; background: #ffffff; border-radius: 15px; margin-bottom: 40px; border: 2px solid #333; }
    .lema-text { font-size: 1.8em; font-weight: bold; color: #111; margin: 0; }
    .lema-subtext { font-size: 1.1em; color: #666; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado con Lema
st.markdown("""
    <div class="lema-box">
        <p class="lema-text">"Moviendo cuerpos, conectando mentes"</p>
        <p class="lema-subtext">La calle es salud mental en movimiento</p>
    </div>
    """, unsafe_allow_html=True)

st.title("🏃‍♂️ Análisis: Educación Física en Castilla y León")
st.write("Propuestas sobre la materia de EF y su inclusión en 2º de Bachillerato.")

# 4. Vídeo del debate
st.video("https://www.youtube.com/watch?v=-KQeQzYw_xw")

st.divider()

# --- BLOQUE 1: PSOE ---
with st.container():
    col_l, col_r = st.columns([1, 5])
    col_l.image("https://upload.wikimedia.org/wikipedia/commons/b/b8/Logotipo_del_PSOE.svg", width=120)
    with col_r:
        st.markdown(f"""
        <div class="main-card psoe-box">
            <h2>1. Iñaki Gómez (PSOE)</h2>
            <p>El representante del PSOE enfatiza que la inclusión de la EF en 2º de Bachillerato ya es un mandato aprobado que la Junta debe ejecutar.</p>
            
            <span class="section-title">Sobre la Educación Física escolar:</span>
            <span class="quote-text">"El Partido Socialista quiere que haya más educación física en las aulas... sería bueno que se implementara una tercera hora en la educación secundaria y en primero de bachillerato."</span>
            <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=2081" target="_blank">⏱️ Ver minuto [34:41]</a>
            
            <span class="section-title">Sobre 2º de Bachillerato:</span>
            <span class="quote-text">"Ahora mismo ya se aprobaron las cortes... eso fue una iniciativa del grupo socialista en Cortes de Castilla y León y se publicó en junio del 2025 en el cual se invita a la Junta a que lo ponga en marcha... ahora hay que estar a la Junta de Castilla y León a que se implemente esa esa asignatura optativa en el segundo bachillerato."</span>
            <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=2050" target="_blank">⏱️ Ver minuto [34:10]</a>
            
            <span class="section-title">Estado de las instalaciones:</span>
            <span class="quote-text">"Da mucha pena que profesionales de la actividad física tengan que impartir sus clases, su docencia, en algunas instalaciones pues decrépitas... las instalaciones educativas en el ámbito del deporte tienen muchas carencias."</span>
            <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=2146" target="_blank">⏱️ Ver minuto [35:46]</a>
        </div>
        """, unsafe_allow_html=True)

# --- BLOQUE 2: VOX ---
with st.container():
    col_l, col_r = st.columns([1, 5])
    col_l.image("https://upload.wikimedia.org/wikipedia/commons/d/df/Vox_logo.svg", width=120)
    with col_r:
        st.markdown(f"""
        <div class="main-card vox-box">
            <h2>2. Enrique Jiménez (VOX)</h2>
            <p>El representante de VOX destaca el valor curricular de la materia y la necesidad de especialistas desde edades tempranas.</p>
            
            <span class="section-title">Sobre la Educación Física escolar:</span>
            <span class="quote-text">"Apostaremos por más horas de educación física, más calidad docente, más especialización... en primaria como infantil la materia de educación física no siempre viene acompañada por el especialista... nuestra apuesta es muy clara por la profesionalización y no al intrusismo profesional."</span>
            <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1740" target="_blank">⏱️ Ver minuto [29:00]</a>
            
            <span class="section-title">Sobre 2º de Bachillerato:</span>
            <span class="quote-text">"Apostamos y agradecemos al Colegio Profesional... el trabajo que se realiza en el desarrollo curricular de las materias optativas de anatomía funcional en primero de bachillerato y de la optativa de actividad física y salud en segundo de bachillerato dándole un componente curricular importante."</span>
            <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1313" target="_blank">⏱️ Ver minuto [21:53]</a>
            
            <span class="section-title">Visión de la materia:</span>
            <span class="quote-text">"La educación física no es una asignatura secundaria... es una herramienta esencial para combatir el sedentarismo, la obesidad infantil... y sobre todo como fuente de plasticidad neuronal."</span>
            <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1692" target="_blank">⏱️ Ver minuto [28:12]</a>
        </div>
        """, unsafe_allow_html=True)

# --- BLOQUE 3: PP ---
with st.container():
    col_l, col_r = st.columns([1, 5])
    col_l.image("https://upload.wikimedia.org/wikipedia/commons/d/de/Logo_del_Partido_Popular_%282019%29.svg", width=120)
    with col_r:
        st.markdown(f"""
        <div class="main-card pp-box">
            <h2>3. Borja del Barrio (PP)</h2>
            <p>El representante del PP se enfoca en el bienestar del alumno en años de alta carga académica y la importancia de los valores sociales.</p>
            
            <span class="section-title">Sobre la Educación Física escolar:</span>
            <span class="quote-text">"Nos preocupa el desplegar y el impulsar un programa de fomento del deporte entre los más jóvenes que tiene que venir precisamente, tiene que nacer de esas escuelas."</span>
            <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1860" target="_blank">⏱️ Ver minuto [31:00]</a>
            
            <span class="section-title">Sobre 2º de Bachillerato:</span>
            <span class="quote-text">"Yo recuerdo que ese año es un año complicado... estás pendiente de la nota, la EVAU, las medias... aunque solo sea por tener un momento de poder hacer deporte... el que se pueda fomentar el tener dentro de ese programa curricular unas horas de actividad física para entendemos que también es importante."</span>
            <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1962" target="_blank">⏱️ Ver minuto [32:42]</a>
            
            <span class="section-title">Valores y relaciones:</span>
            <span class="quote-text">"Es importante el aprender esas relaciones sociales que tienen que empezar desde la escuela... lo que fomentan son valores como el trabajo en equipo, como el sacrificio."</span>
            <a class="time-link" href="https://youtu.be/-KQeQzYw_xw?t=1894" target="_blank">⏱️ Ver minuto [31:34]</a>
        </div>
        """, unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.caption("Análisis independiente - Elecciones CyL 2026")