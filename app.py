import streamlit as st

# 1. Configuración inicial
st.set_page_config(page_title="EF Castilla y León 2026", layout="wide")

# 2. CSS personalizado
st.markdown("""
    <style>
    .quote-box {
        background-color: #f1f3f6;
        border-left: 6px solid #333;
        padding: 1.2rem;
        margin: 10px 0;
        border-radius: 5px;
        font-style: italic;
        font-size: 1.05rem;
        color: #1a1a1a;
    }
    .topic-title {
        font-weight: bold;
        color: #444;
        margin-top: 1.5rem;
        display: block;
        text-transform: uppercase;
        font-size: 0.85rem;
    }
    .time-button {
        display: inline-block;
        background-color: #000;
        color: #fff !important;
        padding: 8px 16px;
        border-radius: 25px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.8rem;
        margin: 10px 0 25px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Cabecera y Lema
st.title("🏃‍♂️ Análisis: Educación Física en CyL")
st.markdown("### *'Propuestas de los distintos partidos en materia de Educación Física y Deportiva en la Comunidad de Castilla y León'*")
st.divider()

# 4. Video
st.video("https://www.youtube.com/watch?v=-KQeQzYw_xw")
st.divider()

# --- BLOQUE 1: PSOE ---
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Logotipo_del_PSOE.svg/512px-Logotipo_del_PSOE.svg.png", width=140)
with col2:
    st.header("1. Iñaki Gómez (PSOE)")
    st.write("El representante del PSOE enfatiza que la inclusión de la EF en 2º de Bachillerato ya es un mandato aprobado que la Junta debe ejecutar.")
    
    st.markdown('<span class="topic-title">Sobre la Educación Física escolar:</span>', unsafe_allow_html=True)
    st.markdown('<div class="quote-box">"El Partido Socialista quiere que haya más educación física en las aulas... sería bueno que se implementara una tercera hora en la educación secundaria y en primero de bachillerato."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2081" class="time-button">⏱️ Ver minuto [34:41]</a>', unsafe_allow_html=True)
    
    st.markdown('<span class="topic-title">Sobre 2º de Bachillerato:</span>', unsafe_allow_html=True)
    st.markdown('<div class="quote-box">"Ahora mismo ya se aprobaron las cortes... eso fue una iniciativa del grupo socialista en Cortes de Castilla y León y se publicó en junio del 2025 en el cual se insta a la Junta a que lo ponga en marcha... ahora hay que estar a la Junta de Castilla y León a que se implemente esa esa asignatura optativa en el segundo bachillerato."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2050" class="time-button">⏱️ Ver minuto [34:10]</a>', unsafe_allow_html=True)
    
    st.markdown('<span class="topic-title">Estado de las instalaciones:</span>', unsafe_allow_html=True)
    st.markdown('<div class="quote-box">"Da mucha pena que profesionales de la actividad física tengan que impartir sus clases, su docencia, en algunas instalaciones pues decrépitas... las instalaciones educativas en el ámbito del deporte tienen muchas carencias."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2146" class="time-button">⏱️ Ver minuto [35:46]</a>', unsafe_allow_html=True)

st.divider()

# --- BLOQUE 2: VOX ---
col3, col4 = st.columns([1, 4])
with col3:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Vox_logo.svg/512px-Vox_logo.svg.png", width=140)
with col4:
    st.header("2. Enrique Jiménez (VOX)")
    st.write("El representante de VOX destaca el valor curricular de la materia y la necesidad de especialistas desde edades tempranas.")
    
    st.markdown('<span class="topic-title">Sobre la Educación Física escolar:</span>', unsafe_allow_html=True)
    st.markdown('<div class="quote-box">"Apostaremos por más horas de educación física, más calidad docente, más especialización... en primaria como infantil la materia de educación física no siempre viene acompañada por el especialista... nuestra apuesta es muy clara por la profesionalización y no al intrusismo profesional."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1740" class="time-button">⏱️ Ver minuto [29:00]</a>', unsafe_allow_html=True)
    
    st.markdown('<span class="topic-title">Sobre 2º de Bachillerato:</span>', unsafe_allow_html=True)
    st.markdown('<div class="quote-box">"Apostamos y agradecemos al Colegio Profesional... el trabajo que se realiza en el desarrollo curricular de las materias optativas de anatomía funcional en primero de bachillerato y de la optativa de actividad física y salud en segundo de bachillerato dándole un componente curricular importante."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1313" class="time-button">⏱️ Ver minuto [21:53]</a>', unsafe_allow_html=True)
    
    st.markdown('<span class="topic-title">Visión de la materia:</span>', unsafe_allow_html=True)
    st.markdown('<div class="quote-box">"La educación física no es una asignatura secundaria... es una herramienta esencial para combatir el sedentarismo, la obesidad infantil... y sobre todo como fuente de plasticidad neuronal."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1692" class="time-button">⏱️ Ver minuto [28:12]</a>', unsafe_allow_html=True)

st.divider()

# --- BLOQUE 3: PP ---
col5, col6 = st.columns([1, 4])
with col5:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Logo_del_Partido_Popular_%282019%29.svg/512px-Logo_del_Partido_Popular_%282019%29.svg.png", width=140)
with col6:
    st.header("3. Borja del Barrio (PP)")
    st.write("El representante del PP se enfoca en el bienestar del alumno en años de alta carga académica y la importancia de los valores sociales.")
    
    st.markdown('<span class="topic-title">Sobre la Educación Física escolar:</span>', unsafe_allow_html=True)
    st.markdown('<div class="quote-box">"Nos preocupa el desplegar y el impulsar un programa de fomento del deporte entre los más jóvenes que tiene que venir precisamente, tiene que nacer de esas escuelas."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1860" class="time-button">⏱️ Ver minuto [31:00]</a>', unsafe_allow_html=True)
    
    st.markdown('<span class="topic-title">Sobre 2º de Bachillerato:</span>', unsafe_allow_html=True)
    st.markdown('<div class="quote-box">"Yo recuerdo que ese año es un año complicado... estás pendiente de la nota, la EVAU, las medias... aunque solo sea por tener un momento de poder hacer deporte... el que se pueda fomentar el tener dentro de ese programa curricular unas horas de actividad física para entendemos que también es importante."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1962" class="time-button">⏱️ Ver minuto [32:42]</a>', unsafe_allow_html=True)
    
    st.markdown('<span class="topic-title">Valores y relaciones:</span>', unsafe_allow_html=True)
    st.markdown('<div class="quote-box">"Es importante el aprender esas relaciones sociales que tienen que empezar desde la escuela... lo que fomentan son valores como el trabajo en equipo, como el sacrificio."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1894" class="time-button">⏱️ Ver minuto [31:34]</a>', unsafe_allow_html=True)

st.sidebar.markdown("### Información del proyecto")
st.sidebar.write("Esperemos que estas propuestas sean hechas realidad durante la próxima legislatura gobierne, quien gobierne. GRACIAS al COLEF de Castilla y León por organizar este encuetro. Todos los profesionales de la Educación Física esperamos que estos cambios se produzcan en la próxima legislatura")