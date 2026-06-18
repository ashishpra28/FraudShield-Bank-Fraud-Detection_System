# Import libraries
import streamlit as st
import requests
import joblib

# API 
API_URL = "http://127.0.0.1:8000/predict"

# Page configuration
st.set_page_config(
    page_title="Bank Fraud Detection",
    page_icon="🏦",
    layout="centered"
)

# Title
st.title("🏦 Bank Fraud Detection System")

st.markdown(
    "Enter transaction details to predict whether the transaction is Fraud or Not."
)

st.divider()

# Define user inputs    
hour = st.slider("Transaction Hour",min_value=0,max_value=23,value=12)
transaction_type = st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","CASH_IN","DEBIT"])
amount = st.number_input("Transaction Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Sender Balance",min_value=0.0,value=0.0)
newbalanceOrig = st.number_input("New Sender Balance",min_value=0.0,value=0.0)
oldbalanceDest = st.number_input("Old Receiver Balance",min_value=0.0,value=0.0)
newbalanceDest = st.number_input("New Receiver Balance",min_value=0.0, value=0.0)

# Prediction button 
if st.button("Predict Fraud"): 

    # Feature Engineering 
    balanceDiffOrig = oldbalanceOrg - newbalanceOrig
    balanceDiffDest = newbalanceDest - oldbalanceDest

    # Final input dataframe 
    input_data = {
        "hour":hour,
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest":newbalanceDest
    }

    st.divider() 
    st.subheader("Prediction Result")

    try:
        response = requests.post(API_URL,json=input_data)
        if response.status_code==200:
            result = response.json() 
            if result['prediction'] == 1:
                st.error(
                    f"⚠️ Potential Fraudulent Transaction Detected\n\n"
                    f"Fraud Probability: {result['fraud_probability']:.2%}"
                    )
            else:
                st.success(
                    f"✅ Legitimate Transaction\n\n"
                    f"Fraud Probability: {result['fraud_probability']:.2%}"
                )
            
            # Risk level 
            if result['fraud_probability'] >= 0.8:
                st.error("🔴 High Risk")
            elif result['fraud_probability'] >= 0.4:
                st.warning("🟠 Medium Risk")
            else:
                st.success("🟢 Low Risk")
        else: 
            st.error(f"API Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError: 
        st.error("Could not connect on the FastAPI server. Make sure it is connected on port 8000")



   
