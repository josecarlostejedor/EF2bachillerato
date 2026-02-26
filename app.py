import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Enfoque EF CyL", layout="wide")

# 2. Estilos CSS Robustos
st.markdown("""
    <style>
    .main-title { text-align: center; color: #1f1f1f; font-size: 2.2em; font-weight: bold; margin-bottom: 0.5em; }
    .card { padding: 25px; border-radius: 12px; margin-bottom: 25px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
    .psoe-card { border-left: 10px solid #EF3B2C; background-color: #fdf2f2; }
    .pp-card { border-left: 10px solid #0054A6; background-color: #f2f7fd; }
    .vox-card { border-left: 10px solid #63BE21; background-color: #f4faf0; }
    
    .quote { font-style: italic; background: rgba(255,255,255,0.6); padding: 12px; border-radius: 6px; margin: 10px 0; border: 1px dashed #ccc; display: block; }
    .label { font-weight: bold; color: #444; text-transform: uppercase; font-size: 0.8em; margin-top: 15px; display: block; }
    
    .btn-time { 
        display: inline-block; background: #000; color: #fff !important; padding: 5px 15px; 
        border-radius: 20px; text-decoration: none; font-size: 0.8em; font-weight: bold; margin-top: 5px;
    }
    .party-icon { 
        width: 100px; height: 100px; display: flex; align-items: center; justify-content: center; 
        color: white; font-weight: bold; font-size: 1.5em; border-radius: 8px; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Nuevo Título
st.markdown('<div class="main-title">"Cambiando el enfoque de la Educación Física y Deportiva en nuestra Comunidad Autónoma"</div>', unsafe_allow_html=True)
st.divider()

# 4. Vídeo
st.video("https://www.youtube.com/watch?v=-KQeQzYw_xw")
st.divider()

# Función para mostrar Logo o Icono si falla
def mostrar_logo(url, color, siglas):
    try:
        st.image(url, width=120)
    except:
        st.markdown(f'<div class="party-icon" style="background-color: {color};">{siglas}</div>', unsafe_allow_html=True)

# --- BLOQUE PSOE ---
col1, col2 = st.columns([1, 4])
with col1:
    mostrar_logo("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b8/Logotipo_del_PSOE.svg/512px-Logotipo_del_PSOE.svg.png", "#EF3B2C", "PSOE")
with col2:
    st.markdown('<div class="card psoe-card"><h3>1. Iñaki Gómez (PSOE)</h3>'
                '<p>El representante del PSOE enfatiza que la inclusión de la EF en 2º de Bachillerato ya es un mandato aprobado que la Junta debe ejecutar.</p>'
                '<span class="label">Sobre la Educación Física escolar:</span>'
                '<span class="quote">"El Partido Socialista quiere que haya más educación física en las aulas... sería bueno que se implementara una tercera hora en la educación secundaria y en primero de bachillerato."</span>'
                '<a class="btn-time" href="https://youtu.be/-KQeQzYw_xw?t=2081" target="_blank">⏱️ Minuto [34:41]</a>'
                '<span class="label">Sobre 2º de Bachillerato:</span>'
                '<span class="quote">"Ahora mismo ya se aprobaron las cortes... eso fue una iniciativa del grupo socialista en Cortes de Castilla y León y se publicó en junio del 2025 en el cual se insta a la Junta a que lo ponga en marcha... ahora hay que estar a la Junta de Castilla y León a que se implemente esa esa asignatura optativa en el segundo bachillerato."</span>'
                '<a class="btn-time" href="https://youtu.be/-KQeQzYw_xw?t=2050" target="_blank">⏱️ Minuto [34:10]</a>'
                '<span class="label">Estado de las instalaciones:</span>'
                '<span class="quote">"Da mucha pena que profesionales de la actividad física tengan que impartir sus clases, su docencia, en algunas instalaciones pues decrépitas... las instalaciones educativas en el ámbito del deporte tienen muchas carencias."</span>'
                '<a class="btn-time" href="https://youtu.be/-KQeQzYw_xw?t=2146" target="_blank">⏱️ Minuto [35:46]</a>'
                '</div>', unsafe_allow_html=True)

# --- BLOQUE VOX ---
col3, col4 = st.columns([1, 4])
with col3:
    mostrar_logo("https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Vox_logo.svg/512px-Vox_logo.svg.png", "#63BE21", "VOX")
with col4:
    st.markdown('<div class="card vox-card"><h3>2. Enrique Jiménez (VOX)</h3>'
                '<p>El representante de VOX destaca el valor curricular de la materia y la necesidad de especialistas desde edades tempranas.</p>'
                '<span class="label">Sobre la Educación Física escolar:</span>'
                '<span class="quote">"Apostaremos por más horas de educación física, más calidad docente, más especialización... en primaria como infantil la materia de educación física no siempre viene acompañada por el especialista... nuestra apuesta es muy clara por la profesionalización y no al intrusismo profesional."</span>'
                '<a class="btn-time" href="https://youtu.be/-KQeQzYw_xw?t=1740" target="_blank">⏱️ Minuto [29:00]</a>'
                '<span class="label">Sobre 2º de Bachillerato:</span>'
                '<span class="quote">"Apostamos y agradecemos al Colegio Profesional... el trabajo que se realiza en el desarrollo curricular de las materias optativas de anatomía funcional en primero de bachillerato y de la optativa de actividad física y salud en segundo de bachillerato dándole un componente curricular importante."</span>'
                '<a class="btn-time" href="https://youtu.be/-KQeQzYw_xw?t=1313" target="_blank">⏱️ Minuto [21:53]</a>'
                '<span class="label">Visión de la materia:</span>'
                '<span class="quote">"La educación física no es una asignatura secundaria... es una herramienta esencial para combatir el sedentarismo, la obesidad infantil... y sobre todo como fuente de plasticidad neuronal."</span>'
                '<a class="btn-time" href="https://youtu.be/-KQeQzYw_xw?t=1692" target="_blank">⏱️ Minuto [28:12]</a>'
                '</div>', unsafe_allow_html=True)

# --- BLOQUE PP ---
col5, col6 = st.columns([1, 4])
with col5:
    mostrar_logo("https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Logo_del_Partido_Popular_%282019%29.svg/512px-Logo_del_Partido_Popular_%282019%29.svg.png", "#0054A6", "PP")
with col6:
    st.markdown('<div class="card pp-card"><h3>3. Borja del Barrio (PP)</h3>'
                '<p>El representante del PP se enfoca en el bienestar del alumno en años de alta carga académica y la importancia de los valores sociales.</p>'
                '<span class="label">Sobre la Educación Física escolar:</span>'
                '<span class="quote">"Nos preocupa el desplegar y el impulsar un programa de fomento del deporte entre los más jóvenes que tiene que venir precisamente, tiene que nacer de esas escuelas."</span>'
                '<a class="btn-time" href="https://youtu.be/-KQeQzYw_xw?t=1860" target="_blank">⏱️ Minuto [31:00]</a>'
                '<span class="label">Sobre 2º de Bachillerato:</span>'
                '<span class="quote">"Yo recuerdo que ese año es un año complicado... estás pendiente de la nota, la EVAU, las medias... aunque solo sea por tener un momento de poder hacer deporte... el que se pueda fomentar el tener dentro de ese programa curricular unas horas de actividad física para entendemos que también es importante."</span>'
                '<a class="btn-time" href="https://youtu.be/-KQeQzYw_xw?t=1962" target="_blank">⏱️ Minuto [32:42]</a>'
                '<span class="label">Valores y relaciones:</span>'
                '<span class="quote">"Es importante el aprender esas relaciones sociales que tienen que empezar desde la escuela... lo que fomentan son valores como el trabajo en equipo, como el sacrificio."</span>'
                '<a class="btn-time" href="https://youtu.be/-KQeQzYw_xw?t=1894" target="_blank">⏱️ Minuto [31:34]</a>'
                '</div>', unsafe_allow_html=True)