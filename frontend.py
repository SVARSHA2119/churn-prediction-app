import streamlit as st
import requests

# ⚠️ IMPORTANT: Use deployed API URL
API_URL = "https://churn-prediction-app.onrender.com/predict"

st.title("Customer Churn Predictor")

# Inputs
tenure = st.number_input("Tenure (months)", min_value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
total_charges = st.number_input("Total Charges", min_value=0.0)

if st.button("Predict"):
    data = {
        "tenure": tenure,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges
    }

    try:
        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            result = response.json()

            prediction_text = result.get("result", "No result")
            probability = result.get("probability", None)

            st.success(f"Prediction: {prediction_text}")

            if probability is not None:
                st.write(f"Probability of churn: {probability * 100:.2f}%")

        else:
            st.error("Error: API not responding")

    except Exception as e:
        st.error(f"Error: {e}")