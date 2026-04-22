import joblib
import numpy as np

# Load saved files
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

def predict(data):
    # Convert input to array
    data = np.array(data).reshape(1, -1)
    
    # Apply same scaling
    data = scaler.transform(data)
    
    # Predict
    prediction = model.predict(data)
    
    return int(prediction[0])