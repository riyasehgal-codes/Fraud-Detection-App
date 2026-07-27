import streamlit as st 
import pandas as pd 
import joblib 

model = joblib.load( "fraud_detection_pipeline.pkl")
import joblib

# try:
#     model = joblib.load("fraud_detection_pipeline.pkl")
#     st.write("Model loaded successfully")
# except Exception as e:
#     st.error(e)

st.title(" Fraud Detection Prediction App")
st.markdown("Please enter the transaction details")

st.divider()

transactionType = st.selectbox( "Transaction Type", [ "PAYMENT", "TRANSFER", "CASH_OUT",  " DEPOSIT"])
amount = st.number_input( "Amount", min_value=0.0 , value = 1000.0)
oldbalanceOrg = st.number_input("Old Balance ( SENDER )", min_value=0.0 , value=10000.0)
newbalanceOrig = st.number_input("New Balance (SENDER)", min_value=0.0 , value =0.0 )
oldbalanceDest = st.number_input("Old Balance ( RECEIVER)", min_value=0.0, value = 0.0)
newbalanceDest = st.number_input( "New Balance (RECEIVER )", min_value=0.0, value=0.0)

if st.button("Predict") :
    input_data = pd.DataFrame( [ { 
        "type" : transactionType,
        "amount" : amount,
        "oldbalanceOrg" : oldbalanceOrg, 
        "newbalanceOrig" : newbalanceOrig,
        "oldbalanceDest" : oldbalanceDest,
        "newbalanceDest" : newbalanceDest
        }]) 
    
    prediction = model.predict(input_data)[0]
    if prediction == 1 : 
        prediction = "FRAUD"
    else : 
        prediction = "MOST LIKELY NOT A FRAUD"
    
    st.subheader( f"Prediction : {prediction}")
    
    if prediction == "FRAUD" : 
        st.error("this can be a FRAUD")
    else : 
        st.success("This transaction looks like it is not a fraud")