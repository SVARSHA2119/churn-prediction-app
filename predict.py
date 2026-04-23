import joblib
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def predict(features):
    input_array = np.array(features).reshape(1, -1)
    input_scaled = scaler.transform(input_array)

    prob = model.predict_proba(input_scaled)[0][1]

    if prob >= 0.5:
        status = "LEAVE"
    else:
        status = "STAY"

    return status, prob