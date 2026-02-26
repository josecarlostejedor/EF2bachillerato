import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Enfoque EF CyL", layout="wide")

# 2. Estilos CSS: Limpios y sin errores de imagen
st.markdown("""
    <style>
    .main-title { text-align: center; color: #1f1f1f; font-size: 2.2em; font-weight: bold; margin-bottom: 20px; }
    .stVideo { margin-bottom: 30px; }
    
    /* Cuadros de texto */
    .quote-box {
        background-color: #f8f9fa;
        padding: 18px;
        border-radius: 10px;
        border-left: 5px solid #333;
        margin: 12px 0px;
        color: #222;
        line-height: 1.5;
    }
    
    /* Siglas de los partidos */
    .party-tag {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        padding: 10px;
        border-radius: 10px;
        color: white;
        margin-bottom: 10px;
    }
    
    /* Botones de tiempo */
    .time-link {
        background-color: #000;
        color: white !important;
        padding: 6px 18px;
        border-radius: 20px;
        text-decoration: none;
        font-weight: bold;
        font-size: 0.85em;
        display: inline-block;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Título corregido
st.markdown('<div class="main-title">"Cambiando el enfoque de la Educación Física y Deportiva en nuestra Comunidad Autónoma"</div>', unsafe_allow_html=True)
st.divider()

# 4. Vídeo
st.video("https://www.youtube.com/watch?v=-KQeQzYw_xw")
st.divider()

# --- BLOQUE 1: PSOE ---
with st.container(border=True):
    col1, col2 = st.columns([1, 4])
    with col1:
        # Siglas con color PSOE
        st.markdown('<div class="party-tag" style="background-color: #EF3B2C;">PSOE</div>', unsafe_allow_html=True)
    with col2:
        st.subheader("1. Iñaki Gómez")
        st.write("**El representante del PSOE enfatiza que la inclusión de la EF en 2º de Bachillerato ya es un mandato aprobado que la Junta debe ejecutar.**")
        
        st.caption("SOBRE LA EDUCACIÓN FÍSICA ESCOLAR")
        st.markdown('<div class="quote-box">"El Partido Socialista quiere que haya más educación física en las aulas... sería bueno que se implementara una tercera hora en la educación secundaria y en primero de bachillerato."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2081" class="time-link">⏱️ Ver minuto [34:41]</a>', unsafe_allow_html=True)
        
        st.caption("SOBRE 2º DE BACHILLERATO")
        st.markdown('<div class="quote-box">"Ahora mismo ya se aprobaron las cortes... eso fue una iniciativa del grupo socialista en Cortes de Castilla y León y se publicó en junio del 2025 en el cual se insta a la Junta a que lo ponga en marcha... ahora hay que estar a la Junta de Castilla y León a que se implemente esa esa asignatura optativa en el segundo bachillerato."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2050" class="time-link">⏱️ Ver minuto [34:10]</a>', unsafe_allow_html=True)
        
        st.caption("ESTADO DE LAS INSTALACIONES")
        st.markdown('<div class="quote-box">"Da mucha pena que profesionales de la actividad física tengan que impartir sus clases, su docencia, en algunas instalaciones pues decrépitas... las instalaciones educativas en el ámbito del deporte tienen muchas carencias."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2146" class="time-link">⏱️ Ver minuto [35:46]</a>', unsafe_allow_html=True)

st.write("") # Espacio entre bloques

# --- BLOQUE 2: VOX ---
with st.container(border=True):
    col3, col4 = st.columns([1, 4])
    with col3:
        # Siglas con color VOX
        st.markdown('<div class="party-tag" style="background-color: #63BE21;">VOX</div>', unsafe_allow_html=True)
    with col4:
        st.subheader("2. Enrique Jiménez")
        st.write("**El representante de VOX destaca el valor curricular de la materia y la necesidad de especialistas desde edades tempranas.**")
        
        st.caption("SOBRE LA EDUCACIÓN FÍSICA ESCOLAR")
        st.markdown('<div class="quote-box">"Apostaremos por más horas de educación física, más calidad docente, más especialización... en primaria como infantil la materia de educación física no siempre viene acompañada por el especialista... nuestra apuesta es muy clara por la profesionalización y no al intrusismo profesional."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1740" class="time-link">⏱️ Ver minuto [29:00]</a>', unsafe_allow_html=True)
        
        st.caption("SOBRE 2º DE BACHILLERATO")
        st.markdown('<div class="quote-box">"Apostamos y agradecemos al Colegio Profesional... el trabajo que se realiza en el desarrollo curricular de las materias optativas de anatomía funcional en primero de bachillerato y de la optativa de actividad física y salud en segundo de bachillerato dándole un componente curricular importante."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1313" class="time-link">⏱️ Ver minuto [21:53]</a>', unsafe_allow_html=True)
        
        st.caption("VISIÓN DE LA MATERIA")
        st.markdown('<div class="quote-box">"La educación física no es una asignatura secundaria... es una herramienta esencial para combatir el sedentarismo, la obesidad infantil... y sobre todo como fuente de plasticidad neuronal."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1692" class="time-link">⏱️ Ver minuto [28:12]</a>', unsafe_allow_html=True)

st.write("") # Espacio entre bloques

# --- BLOQUE 3: PP ---
with st.container(border=True):
    col5, col6 = st.columns([1, 4])
    with col5:
        # Siglas con color PP
        st.markdown('<div class="party-tag" style="background-color: #0054A6;">PP</div>', unsafe_allow_html=True)
    with col6:
        st.subheader("3. Borja del Barrio")
        st.write("**El representante del PP se enfoca en el bienestar del alumno en años de alta carga académica y la importancia de los valores sociales.**")
        
        st.caption("SOBRE LA EDUCACIÓN FÍSICA ESCOLAR")
        st.markdown('<div class="quote-box">"Nos preocupa el desplegar y el impulsar un programa de fomento del deporte entre los más jóvenes que tiene que venir precisamente, tiene que nacer de esas escuelas."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1860" class="time-link">⏱️ Ver minuto [31:00]</a>', unsafe_allow_html=True)
        
        st.caption("SOBRE 2º DE BACHILLERATO")
        st.markdown('<div class="quote-box">"Yo recuerdo que ese año es un año complicado... estás pendiente de la nota, la EVAU, las medias... aunque solo sea por tener un momento de poder hacer deporte... el que se pueda fomentar el tener dentro de ese programa curricular unas horas de actividad física para entendemos que también es importante."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1962" class="time-link">⏱️ Ver minuto [32:42]</a>', unsafe_allow_html=True)
        
        st.caption("VALORES Y RELACIONES")
        st.markdown('<div class="quote-box">"Es importante el aprender esas relaciones sociales que tienen que empezar desde la escuela... lo que fomentan son valores como el trabajo en equipo, como el sacrificio."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1894" class="time-link">⏱️ Ver minuto [31:34]</a>', unsafe_allow_html=True)

st.divider()
st.info("Plataforma de visualización de propuestas políticas para la Educación Física en CyL.")