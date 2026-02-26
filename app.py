import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Análisis Educación Física CyL", layout="wide")

# 2. Estilos CSS para mejorar la apariencia sin romper el texto
st.markdown("""
    <style>
    .stMarkdown p { font-size: 1.1em; line-height: 1.6; }
    .quote { 
        background-color: #f0f2f6; 
        padding: 15px; 
        border-radius: 10px; 
        border-left: 5px solid #333; 
        font-style: italic;
        margin: 10px 0px;
    }
    .party-title { font-weight: bold; font-size: 1.5em; margin-bottom: 10px; }
    .section-header { font-weight: bold; color: #555; text-transform: uppercase; font-size: 0.9em; margin-top: 15px; }
    .time-btn {
        background-color: #000;
        color: white !important;
        padding: 5px 15px;
        border-radius: 20px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.8em;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Encabezado y Lema
st.text("")
st.markdown("<h1 style='text-align: center;'>🏃‍♂️ Moviendo cuerpos, conectando mentes</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em;'><i>La calle es salud mental en movimiento</i></p>", unsafe_allow_html=True)
st.divider()

# 4. Vídeo principal
st.video("https://www.youtube.com/watch?v=-KQeQzYw_xw")
st.divider()

# --- BLOQUE 1: Iñaki Gómez (PSOE) ---
col1, col2 = st.columns([1, 4])
with col1:
    # Logo PSOE
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/b8/Logotipo_del_PSOE.svg", width=150)
with col2:
    st.markdown("<div class='party-title'>1. Iñaki Gómez (PSOE)</div>", unsafe_allow_html=True)
    st.write("El representante del PSOE enfatiza que la inclusión de la EF en 2º de Bachillerato ya es un mandato aprobado que la Junta debe ejecutar.")
    
    st.markdown("**Sobre la Educación Física escolar:**", unsafe_allow_html=True)
    st.markdown('<div class="quote">"El Partido Socialista quiere que haya más educación física en las aulas... sería bueno que se implementara una tercera hora en la educación secundaria y en primero de bachillerato."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2081" class="time-btn">⏱️ Ver minuto [34:41]</a>', unsafe_allow_html=True)
    
    st.markdown("**Sobre 2º de Bachillerato:**", unsafe_allow_html=True)
    st.markdown('<div class="quote">"Ahora mismo ya se aprobaron las cortes... eso fue una iniciativa del grupo socialista en Cortes de Castilla y León y se publicó en junio del 2025 en el cual se invita a la Junta a que lo ponga en marcha... ahora hay que estar a la Junta de Castilla y León a que se implemente esa esa asignatura optativa en el segundo bachillerato."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2050" class="time-btn">⏱️ Ver minuto [34:10]</a>', unsafe_allow_html=True)
    
    st.markdown("**Estado de las instalaciones:**", unsafe_allow_html=True)
    st.markdown('<div class="quote">"Da mucha pena que profesionales de la actividad física tengan que impartir sus clases, su docencia, en algunas instalaciones pues decrépitas... las instalaciones educativas en el ámbito del deporte tienen muchas carencias."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2146" class="time-btn">⏱️ Ver minuto [35:46]</a>', unsafe_allow_html=True)

st.divider()

# --- BLOQUE 2: Enrique Jiménez (VOX) ---
col3, col4 = st.columns([1, 4])
with col3:
    # Logo VOX
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/df/Vox_logo.svg", width=150)
with col4:
    st.markdown("<div class='party-title'>2. Enrique Jiménez (VOX)</div>", unsafe_allow_html=True)
    st.write("El representante de VOX destaca el valor curricular de la materia y la necesidad de especialistas desde edades tempranas.")
    
    st.markdown("**Sobre la Educación Física escolar:**", unsafe_allow_html=True)
    st.markdown('<div class="quote">"Apostaremos por más horas de educación física, más calidad docente, más especialización... en primaria como infantil la materia de educación física no siempre viene acompañada por el especialista... nuestra apuesta es muy clara por la profesionalización y no al intrusismo profesional."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1740" class="time-btn">⏱️ Ver minuto [29:00]</a>', unsafe_allow_html=True)
    
    st.markdown("**Sobre 2º de Bachillerato:**", unsafe_allow_html=True)
    st.markdown('<div class="quote">"Apostamos y agradecemos al Colegio Profesional... el trabajo que se realiza en el desarrollo curricular de las materias optativas de anatomía funcional en primero de bachillerato y de la optativa de actividad física y salud en segundo de bachillerato dándole un componente curricular importante."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1313" class="time-btn">⏱️ Ver minuto [21:53]</a>', unsafe_allow_html=True)
    
    st.markdown("**Visión de la materia:**", unsafe_allow_html=True)
    st.markdown('<div class="quote">"La educación física no es una asignatura secundaria... es una herramienta esencial para combatir el sedentarismo, la obesidad infantil... y sobre todo como fuente de plasticidad neuronal."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1692" class="time-btn">⏱️ Ver minuto [28:12]</a>', unsafe_allow_html=True)

st.divider()

# --- BLOQUE 3: Borja del Barrio (PP) ---
col5, col6 = st.columns([1, 4])
with col5:
    # Logo PP
    st.image("https://upload.wikimedia.org/wikipedia/commons/d/de/Logo_del_Partido_Popular_%282019%29.svg", width=150)
with col6:
    st.markdown("<div class='party-title'>3. Borja del Barrio (PP)</div>", unsafe_allow_html=True)
    st.write("El representante del PP se enfoca en el bienestar del alumno en años de alta carga académica y la importancia de los valores sociales.")
    
    st.markdown("**Sobre la Educación Física escolar:**", unsafe_allow_html=True)
    st.markdown('<div class="quote">"Nos preocupa el desplegar y el impulsar un programa de fomento del deporte entre los más jóvenes que tiene que venir precisamente, tiene que nacer de esas escuelas."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1860" class="time-btn">⏱️ Ver minuto [31:00]</a>', unsafe_allow_html=True)
    
    st.markdown("**Sobre 2º de Bachillerato:**", unsafe_allow_html=True)
    st.markdown('<div class="quote">"Yo recuerdo que ese año es un año complicado... estás pendiente de la nota, la EVAU, las medias... aunque solo sea por tener un momento de poder hacer deporte... el que se pueda fomentar el tener dentro de ese programa curricular unas horas de actividad física para entendemos que también es importante."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1962" class="time-btn">⏱️ Ver minuto [32:42]</a>', unsafe_allow_html=True)
    
    st.markdown("**Valores y relaciones:**", unsafe_allow_html=True)
    st.markdown('<div class="quote">"Es importante el aprender esas relaciones sociales que tienen que empezar desde la escuela... lo que fomentan son valores como el trabajo en equipo, como el sacrificio."</div>', unsafe_allow_html=True)
    st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1894" class="time-btn">⏱️ Ver minuto [31:34]</a>', unsafe_allow_html=True)

st.divider()
st.caption("Resumen elaborado para el Día de la Educación Física en la Calle.")