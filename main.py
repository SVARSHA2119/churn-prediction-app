@app.post("/predict")
def get_prediction(data: Customer):
    features = [
        data.tenure,
        data.monthly_charges,
        data.total_charges
    ]
    
    status, prob = predict(features)

    return {
        "prediction": status,
        "probability": round(prob * 100, 2),
        "meaning": "Customer will leave" if status == "LEAVE" else "Customer will stay"
    }