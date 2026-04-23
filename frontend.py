import streamlit as st
import requests

API_URL = "https://churn-prediction-app-i4x9.onrender.com/predict"


st.title("Customer Churn Prediction")

# Inputs
tenure = st.number_input("Tenure", min_value=0, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=500.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=6000.0)

# Backend URL (Render)
API_URL = "https://churn-prediction-app-i4x9.onrender.com/predict"


if st.button("Predict"):

    payload = {
        "tenure": tenure,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges
    }

    try:
        response = requests.post(API_URL, json=payload)
        data = response.json()

        st.success(f"Prediction: {data['prediction']}")
        st.info(f"Probability: {data['probability']}%")
        st.write(data["meaning"])

    except Exception as e:
        st.error(f"Connection error: {e}")