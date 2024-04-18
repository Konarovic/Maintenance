import pickle
import streamlit as st
import pandas as pd


# Page 
st.title('Maintenance')
col1, col2, col3 = st.columns([1,4,1])
with col1:
    st.write("")
with col2 :
    st.subheader('Prédiction de pannes')
with col3:
    st.write("")
st.write("\n\n")


# chargement du modele

with open('../model/lgbmc.pkl', 'rb') as model_file:
    model = pickle.load(model_file)