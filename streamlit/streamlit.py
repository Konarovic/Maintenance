import pickle
import streamlit as st
import pandas as pd


# Page config
st.set_page_config(
    page_title="Failure Classifier",
    #page_icon="images/icone.png",
)

# Page title
st.title('Maintenance - Failure Prediction')
st.write("\n\n")

# Load the model
with open('../model/random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Streamlit interface to input data
col1, col2 = st.columns(2)

with col1:
    air = st.number_input(label='Air Temperature')
    process = st.number_input(label='Process Temperature')
    rpm = st.number_input(label='Rotational Speed')

with col2:
    torque = st.number_input(label='Torque')
    tool_wear = st.number_input(label='Tool Wear')
    type = st.selectbox(label='Type', options=['Low', 'Medium', 'High'])

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
if st.button('Predict'):
    predict = prediction(air, process, rpm, torque, tool_wear, type)
    st.success(predict)