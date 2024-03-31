import pickle
import streamlit as st
import pandas as pd


# Page config
st.set_page_config(
    page_title="Failure Classifier",
    page_icon="C:/Users/prans/OneDrive/Desktop/sem 6/AiMl/mini project/images/icon.png", 
)

# Page title
st.title('Maintenance - Failure Prediction')
st.image('C:/Users/prans/OneDrive/Desktop/sem 6/AiMl/mini project/images/main.webp')
st.write("\n\n")

st.markdown(
    """
    This app aims to assist in classifying failures, thereby reducing the time required to analyze machine problems. It enables the analysis of sensor data to classify failures swiftly and expedite the troubleshooting process. It classifies the failures of 4 types - No failure, Heat Dissipation failure, Overstain failure and Tool wear failure. 
    """
)

# Load the model
with open('C:/Users/prans/OneDrive/Desktop/sem 6/AiMl/mini project/model/model.pkl', 'rb') as model_file:
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
        'air_temperature': [air],
        'process_temperature': [process],
        'rotational_speed': [rpm],
        'torque': [torque],
        'tool_wear': [tool_wear],
        'Type': [type]
    })
    
    prediction = model.predict(df_input)
    return prediction

# Botton to predict
if st.button('Predict'):
    predict = prediction(air, process, rpm, torque, tool_wear, type)
    st.success(predict)