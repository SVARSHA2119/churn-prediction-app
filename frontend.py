import streamlit as st
from main import predict

st.set_page_config(page_title="Churn Prediction App")

st.title("Customer Churn Prediction")

st.header("Enter Customer Details")

# ONLY 3 inputs (must match training)
tenure = st.number_input("Tenure (months)", min_value=0, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=500.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=6000.0)

if st.button("Predict"):

    input_data = [
        tenure,
        monthly_charges,
        total_charges
    ]

    status, prob = predict(input_data)

    if status is not None:
        st.subheader(f"Prediction: {status}")
        st.write(f"Churn Probability: {prob * 100:.2f}%")

        if status == "LEAVE":
            st.error("⚠️ High risk of churn")
        else:
            st.success("✅ Customer likely to stay")

    else:
        st.error(f"Error: {prob}")