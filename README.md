# Customer Churn Prediction App

## 📌 Project Overview
This project predicts whether a customer will churn (leave a service) based on input features like tenure, monthly charges, and total charges.

The goal is to move a machine learning model from a local environment to a real-world production system using APIs and deployment.

---

## 🚀 Features
- Machine Learning model for churn prediction
- FastAPI backend for serving predictions
- Streamlit frontend for user interaction
- Live deployment on cloud
- Dockerfile included for containerization

---

## 🧠 Tech Stack
- Python
- FastAPI
- Streamlit
- Scikit-learn
- Joblib
- Uvicorn

---

## ⚙️ How to Run Locally

### 1. Start Backend API
```bash
python -m uvicorn main:app --reload