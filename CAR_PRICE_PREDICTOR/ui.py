import pickle
import numpy as np
import pandas as pd
import streamlit as st



pipe = pickle.load(open('model.pkl', "rb"))


df = pd.read_csv("Car details v3.csv")
st.set_page_config(page_title='Car Price Prediction',page_icon="🚘",layout="centered")
st.title("🚗 Car Price Prediction")
st.caption("Enter your car details to estimate its selling price.")
st.markdown("-----")

brand = ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel']

col1, col2 = st.columns(2)
with col1:
    st.subheader("🚘 Car Information")
    selected_brand = st.selectbox("Select Car Brand",brand)
    selected_fuel = st.radio("Select Fuel Type",df['fuel'].unique())
    selected_year = st.number_input("Enter Year",min_value=1994,max_value=2020,value=2000)
    selected_km = st.number_input("Kilometers Driven",min_value=1,max_value=2360000,value=10000)
    selected_transmission = st.selectbox("Select Transmission type",df['transmission'].unique())
    selected_seller = st.selectbox("Select Seller type",df['seller_type'].unique())
    

with col2:
    st.subheader("⚙️ Car Specifications")
    selected_owner = st.selectbox("Select Owner type",df['owner'].unique())
    selected_mileage_unit = st.radio("Select Mileage unit Type",['kmpl','km/kg'])
    selected_seats = st.number_input("Enter seats",min_value=2,max_value=10,value=5)
    selected_mileage = st.number_input("Enter Mileage",min_value=0,max_value=42,value=15)
    selected_capasity = st.number_input("Engine Capacity (CC)",min_value=625,max_value=3600,value=1000)
    selected_power = st.number_input("Maximum Power (BHP)",min_value=32,max_value=400,value=100)
    

if st.button("Predict Price", use_container_width=True):
       input_data = pd.DataFrame({
        'brand': [selected_brand],
        'year': [selected_year],
        'km_driven': [selected_km],
        'fuel': [selected_fuel],
        'seller_type': [selected_seller],
        'transmission': [selected_transmission],
        'owner': [selected_owner],
        'seats': [selected_seats],
        'mileage_value': [selected_mileage],
        'mileage_unit': [selected_mileage_unit],
        'engine_value': [selected_capasity],
        'max_power_value': [selected_power]
    })
       prediction = pipe.predict(input_data)
       st.subheader("💰 Estimated Car Price")
       st.metric("Estimated Selling Price",f"₹{prediction[0]:,.0f}")
    
