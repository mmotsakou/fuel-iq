import streamlit as st
import pandas as pd
import joblib


# Load the trained model
model = joblib.load("mpg_model_final.pkl")

# MPG categories
mpg_categories = ["Α-Eco Warrior Mode", "B-Smart Saver mode", "C-Think before you fill", "D-Fuel Monster"]

# App title
st.title("Fuel iQ 🚗⛽")

# Input data
cylinders = st.slider("Cylinders", 3, 12, 6)
displacement = st.number_input("Displacement", min_value=50, max_value=500, value=200)
horsepower = st.number_input("Horsepower", min_value=40, max_value=250, value=100)
weight = st.number_input("Weight (lbs)", min_value=1500, max_value=5000, value=3000)
acceleration = st.number_input("Acceleration", min_value=5.0, max_value=25.0, value=15.0)
model_year = st.slider("Model Year", 70, 82, 76)
origin = st.selectbox("Origin", [1, 2, 3])

# Prediction
if st.button("Predict MPG Category"):
    input_data = pd.DataFrame([[cylinders, displacement, horsepower, weight, acceleration, model_year, origin]],
                              columns=["cylinders", "displacement", "horsepower", "weight", "acceleration", "model_year", "origin"])

    prediction = model.predict(input_data)[0]
    result = mpg_categories[prediction]

    st.success(f"🚘 Το μοντέλο προβλέπει: **{result}**")
