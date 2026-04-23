import streamlit as st
import requests

st.set_page_config(page_title="Churn Prediction App")

st.title("Customer Churn Prediction")

st.header("Enter Customer Details")

# Inputs (must match your model)
tenure = st.number_input("Tenure (months)", min_value=0, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=500.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=6000.0)

if st.button("Predict"):
    url = "http://localhost:8000/predict"  # change later for Render

    data = {
        "tenure": tenure,
        "monthly_charges": monthly_charges,
        "total_charges": total_charges
    }

    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            result = response.json()

            st.subheader(f"Prediction: {result['prediction']}")
            st.write(f"Churn Probability: {result['probability']}%")

            if result['prediction'] == "LEAVE":
                st.error("⚠️ High risk of churn")
            else:
                st.success("✅ Customer likely to stay")

        else:
            st.error("Error in API response")

    except Exception as e:
        st.error(f"Connection error: {e}")