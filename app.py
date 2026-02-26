import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Enfoque EF CyL", layout="wide")

# 2. Estilos CSS corregidos para asegurar que los cuadros se vean
st.markdown("""
    <style>
    .stVideo { margin-bottom: 20px; }
    .quote-box {
        background-color: #f1f3f6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid #333;
        margin: 10px 0px;
    }
    .time-link {
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

# 3. Nuevo Título
st.markdown("<h1 style='text-align: center;'>\"Cambiando el enfoque de la Educación Física y Deportiva en nuestra Comunidad Autónoma\"</h1>", unsafe_allow_html=True)
st.divider()

# 4. Vídeo
st.video("https://www.youtube.com/watch?v=-KQeQzYw_xw")
st.divider()

# --- BLOQUE 1: PSOE ---
with st.container(border=True):
    col1, col2 = st.columns([1, 4])
    with col1:
        # Intento de carga de logo con fallback visual
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Logotipo_del_PSOE.svg/512px-Logotipo_del_PSOE.svg.png", width=130)
        st.markdown("<h3 style='color: #EF3B2C; text-align: center;'>PSOE</h3>", unsafe_allow_html=True)
    with col2:
        st.subheader("1. Iñaki Gómez")
        st.write("**El representante del PSOE enfatiza que la inclusión de la EF en 2º de Bachillerato ya es un mandato aprobado que la Junta debe ejecutar.**")
        
        st.caption("SOBRE LA EDUCACIÓN FÍSICA ESCOLAR")
        st.markdown('<div class="quote-box">"El Partido Socialista quiere que haya más educación física en las aulas... sería bueno que se implementara una tercera hora en la educación secundaria y en primero de bachillerato."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2081" class="time-link">⏱️ Minuto [34:41]</a>', unsafe_allow_html=True)
        
        st.caption("SOBRE 2º DE BACHILLERATO")
        st.markdown('<div class="quote-box">"Ahora mismo ya se aprobaron las cortes... eso fue una iniciativa del grupo socialista en Cortes de Castilla y León y se publicó en junio del 2025 en el cual se insta a la Junta a que lo ponga en marcha... ahora hay que estar a la Junta de Castilla y León a que se implemente esa esa asignatura optativa en el segundo bachillerato."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2050" class="time-link">⏱️ Minuto [34:10]</a>', unsafe_allow_html=True)
        
        st.caption("ESTADO DE LAS INSTALACIONES")
        st.markdown('<div class="quote-box">"Da mucha pena que profesionales de la actividad física tengan que impartir sus clases, su docencia, en algunas instalaciones pues decrépitas... las instalaciones educativas en el ámbito del deporte tienen muchas carencias."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=2146" class="time-link">⏱️ Minuto [35:46]</a>', unsafe_allow_html=True)

st.write("") # Espaciador

# --- BLOQUE 2: VOX ---
with st.container(border=True):
    col3, col4 = st.columns([1, 4])
    with col3:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Vox_logo.svg/512px-Vox_logo.svg.png", width=130)
        st.markdown("<h3 style='color: #63BE21; text-align: center;'>VOX</h3>", unsafe_allow_html=True)
    with col4:
        st.subheader("2. Enrique Jiménez")
        st.write("**El representante de VOX destaca el valor curricular de la materia y la necesidad de especialistas desde edades tempranas.**")
        
        st.caption("SOBRE LA EDUCACIÓN FÍSICA ESCOLAR")
        st.markdown('<div class="quote-box">"Apostaremos por más horas de educación física, más calidad docente, más especialización... en primaria como infantil la materia de educación física no siempre viene acompañada por el especialista... nuestra apuesta es muy clara por la profesionalización y no al intrusismo profesional."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1740" class="time-link">⏱️ Minuto [29:00]</a>', unsafe_allow_html=True)
        
        st.caption("SOBRE 2º DE BACHILLERATO")
        st.markdown('<div class="quote-box">"Apostamos y agradecemos al Colegio Profesional... el trabajo que se realiza en el desarrollo curricular de las materias optativas de anatomía funcional en primero de bachillerato y de la optativa de actividad física y salud en segundo de bachillerato dándole un componente curricular importante."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1313" class="time-link">⏱️ Minuto [21:53]</a>', unsafe_allow_html=True)
        
        st.caption("VISIÓN DE LA MATERIA")
        st.markdown('<div class="quote-box">"La educación física no es una asignatura secundaria... es una herramienta esencial para combatir el sedentarismo, la obesidad infantil... y sobre todo como fuente de plasticidad neuronal."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1692" class="time-link">⏱️ Minuto [28:12]</a>', unsafe_allow_html=True)

st.write("") # Espaciador

# --- BLOQUE 3: PP ---
with st.container(border=True):
    col5, col6 = st.columns([1, 4])
    with col5:
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Logo_del_Partido_Popular_%282019%29.svg/512px-Logo_del_Partido_Popular_%282019%29.svg.png", width=130)
        st.markdown("<h3 style='color: #0054A6; text-align: center;'>PP</h3>", unsafe_allow_html=True)
    with col6:
        st.subheader("3. Borja del Barrio")
        st.write("**El representante del PP se enfoca en el bienestar del alumno en años de alta carga académica y la importancia de los valores sociales.**")
        
        st.caption("SOBRE LA EDUCACIÓN FÍSICA ESCOLAR")
        st.markdown('<div class="quote-box">"Nos preocupa el desplegar y el impulsar un programa de fomento del deporte entre los más jóvenes que tiene que venir precisamente, tiene que nacer de esas escuelas."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1860" class="time-link">⏱️ Minuto [31:00]</a>', unsafe_allow_html=True)
        
        st.caption("SOBRE 2º DE BACHILLERATO")
        st.markdown('<div class="quote-box">"Yo recuerdo que ese año es un año complicado... estás pendiente de la nota, la EVAU, las medias... aunque solo sea por tener un momento de poder hacer deporte... el que se pueda fomentar el tener dentro de ese programa curricular unas horas de actividad física para entendemos que también es importante."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1962" class="time-link">⏱️ Minuto [32:42]</a>', unsafe_allow_html=True)
        
        st.caption("VALORES Y RELACIONES")
        st.markdown('<div class="quote-box">"Es importante el aprender esas relaciones sociales que tienen que empezar desde la escuela... lo que fomentan son valores como el trabajo en equipo, como el sacrificio."</div>', unsafe_allow_html=True)
        st.markdown('<a href="https://youtu.be/-KQeQzYw_xw?t=1894" class="time-link">⏱️ Minuto [31:34]</a>', unsafe_allow_html=True)

st.divider()
st.info("Plataforma de visualización de propuestas políticas para la Educación Física.")