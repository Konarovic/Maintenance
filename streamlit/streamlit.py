import pickle
import streamlit as st
import pandas as pd
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'model', 'lgbmc_model.pkl')


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


# chargement du model
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)