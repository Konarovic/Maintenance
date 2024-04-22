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
    st.title('Maintenance (WIP)')
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


### pour correspondance temperature degrés en kelvin = degrés + 293.15


if option == '1 / Prédictions':
    st.write('Tableau de prédictions')
   
    col1,col2 = st.columns(2)

    with col1 :
        air = st.number_input(label='Temperature de l air', step=0.1) 
        process = st.number_input(label='Temperature de fonctionnement[K]', step=0.1)
        rpm = st.number_input(label='Vitesse de rotation[rpm]', step=5)

    with col2:
        torque = st.number_input(label='Couple[3-80]', step=0.1)
        tool_wear = st.number_input(label='Taux d usure[0-260]', step=1)
        type = st.selectbox(label='Qualité', options=['Basse', 'Moyenne', 'Haute'])


    # Function to predict the input
    def prediction(air, process, rpm, torque, tool_wear, type):
        # Create a df with input data
        df_input = pd.DataFrame({
            'Air_temperature': [air],
            'Process_temperature': [process],
            'Rotational_speed': [rpm],
            'Torque': [torque],
            'Tool_wear': [tool_wear],
            'Type': [type]
        })

        prediction = model.predict(df_input)
        return prediction

    # Botton to predict
    st.markdown('WIP !!!!')
    if st.button('Predict (WIP)'):
        predict = prediction(air, process, rpm, torque, tool_wear, type)
        st.success(predict)

# Page 2
elif option == '2 / Détails du modèle':
    st.write('wip')
    st.dataframe('./data/maintenance_data_clean.csv')
  

