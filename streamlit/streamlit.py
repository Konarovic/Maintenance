
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



# load
import joblib

# Load the LightGBM model
lgbmc_loaded_model = joblib.load('lgbmc_model.pkl')

# Now you can use lgbmc_loaded_model for predictions

