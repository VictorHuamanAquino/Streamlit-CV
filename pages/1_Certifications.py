import streamlit as st
import pandas as pd

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.write("<h1 class='texto-primario'>Certificaciones</h1>", unsafe_allow_html=True)
