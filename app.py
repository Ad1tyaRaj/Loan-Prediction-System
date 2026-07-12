import streamlit as st
import pandas as pd
import joblib

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Loan Prediction System",
    page_icon="🏦",
    layout="wide"
)

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load("Model/loan_model.pkl")

# =====================================================
# CONSTANT MESSAGE
# =====================================================

BANK_MESSAGE = """
⚠️ This input is outside the training dataset range.

Please consult your bank manager for manual evaluation.

This ML model is trained only on historical loan applications.
Predictions are most reliable within the training data range.
"""

# =====================================================
# VALIDATION FUNCTION
# =====================================================

def validate_input(
    no_of_dependents,
    income_annum,
    loan_amount,
    loan_term,
    cibil_score
):

    if no_of_dependents > 5:
        st.warning(BANK_MESSAGE)
        st.stop()

    if income_annum < 200000 or income_annum > 9900000:
        st.warning(BANK_MESSAGE)
        st.stop()

    if loan_amount < 300000 or loan_amount > 39500000:
        st.warning(BANK_MESSAGE)
        st.stop()

    if loan_term < 2 or loan_term > 20:
        st.warning(BANK_MESSAGE)
        st.stop()

    if cibil_score < 300 or cibil_score > 900:
        st.warning(BANK_MESSAGE)
        st.stop()

    # Business Rule
    if loan_amount > income_annum * 5:
        st.warning(
            "⚠️ Requested loan amount is very high compared to annual income.\n\n"
            "Please consult your bank manager."
        )
        st.stop()


# =====================================================
# DATAFRAME FUNCTION
# =====================================================

def create_dataframe(
    no_of_dependents,
    income_annum,
    loan_amount,
    loan_term,
    cibil_score
):

    return pd.DataFrame({

        "no_of_dependents":[no_of_dependents],
        "income_annum":[income_annum],
        "loan_amount":[loan_amount],
        "loan_term":[loan_term],
        "cibil_score":[cibil_score]

    })


# =====================================================
# PREDICTION FUNCTION
# =====================================================

def predict_loan(input_df):

    prediction = model.predict(input_df)

    probability = model.predict_proba(input_df)

    return prediction, probability

# =====================================================
# TITLE
# =====================================================

st.title("🏦 Loan Prediction System")
st.write("Machine Learning Based Loan Approval Prediction")

st.markdown("---")

st.markdown("""
### 📋 Fill Applicant Details

Enter the applicant information and click **Predict Loan Status**.

The model predicts whether the loan is likely to be **Approved** or **Rejected**.
""")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("📌 About Project")

st.sidebar.success("Machine Learning Project")

st.sidebar.write("""
### Model

- XGBoost Classifier

### Performance

- Accuracy : **98.75%**
- ROC-AUC : **0.995**

### Developed Using

- Python
- Pandas
- XGBoost
- Streamlit
""")

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader("📝 Applicant Information")

col1, col2 = st.columns(2)

with col1:

    no_of_dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        step=1
    )

    income_annum = st.number_input(
        "Annual Income (₹)",
        step=10000
    )

    loan_amount = st.number_input(
        "Loan Amount (₹)",
        step=50000
    )

with col2:

    loan_term = st.number_input(
        "Loan Term (Years)",
        step=1
    )

    cibil_score = st.number_input(
        "CIBIL Score",
        step=1
    )

st.markdown("---")

# =====================================================
# PREDICTION BUTTON
# =====================================================

if st.button("🔍 Predict Loan Status", use_container_width=True):

    # Validation
    validate_input(
        no_of_dependents,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score
    )

    # DataFrame
    input_df = create_dataframe(
        no_of_dependents,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score
    )

    # Prediction
    prediction, probability = predict_loan(input_df)

    result = prediction[0]

    confidence = probability[0][result] * 100

    approved_prob = probability[0][0] * 100
    rejected_prob = probability[0][1] * 100
    
    

    # =====================================================
    # RESULT
    # =====================================================

    st.subheader("📊 Prediction Result")

    if result == 0:

        st.success("✅ Loan Approved")

    else:

        st.error("❌ Loan Rejected")


    # =====================================================
    # CONFIDENCE
    # =====================================================

    st.metric(
        label="Model Confidence",
        value=f"{confidence:.2f}%"
    )

    st.progress(confidence / 100)


    # =====================================================
    # PROBABILITY
    # =====================================================

    st.subheader("📈 Prediction Probability")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Approved Probability",
            f"{approved_prob:.2f}%"
        )

    with col2:

        st.metric(
            "Rejected Probability",
            f"{rejected_prob:.2f}%"
        )

    st.markdown("---")


    # =====================================================
    # SIMPLE EXPLANATION
    # =====================================================

    st.subheader("🧠 Prediction Explanation")

    if result == 0:

        st.success("The model approved the application mainly because:")

        if cibil_score >= 700:
            st.write("✔ High CIBIL Score")

        if income_annum >= 500000:
            st.write("✔ Good Annual Income")

        if loan_amount <= income_annum * 3:
            st.write("✔ Reasonable Loan Amount")

        if no_of_dependents <= 3:
            st.write("✔ Moderate Number of Dependents")

    else:

        st.error("The model rejected the application mainly because:")

        if cibil_score < 650:
            st.write("✖ Low CIBIL Score")

        if loan_amount > income_annum * 3:
            st.write("✖ Loan Amount is high compared to Income")

        if income_annum < 300000:
            st.write("✖ Annual Income is low")

        if no_of_dependents > 3:
            st.write("✖ High Number of Dependents")


    st.markdown("---")


    # =====================================================
    # APPLICANT SUMMARY
    # =====================================================

    st.subheader("📋 Applicant Summary")

    summary = pd.DataFrame({

        "Feature":[
            "Dependents",
            "Annual Income",
            "Loan Amount",
            "Loan Term",
            "CIBIL Score"
        ],

        "Value":[
            no_of_dependents,
            f"₹ {income_annum:,}",
            f"₹ {loan_amount:,}",
            loan_term,
            cibil_score
        ]

    })

    st.table(summary)


    # =====================================================
    # INPUT DATA
    # =====================================================

    with st.expander("🔍 View Model Input"):

        st.dataframe(input_df)


    # =====================================================
    # DISCLAIMER
    # =====================================================

    st.markdown("---")

    st.caption("""
    ⚠️ Disclaimer

    This prediction is generated using an XGBoost Machine Learning model trained on historical loan application data.

    The result is intended for educational purposes only and should not replace a bank's official credit evaluation process.
    """)