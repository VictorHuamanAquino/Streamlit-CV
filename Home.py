import streamlit as st
from PIL import Image
from io import BytesIO
import pandas as pd
import plotly.express as px
from datetime import datetime


icono_pagina = Image.open("images/icons/iconocurrículum.png")
st.set_page_config(page_title="Portfolio", page_icon=icono_pagina, layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Header ---
st.write("<h1 class='texto-primario'>Junior Data Engineer | Cloud Certified | Python Enthusiast</h1>", unsafe_allow_html=True)

st.divider()
# --- Sobre Mi ---
col1, col2 = st.columns(2)
with col1 :
    st.write("<h1 class='texto-primario'>Sobre mí</h1>", unsafe_allow_html=True)
    image = Image.open("images/photos/FotoJersey.jpg").resize((470,600))
    buffer = BytesIO()
    image.save(buffer, format="JPEG", quality=100)
    st.image(
        image,
        output_format="JPEG" 
        )

st.divider()
# --- Educacion ---
st.write("<h1 class='texto-primario'>Educación</h1>", unsafe_allow_html=True)

df_educacion = pd.read_csv("data/formacionprof.csv",delimiter=";",encoding="UTF-8")

df_educacion['Start'] = pd.to_datetime(df_educacion['Start'], errors='coerce')
df_educacion['Finish'] = pd.to_datetime(df_educacion['Finish'], errors='coerce')

# Fecha actual
hoy = pd.Timestamp(datetime.now().date())

# Crear columna temporal para el gráfico: si Finish es mayor que hoy, reemplazar por hoy
df_educacion['Finish_grafico'] = df_educacion['Finish'].apply(lambda x: min(x, hoy))

fig = px.timeline(df_educacion, x_start="Start", x_end="Finish_grafico", y="title", color="Done")
fig.update_yaxes(autorange="reversed")

fig.update_layout(
    yaxis_title=None,
    xaxis=dict(
        showgrid=True,      # Líneas de background
        gridcolor='lightgray',
        title_font=dict(size=20),
        tickfont=dict(size=20)
    ),
    yaxis=dict(
        gridcolor='lightgray',
        title_font=dict(size=20),
        tickfont=dict(size=20)
    ),
    legend=dict(
        title="Estado",
        font=dict(size=20),
        bgcolor='rgba(0,0,0,0)',
        bordercolor='black',
        borderwidth=1
    ),
    margin=dict(l=150, r=50, t=100, b=100),  # Espacios alrededor
    height=500
)

st.plotly_chart(fig)
st.divider()


st.write("""
Soy un profesional con formación en ingeniería de datos y un fuerte interés en el desarrollo de soluciones 
basadas en la nube (AWS, Azure, GCP).  
He trabajado en proyectos de ETL, orquestación de pipelines y automatización de procesos con Python.
""")

st.header("Habilidades Técnicas - Oveview")
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    - Python (Pandas, PySpark, Airflow)
    - SQL / PostgreSQL
    - Docker
    - Linux / Bash
    """)

with col2:
    st.markdown("""
    - AWS / Azure / GCP
    - Data Modeling
    - CI/CD (GitHub Actions)
    - Streamlit / Dash
    """)


