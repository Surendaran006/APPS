# streamlit_app.py

import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("HR_details.pkl", "rb") as f:
    model = pickle.load(f)

# App title
st.title("HR Salary Category Predictor")

# User input
satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
average_monthly_hours = st.number_input("Average Monthly Hours", min_value=0, max_value=500, value=160)
promotion_last_5years = st.selectbox("Promotion in Last 5 Years", [0, 1])

# Predict
if st.button("Predict Salary Category"):
    input_data = pd.DataFrame([[satisfaction_level, average_monthly_hours, promotion_last_5years]],
                              columns=['satisfaction_level', 'average_monthly_hours', 'promotion_last_5years'])
    prediction = model.predict(input_data)

    salary_classes = ['low', 'medium', 'high']  # Update based on your LabelEncoder classes
    st.success(f"Predicted Salary Category: {salary_classes[int(prediction[0])]}")

