
import os
import streamlit as st
import pandas as pd
import joblib

# Load the model committed by the pipeline (sits next to this file)
model_path = os.path.join(os.path.dirname(__file__), "model.joblib")
model = joblib.load(model_path)

# Streamlit app

st.title("Tourism Package Prediction")
st.write("""
This application predicts if a customer would sign-up for tourism package.
Please provide details for below characteristics to get a prediction.
""")

# User input

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=120, value=30)
passport = st.selectbox("Passport", [0, 1])
maritalstatus = st.selectbox("Marital Status", ["Single", "Divorced", "Married"])
occupation = st.selectbox("Occupation", ["Salaried", "Free Lancer", "Small Business", "Large Business"])
designation = st.selectbox("Designation", ["Manager", "Executive", "Senior Manager", "AVP", "VP"])
monthlyincome = st.number_input("Monthly Income", min_value=0, max_value=1000000, value=5000)
owncar = st.selectbox("Own Car", ["Yes", "No"])
citytier = st.selectbox("City Tier", [1, 2, 3])
preferredpropertystar = st.selectbox("Preferred Property Star", [3, 4, 5])
numberofpersonvisiting = st.number_input("Number of Person Visiting", min_value=1, max_value=100, value=2)
numberofchildrenvisiting = st.number_input("Number of Children Visiting", min_value=0, max_value=10, value=0)
typeofcontact = st.selectbox("Type of Contact", [ "Self Enquiry", "Company Invited"])
numberoftrips = st.number_input("Number of Trips", min_value=0, max_value=365, value=0)
durationofpitch = st.number_input("Duration of Pitch", min_value=1, max_value=30, value=15)
numberoffollowups = st.number_input("Number of Follow-ups", min_value=0, max_value=10, value=0)
productpitched = st.selectbox("Product Pitched", ["Deluxe", "Basic", "Standard", "Super Deluxe", "King"])
pitchsatisfactionscore = st.number_input("Pitch Satisfaction Score", min_value=1, max_value=5, value=3)


# Assemble input into dataframe
input_data = pd.DataFrame([{
    'gender' : Gender,
    'age' : Age,
    'passport' : Passport,
    'maritalstatus' : Marital Status,
    'occupation' : Occupation,
    'designation' : Designation,
    'monthlyincome' : Monthly Income,
    'owncar' : Own Car,
    'citytier' : City Tier,
    'preferredpropertystar' : Preferred Property Star,
    'numberofpersonvisiting' : Number of Person Visiting,
    'numberofchildrenvisiting' : Number of Children Visiting,
    'typeofcontact' : Type of Contact,
    'numberoftrips' : Number of Trips,
    'durationofpitch' : Duration of Pitch,
    'numberoffollowups' : Number of Follow-ups,
    'productpitched' : Product Pitched,
    'pitchsatisfactionscore' : Pitch Satisfaction Score
}])


# Predict button

if st.button("Tourism Package?"):
    prediction = model.predict(input_data)[0]
    st.subheader("Prediction Result:")

