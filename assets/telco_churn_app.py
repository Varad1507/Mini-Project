# telco_churn_app.py
import streamlit as st
import pandas as pd
import joblib

# Load model and column order
model = joblib.load("telco_churn_model.pkl")
model_features = joblib.load("model_features.pkl")

st.title("📊 Telco Customer Churn Prediction")

# Collect inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Has Partner?", ["Yes", "No"])
dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.number_input("Tenure (in months)", 0, 72)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
monthly_charges = st.number_input("Monthly Charges", 0.0)
total_charges = st.number_input("Total Charges", 0.0)

# Prepare input
input_dict = {
    "gender": gender,
    "SeniorCitizen": senior_citizen,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone_service,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges
}
input_df = pd.DataFrame([input_dict])
input_encoded = pd.get_dummies(input_df)

# Add missing columns
for col in model_features:
    if col not in input_encoded:
        input_encoded[col] = 0

# Reorder
input_encoded = input_encoded[model_features]

# Predict
if st.button("Predict Churn"):
    pred = model.predict(input_encoded)[0]
    proba = model.predict_proba(input_encoded)[0][pred]

    if pred == 1:
        st.error(f"❌ This customer is likely to churn (Confidence: {proba:.2f})")
    else:
        st.success(f"✅ This customer is not likely to churn (Confidence: {proba:.2f})")
