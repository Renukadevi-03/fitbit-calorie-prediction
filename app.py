import streamlit as st
import numpy as np
import joblib

# Load saved model
model = joblib.load('xgb_model.pkl')

# Load scaler
scaler = joblib.load('scaler.pkl')

# App title
st.title("Fitbit Calorie Burn Prediction")

st.write("Predict calories burned during workouts")

# User Inputs
age = st.number_input("Age", 10, 80)

weight = st.number_input("Weight (kg)", 30.0, 150.0)

height = st.number_input("Height (m)", 1.0, 2.5)

avg_bpm = st.number_input("Average BPM", 50, 220)

session_duration = st.number_input(
    "Session Duration (hours)",
    0.1,
    5.0
)

# Predict button
if st.button("Predict Calories Burned"):

    # Create feature array
    features = np.array([[
        age,
        weight,
        height,
        avg_bpm,
        session_duration
    ]])

    # Scale features
    features_scaled = scaler.transform(features)

    # Predict
    prediction = model.predict(features_scaled)

    # Display result
    st.success(
        f"Estimated Calories Burned: {prediction[0]:.2f}"
    )
    gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)
workout = st.selectbox(
    "Workout Type",
    ["Cardio", "HIIT", "Strength", "Yoga"]
)
experience = st.selectbox(
    "Experience Level",
    ["Beginner", "Intermediate", "Advanced"]
)