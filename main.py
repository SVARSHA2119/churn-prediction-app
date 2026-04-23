from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS FIX (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Customer(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float

@app.get("/")
def home():
    return {"status": "API running"}

@app.post("/predict")
def predict_churn(data: Customer):

    features = [
        data.tenure,
        data.monthly_charges,
        data.total_charges
    ]

    pred, prob = predict(features)

    return {
        "prediction": "LEAVE" if pred == 1 else "STAY",
        "probability": round(prob * 100, 2)
    }