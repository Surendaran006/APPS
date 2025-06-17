import streamlit as st
import pandas as pd
import pickle

# Load model
with open('HR_details.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("HR Salary Prediction App")

st.markdown("""
This app predicts whether the **employee will continue** with the company or not based on:
- Satisfaction level
- Average monthly hours
- Whether they got promotion in the last 5 years
""")

# Input fields
satisfaction = st.slider("Satisfaction Level", 0.0, 1.0, 0.5, step=0.01)
hours = st.number_input("Average Monthly Hours", min_value=50, max_value=350, value=160)
promotion = st.selectbox("Got Promotion in Last 5 Years?", ['No', 'Yes'])

# Convert to numeric
promotion_val = 1 if promotion == 'Yes' else 0

# Predict
if st.button("Predict"):
    input_data = pd.DataFrame([[satisfaction, hours, promotion_val]],
                              columns=['satisfaction_level', 'average_monthly_hours', 'promotion_last_5years'])
    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.error("❌ The worker will NOT continue with the company.")
    else:
        st.success("✅ The worker WILL continue with the company.")
