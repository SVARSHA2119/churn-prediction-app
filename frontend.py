import streamlit as st
import requests

API_URL = "https://churn-prediction-app-i4x9.onrender.com/predict"

st.title("Customer Churn Prediction App")

tenure = st.number_input("Tenure", 0, 100, 12)
monthly = st.number_input("Monthly Charges", 0.0, 1000.0, 500.0)
total = st.number_input("Total Charges", 0.0, 10000.0, 6000.0)

if st.button("Predict"):

    payload = {
        "tenure": tenure,
        "monthly_charges": monthly,
        "total_charges": total
    }

    try:
        res = requests.post(API_URL, json=payload)

        if res.status_code == 200:
            data = res.json()
            st.success(f"Prediction: {data['prediction']}")
            st.info(f"Probability: {data['probability']}%")
        else:
            st.error(res.text)

    except Exception as e:
        st.error(f"Error: {e}")