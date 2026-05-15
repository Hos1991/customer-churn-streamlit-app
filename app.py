import streamlit as st
import pandas as pd
import joblib

model = joblib.load("churn_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.title("Customer Churn Prediction App")

tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=1000.0)

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
payment_method = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

input_data = pd.DataFrame([{
    "tenure": tenure,
    "MonthlyCharges": monthly_charges,
    "TotalCharges": total_charges,
    "Contract": contract,
    "InternetService": internet_service,
    "PaymentMethod": payment_method
}])

input_encoded = pd.get_dummies(input_data)

input_encoded = input_encoded.reindex(columns=model_columns, fill_value=0)

if st.button("Predict Churn"):
    prediction = model.predict(input_encoded)[0]
    probability = model.predict_proba(input_encoded)[0][1]

    if prediction == 1:
        st.error(f"Customer is likely to churn. Probability: {probability:.2%}")
    else:
        st.success(f"Customer is likely to stay. Churn probability: {probability:.2%}")