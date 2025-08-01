import random
import string
import streamlit as st

import streamlit as st
import pandas as pd
import joblib
import sklearn


# Load the model
model = joblib.load('bank_account_model.pkl')

# Title
st.title("Bank Account Prediction App")
st.write("Fill in the details to check the likelihood of having a bank account.")

# Form inputs
country = st.selectbox("Country", ['Kenya', 'Rwanda', 'Tanzania', 'Uganda'])
location_type = st.selectbox("Location Type", ['Rural', 'Urban'])
cellphone_access = st.selectbox("Cellphone Access", ['Yes', 'No'])
household_size = st.number_input("Household Size", min_value=1, max_value=50, value=3)
age_of_respondent = st.number_input("Age of Respondent", min_value=15, max_value=100, value=30)
gender = st.selectbox("Gender", ['Male', 'Female'])
relationship = st.selectbox("Relationship with Head", ['Head of Household', 'Spouse', 'Child', 'Other relative', 'Other non-relatives'])
marital_status = st.selectbox("Marital Status", ['Married/Living together', 'Single/Never Married', 'Divorced/Separated', 'Widowed'])
education = st.selectbox("Education Level", ['No formal education', 'Primary education', 'Secondary education', 'Tertiary education', 'Other/DK'])
job_type = st.selectbox("Job Type", ['Self employed', 'Government Dependent', 'Formally employed Private', 'Formally employed Government',
                                     'Informally employed', 'Farming and Fishing', 'Remittance Dependent', 'Other Income', 'No Income'])

# On button click
if st.button("Validate"):
    # Create a DataFrame from input
    input_df = pd.DataFrame({
        'country': [country],
        'location_type': [location_type],
        'cellphone_access': [cellphone_access],
        'household_size': [household_size],
        'age_of_respondent': [age_of_respondent],
        'gender_of_respondent': [gender],
        'relationship_with_head': [relationship],
        'marital_status': [marital_status],
        'education_level': [education],
        'job_type': [job_type]
    })

    # Encode input the same way you trained
    input_encoded = pd.get_dummies(input_df)

    # Align input with model features
    model_features = model.feature_names_in_
    for col in model_features:
        if col not in input_encoded.columns:
            input_encoded[col] = 0
    input_encoded = input_encoded[model_features]

    # Make prediction
    prediction = model.predict(input_encoded)[0]

    # Display result
    if prediction == 1:
        st.success("Prediction: ✅ Likely to have a bank account")
    else:
        st.warning("Prediction: ❌ Unlikely to have a bank account")
