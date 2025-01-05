import streamlit as st
from model_utils import load_model_from_github, predict_image
from tensorflow.keras.preprocessing import image
import numpy as np

# GitHub raw file link to the model (replace with your link)
MODEL_URL = "https://raw.githubusercontent.com/S-t-e-v-e-G/skincheck_ai_r_demo/main/demo_model_v1.h5"

# Load the model (download if needed)
model = load_model_from_github(MODEL_URL)

st.title("Skin Cancer Detection App")
st.write("Upload an image to get a prediction.")

# Image upload widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Load and preprocess the image
    img = image.load_img(uploaded_file, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Make predictions
    predictions = predict_image(model, img_array)
    st.write("Prediction Probabilities:", predictions)
    st.write(f"Predicted Class: {np.argmax(predictions)}")
