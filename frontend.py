import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦Loan Approval Predictor")
st.markdown("Fill in the applicant details below.")

col1, col2 = st.columns(2)

with col1:

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["Yes", "No"]
    )

    cibil_score = st.slider(
        "CIBIL Score",
        min_value=300,
        max_value=900,
        value=750
    )

    loan_term = st.slider(
        "Loan Term (Months)",
        min_value=1,
        max_value=30,
        value=12
    )

with col2:

    income_annum = st.number_input(
        "Annual Income",
        min_value=1,
        value=500000
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=1,
        value=1000000
    )

    residential_assets_value = st.number_input(
        "Residential Assets Value",
        min_value=0,
        value=0
    )

    commercial_assets_value = st.number_input(
        "Commercial Assets Value",
        min_value=0,
        value=0
    )

    luxury_assets_value = st.number_input(
        "Luxury Assets Value",
        min_value=0,
        value=0
    )

    bank_asset_value = st.number_input(
        "Bank Asset Value",
        min_value=0,
        value=0
    )

st.divider()

if st.button("Predict Loan Approval", use_container_width=True):

    payload = {
        "education": education,
        "self_employed": self_employed,
        "income_annum": int(income_annum),
        "loan_amount": int(loan_amount),
        "loan_term": int(loan_term),
        "cibil_score": int(cibil_score),
        "residential_assets_value": int(residential_assets_value),
        "commercial_assets_value": int(commercial_assets_value),
        "luxury_assets_value": int(luxury_assets_value),
        "bank_asset_value": int(bank_asset_value)
    }

    try:
        response = requests.post(
            API_URL,
            json=payload
        )

        if response.status_code == 200:

            prediction = response.json()["prediction_category"]

            if prediction == "Approved":
                st.success("Loan Approved")
                st.balloons()

            else:
                st.error("Loan Rejected")

        else:
            st.error("Failed to get prediction from FastAPI")

    except Exception as e:
        st.error(f"Connection Error: {e}")