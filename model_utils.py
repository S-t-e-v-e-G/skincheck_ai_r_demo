import tensorflow as tf
import requests
import os
import numpy as np
import streamlit as st

def load_model_from_github(model_url):
    """Download and load the model from a public GitHub repo."""
    model_path = "https://raw.githubusercontent.com/S-t-e-v-e-G/skincheck_ai_r_demo/main/skincheckr-demo.keras"

    # Check if model already exists locally
    if not os.path.exists(model_path):
        st.info("Downloading model, please wait...")
        response = requests.get(model_url)
        with open(model_path, "wb") as file:
            file.write(response.content)
        st.success("Model downloaded successfully!")

    # Load the model
    model = tf.keras.models.load_model(model_path)
    return model

def predict_image(model, img_array):
    """Predict using the loaded model."""
    predictions = model.predict(img_array)
    return np.round(predictions * 100, 2)
