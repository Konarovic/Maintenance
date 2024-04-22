
import pickle
import streamlit as st
import pandas as pd
import joblib

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


# import model

# Charger le modèle
lgbmc_model = joblib.load('../notebook/lgbmc_model.pkl')

with st.sidebar:
    st.[Model]
    st.[Model details]