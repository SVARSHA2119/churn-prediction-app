from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Input schema
class CustomerData(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float

# Health check
@app.get("/health")
def health():
    return {"status": "OK"}

# Prediction endpoint
@app.post("/predict")
def predict(data: CustomerData):
    input_data = np.array([[data.tenure, data.monthly_charges, data.total_charges]])

    # Scale
    input_scaled = scaler.transform(input_data)

    # Predict
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)[0][1]

    # Label
    if prediction[0] == 0:
        result = "Customer will stay"
    else:
        result = "Customer will churn"

    return {
        "prediction": int(prediction[0]),
        "result": result,
        "probability": float(probability)
    }