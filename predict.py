import joblib
import numpy as np

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def predict(features):
    X = np.array(features).reshape(1, -1)
    X_scaled = scaler.transform(X)

    prob = model.predict_proba(X_scaled)[0][1]
    pred = model.predict(X_scaled)[0]

    return pred, prob