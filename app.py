 

import streamlit as st
import joblib
import numpy as np

model = joblib.load("nltk.pkl")

st.title("Spam Detection App")

text = st.text_input("Enter message received")


if st.button("Predict"):

    features = np.array([[text]])

    prediction = model.predict(features)

    st.success(f"Prediction: {prediction[0]}")
    
