import joblib
import streamlit as st
import pandas as pd

# Charger le modèle
try:
    model = joblib.load('./model/lgbmc_model.pkl')
except FileNotFoundError:
    st.error("Le fichier du modèle est introuvable.")
except Exception as e:
    st.error(f"Une erreur s'est produite lors du chargement du modèle : {e}")


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

# menu
option = st.sidebar.selectbox(
    'Navigation',
    ('1 / Prédictions', '2 / Details du modèle')
)


# Page 1
if option == '1 / Prédictions':
    st.write('Tableau de prédictions')
   
    col1,col2 = st.columns(2)

    with col1 :
        air = st.number_input(label='Air Temperature[K]', step=0.1)
        process = st.number_input(label='Process Temperature[K]', step=0.1)
        rpm = st.number_input(label='Rotational Speed[rpm]', step=5)

    with col2:
        torque = st.number_input(label='Torque[3-80]', step=0.1)
        tool_wear = st.number_input(label='Tool Wear[0-260]', step=1)
        type = st.selectbox(label='Type', options=['Low', 'Medium', 'High'])

# Page 2
elif option == '2 / Détails du modèle':
    st.write('wip')
  

