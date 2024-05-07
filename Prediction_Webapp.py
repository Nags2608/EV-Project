# -*- coding: utf-8 -*-
"""
Created on Mon May  6 17:42:13 2024

@author: supre
"""


import numpy as np
import pickle
import streamlit as st  # Added import statement for Streamlit
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

loaded_model = pickle.load(open('C:/Users/supre/Downloads/ss/trained_model.sav', 'rb'))

# Creating a function for prediction
def prediction(input_data):
    # Changing the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    # Make prediction
    prediction = loaded_model.predict(input_data_reshaped)
    # Display the prediction
    if prediction[0] == 0:
        return 'The predicted Vehicle type is Battery Electric Vehicle'
    else:
        return 'The predicted Vehicle type is Plug-in Hybrid Electric Vehicle'

def main():
    # Giving a title
    st.title('EV Prediction Web App')
    Postal_code = st.text_input("Postal Code")
    Model_year = st.text_input("Model Year")
    Make = st.text_input("Make")
    Model = st.text_input("Model")
    Electric_range = st.text_input("Electric Range")
    Base_MSRP = st.text_input("Base MSRP")
    # Code for Prediction
    EV_type = ''
    # Creating a button for Prediction
    if st.button('Electric Vehicle Type:'):
        EV_type = prediction([Postal_code, Model_year, Make, Model, Electric_range, Base_MSRP])
    st.success(EV_type)

if __name__ == '__main__':
    main()
