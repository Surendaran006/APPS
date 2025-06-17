import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("HR_details.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Employee Retention Prediction")

# User input fields
satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5, step=0.01)
average_monthly_hours = st.number_input("Average Monthly Hours", min_value=50, max_value=350, value=200)
promotion_last_5years = st.selectbox("Got Promotion in Last 5 Years?", ["No", "Yes"])

# Convert input to numeric
promotion_val = 1 if promotion_last_5years == "Yes" else 0

# Prediction
if st.button("Predict"):
    input_df = pd.DataFrame([[satisfaction_level, average_monthly_hours, promotion_val]],
                        columns=['satisfaction_level', 'average_montly_hours', 'promotion_last_5years'])

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.success("✅ The worker will continue with the company.")
    else:
        st.error("❌ The worker will NOT continue with the company.")
