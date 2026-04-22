import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
df = pd.read_csv("churn.csv")

# Convert TotalCharges to numeric
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

# Drop missing values
df = df.dropna()

# Convert target column
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Select features (keep it simple)
X = df[['tenure', 'MonthlyCharges', 'TotalCharges']]
y = df['Churn']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Scale data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and scaler
joblib.dump(model, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model trained and saved successfully!")