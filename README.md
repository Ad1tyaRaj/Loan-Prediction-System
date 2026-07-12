# 🏦 Loan Prediction System

A Machine Learning web application that predicts whether a loan application is likely to be **Approved** or **Rejected** using an **XGBoost Classifier**. The application is built with **Streamlit** and includes business-rule validation for reliable predictions.

---

## 🚀 Live Demo

🔗 **Live App:** *(Add your Streamlit Cloud link here after deployment)*

Example:
```
https://your-app-name.streamlit.app
```

---

## 📌 Project Overview

Financial institutions receive thousands of loan applications every day. This project uses Machine Learning to assist in the loan approval process by analyzing applicant information and predicting loan eligibility.

The application provides:

- ✅ Loan Approval Prediction
- 📊 Prediction Confidence Score
- 📈 Approval & Rejection Probability
- ⚠️ Business Rule Validation
- 📋 Applicant Summary

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- XGBoost
- Scikit-learn
- Streamlit
- Joblib

---

## 📂 Project Structure

```
Loan-Prediction-System/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── model/
      └── loan_model.pkl
```

---

## 🎯 Input Features

| Feature | Description |
|---------|-------------|
| Number of Dependents | Total dependents of applicant |
| Annual Income | Applicant's yearly income |
| Loan Amount | Requested loan amount |
| Loan Term | Loan duration |
| CIBIL Score | Applicant credit score |

---

## 🤖 Machine Learning Model

**Algorithm Used**

- XGBoost Classifier

### Model Performance

| Metric | Score |
|---------|--------|
| Accuracy | **98.75%** |
| ROC-AUC Score | **0.995** |

---

## ⚠ Business Validation Rules

The application validates user input before making predictions.

Examples include:

- Dependents should not exceed 5.
- Annual income should be within the training data range.
- Loan amount should be within the training data range.
- Loan term should be within the supported range.
- Loan amount should not be unrealistically high compared to annual income.

If any validation fails, the application advises the user to consult a bank manager instead of making an unreliable prediction.

---

## 💻 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Loan-Prediction-System.git
```

Go to project folder

```bash
cd Loan-Prediction-System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

### Home Page

*(Add Screenshot Here)*

### Prediction Result

*(Add Screenshot Here)*

---

## 🔮 Future Improvements

- User Authentication
- Database Integration
- Model Explainability (SHAP)
- Loan EMI Calculator
- PDF Report Generation
- Cloud Deployment with CI/CD

---

## 👨‍💻 Author

**Aditya Raj**

GitHub:
https://github.com/AD1TYARAJ

Portfolio:
https://ad1tyaraj.github.io/Portfolio/

LinkedIn:
*(Add your LinkedIn profile)*

---

## ⭐ If you found this project useful, consider giving it a Star!
