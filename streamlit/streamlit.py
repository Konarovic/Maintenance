
import joblib
import streamlit as st
import pandas as pd


# Page 

col1, col2, col3 = st.columns([1,4,1])
with col1:
    st.write("")
with col2 :
    st.title('Maintenance')
    st.subheader('Prédiction de pannes')
with col3:
    st.write("")
st.write("\n\n")


option = st.sidebar.selectbox(
    'Navigation',
    ('1 / Prédictions', '2 / Details du modèle')
)


