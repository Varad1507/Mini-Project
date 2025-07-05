# train_model.py
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Remove spaces and NaNs
df = df[df['TotalCharges'] != ' ']
df['TotalCharges'] = df['TotalCharges'].astype(float)
df.dropna(inplace=True)

# Drop customerID
df.drop(['customerID'], axis=1, inplace=True)

# Encode target
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

# Split features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# One-hot encode
X_encoded = pd.get_dummies(X)

# Save column order
joblib.dump(X_encoded.columns.tolist(), 'model_features.pkl')

# Train model
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'telco_churn_model.pkl')

print("Model trained and saved successfully.")
