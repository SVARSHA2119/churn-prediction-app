from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

app = FastAPI()

class Customer(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/predict")
def get_prediction(data: Customer):
    features = [
        data.tenure,
        data.monthly_charges,
        data.total_charges
    ]
    
    result = predict(features)

    return {
        "prediction": result,
        "meaning": "Customer will leave" if result == 1 else "Customer will stay"
    }