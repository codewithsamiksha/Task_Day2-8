import streamlit as st
import pandas as pd
import joblib

# Load files
model = joblib.load("models/ford_car.pkl")
scaler = joblib.load("models/scaler.pkl")
columns = joblib.load("models/columns.pkl")

#congiguring the streamlit pages
st.set_page_config(page_title="Ford Car Price Predictor", layout="centered")

#display title & description
st.title("🚗 Ford Car Price Prediction")
st.write("Enter the car details below to predict the price.")

#Numerical input field
year = st.number_input(
    "Year",
    min_value=1990,
    max_value=2025,
    value=2018
)

mileage = st.number_input(
    "Mileage(in km)",
    min_value=0,
    max_value=300000,
    value=10000
)


mpg = st.number_input(
   "Miles per Gallon(mpg)",
   min_value=0,
   max_value=100,
   value=55
)

engineSize = st.number_input(
    "Engine Size",
    min_value=0,
    max_value=5,
    value=1
)
#Dropdown Selection of transmission
transmission = st.selectbox(
    "Select Transmission type",
    [
        "Automatic",
        "Manual",
        "Semi-Auto"
    ]
)
#Dropdown Selection of fueltype
fuelType = st.selectbox(
    "Select fuel Type",
    [
        "Petrol",
        "Diesel",
        "Hybrid",
        "Electric",
        "Other"
    ]
)

#text input
model_name = st.text_input("Model","Focus")

#predict button
if st.button("Predict Price"): 

#creating input dataframe    
    input_df = pd.DataFrame({
        "year" : [year],
        "model" : [model_name],
        "Transmission" : [transmission],
        "mileage" : [mileage],
        "fuelType" : [fuelType],
        # "tax" : [tax],
        "mpg" : [mpg],
        "engineSize" : [engineSize]    
    })
# Display entered values.
    st.subheader("Entered Car Details")
    st.table(input_df)

        # Perform One-Hot Encoding.
    input_df_encoded = pd.get_dummies(input_df)

        # Match training columns.
    input_df_encoded = input_df_encoded.reindex(
        columns = columns,
        fill_value=0
        )

        # Scale numerical columns.
    numeric_col = ["year", "mileage",  "mpg", "engineSize"]
    input_df_encoded[numeric_col] = scaler.transform(
            input_df_encoded[numeric_col]
        )

        # Predict price.
    prediction = model.predict(input_df_encoded)

        # Display predicted price.
    st.subheader("Predicted Price")
    st.success(f"£ {prediction[0]:,.2f}")
