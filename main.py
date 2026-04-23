from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

# Initialize FastAPI app (MUST be at top)
app = FastAPI()

# Request body structure
class Customer(BaseModel):
    tenure: int
    monthly_charges: float
    total_charges: float


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "OK"}


# Prediction endpoint
@app.post("/predict")
def get_prediction(data: Customer):

    # Prepare features in correct order (same as training)
    features = [
        data.tenure,
        data.monthly_charges,
        data.total_charges
    ]

    # Get prediction from model
    result, prob = predict(features)

    # Convert result to readable label
    status = "LEAVE" if result == 1 else "STAY"

    return {
        "prediction": status,
        "probability": round(prob * 100, 2),
        "meaning": "Customer will leave" if result == 1 else "Customer will stay"
    }