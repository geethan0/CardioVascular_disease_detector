import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load your trained machine learning model
model = joblib.load('/Users/geethan/Downloads/heart_disease_model.sav')

# Define a function to make predictions
def predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    input_data = np.array([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]).reshape(1, -1)
    prediction = model.predict(input_data)
    return prediction

# Streamlit App
st.title('Cardiovascular Disease Detector')

# Sidebar with input widgets
st.sidebar.header('User Input')

age = st.sidebar.number_input('Age', min_value=1, max_value=100, value=40)
sex = st.sidebar.selectbox('Sex', ['Male', 'Female'])
cp = st.sidebar.selectbox('Chest Pain Type', [0, 1, 2, 3])
trestbps = st.sidebar.number_input('Resting Blood Pressure (mm Hg)', min_value=50, max_value=200, value=120)
chol = st.sidebar.number_input('Cholesterol (mg/dl)', min_value=50, max_value=500, value=200)
fbs = st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', ['No', 'Yes'])
restecg = st.sidebar.selectbox('Resting ECG', [0, 1, 2])
thalach = st.sidebar.number_input('Max Heart Rate Achieved', min_value=50, max_value=220, value=150)
exang = st.sidebar.selectbox('Exercise-Induced Angina', ['No', 'Yes'])
oldpeak = st.sidebar.number_input('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, value=0.0)
slope = st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
ca = st.sidebar.number_input('Number of Major Vessels Colored by Fluoroscopy', min_value=0, max_value=4, value=0)
thal = st.sidebar.selectbox('Thalassemia Type', [0, 1, 2, 3])

# Convert input values to numerical format
sex = 1 if sex == 'Male' else 0
fbs = 1 if fbs == 'Yes' else 0
exang = 1 if exang == 'Yes' else 0

# Make predictions when the 'Predict' button is clicked
if st.sidebar.button('Predict'):
    prediction = predict(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal)
    if prediction[0] == 1:
        st.sidebar.success('Prediction: You have a high risk of heart disease.')
    else:
        st.sidebar.success('Prediction: You have a low risk of heart disease.')

# Display data in the main panel if needed
# st.write('Input Data:', pd.DataFrame({'Age': [age], 'Sex': [sex], 'Chest Pain Type': [cp], ...}))

# You can add more sections or details to the app as per your requirements.

