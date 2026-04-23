import joblib
import numpy as np

# Load model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def predict(input_data):
    try:
        # Convert to numpy array
        input_array = np.array(input_data).reshape(1, -1)

        # Scale input
        input_scaled = scaler.transform(input_array)

        # Get probability
        prob = model.predict_proba(input_scaled)[0][1]

        # Decision logic
        if prob >= 0.5:
            status = "LEAVE"
        else:
            status = "STAY"

        return status, prob

    except Exception as e:
        return None, str(e)