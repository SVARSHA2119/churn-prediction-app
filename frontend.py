import streamlit as st
import requests

st.title("Customer Churn Predictor")

tenure = st.number_input("Tenure (months)", min_value=0)
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

if st.button("Predict"):
    data = {
        "tenure": int(tenure),
        "monthly_charges": float(monthly),
        "total_charges": float(total)
    }

    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=data
    )

    result = response.json()

    st.write("Prediction:", result["meaning"])