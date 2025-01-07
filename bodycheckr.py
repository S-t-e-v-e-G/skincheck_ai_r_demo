import streamlit as st
from model_utils import load_model_from_github, predict_image
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import pandas as pd
from datetime import datetime
import os

# Function to determine recommended action
def recommended_action(malignant, benign):
    if 25 <= malignant <= 45:
        return "Unsure - Advise Check Up", "orange"
    elif 46 <= malignant <= 65:
        return "Likely Malignant - Seek Professional Care", "red"
    elif 66 <= malignant <= 100:
        return "Highly Likely Malignant - Seek Professional Care Urgently", "darkred"
    else:
        return "Likely Benign - No Action Needed", "green"

def bodycheckr():
    # Load the model
    MODEL_URL = "https://raw.githubusercontent.com/S-t-e-v-e-G/skincheck_ai_r_demo/main/skincheckr-demo.keras"
    model = load_model_from_github(MODEL_URL)

    st.title("🔎 Body Check - Score, Screen & Record")
    st.write("Upload or capture an image to get a prediction.")
    st.write("Results are stored enabling you to track your health over time.")

    st.write("---")

    # Capture metadata
    st.subheader("Scan Metadata")

    # Dropdown for lesion location
    location = st.selectbox("Select Lesion Location", ["Face", "Arm", "Leg", "Torso", "Other"])

    # Input for user metadata
    date = st.text_input("Enter the Date (YYYY-MM-DD)", value=datetime.today().strftime("%Y-%m-%d"))
    notes = st.text_input("Enter Notes/Comments")

    # Image upload widget
    option = st.radio("Select an option", ("Upload a photo", "Take a photo"))

    uploaded_file = None
    if option == "Upload a photo":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    elif option == "Take a photo":
        uploaded_file = st.camera_input("Capture a photo")

    if uploaded_file:
        # Load the original image
        original_img = Image.open(uploaded_file)

        # Ensure image is in RGB mode (removes alpha channel if present)
        if original_img.mode != "RGB":
            original_img = original_img.convert("RGB")

        # Display the original image
        st.image(original_img, caption="📸 Image Submitted", width=300)

        # Preprocess for the model (resize and normalize)
        model_input_img = original_img.resize((56, 56))
        img_array = image.img_to_array(model_input_img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize

        # Make predictions
        predictions = predict_image(model, img_array)

        # Display results
        nevus = round(predictions[0][0])
        melanoma = round(predictions[0][1])
        bcc = round(predictions[0][2])
        malignant = melanoma + bcc

        # Get the recommended action
        action, color = recommended_action(malignant, nevus)

        # Display the recommended action with color
        st.markdown("---")
        st.write("Recommended Action:")
        st.markdown(f"<h3 style='color:{color};'>{action}</h3>", unsafe_allow_html=True)
        st.markdown("---")

        # Columns to display icons or additional information
        st.write("Detected Probabilities:")
        columns = st.columns(3)
        columns[0].markdown(f"**Benign**")
        columns[0].write(f"**Nevus:** {nevus}%")
        columns[1].markdown(f"**Critical**", unsafe_allow_html=True)
        columns[1].markdown(f"<span style='color: red;'>{melanoma}% - Melanoma</span>", unsafe_allow_html=True)
        columns[2].markdown(f"**Urgent Care**", unsafe_allow_html=True)
        columns[2].markdown(f"<span style='color: orange;'>{bcc}% - BCC/SCC</span>", unsafe_allow_html=True)

        # Horizontal separator
        st.markdown("---")
        st.write("Detailed Breakdown:")

        # Prepare data
        classification_data = {
            "Type": ["Nevus", "Melanoma", "BCC/SCC"],
            "Probability (%)": [nevus, melanoma, bcc],
            "Description": [
                "A common mole or birthmark. Generally harmless.",
                "A malignant tumor requiring urgent medical attention.",
                "A locally invasive cancer requiring immediate care."
            ]
        }
        df = pd.DataFrame(classification_data)

        # Style and render the table
        st.markdown(
            """
            <style>
                table {
                    border-collapse: collapse;
                    width: 100%;
                    border: 1px solid black;
                    color: black;
                }
                th, td {
                    padding: 10px;
                    text-align: left;
                    border-bottom: 1px solid black;
                }
                th {
                    background-color: black;
                    color: white;
                }
                tr:hover {background-color: #f5f5f5;}
            </style>
            """,
            unsafe_allow_html=True
        )

        # Display the table without index
        st.table(df)



        # Prepare data to save
        scan_data = {
            "Date": date,
            "Location": location,
            "Notes": notes,
            "% Benign": nevus,
            "% Malignant": malignant,
            "Recommended Action": action
        }

        # Create a DataFrame from the collected data
        df = pd.DataFrame([scan_data])

        # Get the current working directory
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Save path for the CSV file
        file_path = os.path.join(current_directory, "skin_scan_data.csv")

        # Save to a CSV file
        try:
            # If the file exists, append data; otherwise, create the file with headers
            df.to_csv(file_path, mode="a", header=not os.path.exists(file_path), index=False)
            st.success(f"Scan recorded successfully! Data saved to {file_path}")
        except Exception as e:
            st.error(f"Error saving data: {e}")

if __name__ == "__main__":
    bodycheckr()
