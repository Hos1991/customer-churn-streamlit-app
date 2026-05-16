# 📉 Customer Churn Prediction Dashboard

## 📌 Project Overview
This project predicts customer churn using machine learning and an interactive Streamlit dashboard.

The application allows users to input customer information and receive:
- Churn prediction
- Churn probability score

The goal is to help businesses identify customers at risk of leaving.

---

## 📊 Dataset
- Dataset: Telco Customer Churn Dataset
- Problem Type: Classification
- Target Variable: Churn

---

## 🔍 Project Workflow
- Data cleaning
- Handling missing values
- Encoding categorical variables
- Train/Test split
- XGBoost classification model
- Probability prediction
- Streamlit dashboard deployment

---

## ⚙️ Features Used
- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Internet Service
- Payment Method

---

## 🤖 Model Used
XGBoost Classifier

---

## 📈 Model Performance

Classification Report:

Precision, recall, and F1-score showed strong performance for customer retention prediction.

Key observation:
- Customers with month-to-month contracts showed higher churn probability.
- Long-term contracts reduced churn significantly.
- Fiber optic customers tended to churn more frequently.

---

## 🚀 Streamlit Dashboard
The dashboard allows users to:
- Enter customer information
- Predict churn status
- View churn probability

Example outputs:
- "Customer is likely to churn"
- "Customer is likely to stay"

---

## 🧠 Business Value
This application can help businesses:
- Identify high-risk customers
- Improve retention strategies
- Reduce customer loss
- Support marketing decision-making

---

## 🛠️ Technologies Used
- Python
- Pandas
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

## ▶️ How to Run

### 1. Clone the repository
git clone <repo-link>

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run Streamlit app
streamlit run app.py

---

## 📂 Project Structure

customer-churn-streamlit-app/
│
├── app.py
├── churn_model.pkl
├── model_columns.pkl
├── requirements.txt
└── README.md

---

## 👨‍💻 Author
Hossein Fathi
