
import os
import streamlit as st
import pandas as pd
import joblib


# Define the path for the model
folder_path = "tourism_project/model_deployment"
os.makedirs(folder_path, exist_ok=True)

# model file
my_model = xgb_model

# saving joblib file
model_path = os.path.join(folder_path, "model.joblib")
joblib.dump(my_model, model_path)

print(f"Model saved to {model_path}")

# Load the model
model_path = "tourism_project/model_deployment/model.joblib"
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
maritalstatus = st.selectbox("Marital Status", ["Single", "Divorced", "Married"])
passport = st.selectbox("Passport", [0, 1])
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
    "Gender" : gender,
    "Age" : age,
    "Marital Status" : maritalstatus,
    "Passport" : passport,
    "Occupation" : occupation,
    "Designation" : designation,
    "Monthly Income" : monthlyincome,
    "Own Car" : owncar,
    "City Tier" : citytier,
    "Preferred Property Star" : preferredpropertystar,
    "Number of Persons Visiting" : numberofpersonvisiting,
    "Number of Children Visiting" : numberofchildrenvisiting,
    "Type of Contact" : typeofcontact,
    "Number of Trips" : numberoftrips,
    "Duration of Pitch" : durationofpitch,
    "Number of Follow-ups" : numberoffollowups,
    "Product Pitched" : productpitched,
    "Pitch Satisfaction Score" : pitchsatisfactionscore
}])




# Predict button

if st.button("Tourism Package?"):
    prediction = model.predict(input_data)[0]
    st.subheader("Prediction Result:")

