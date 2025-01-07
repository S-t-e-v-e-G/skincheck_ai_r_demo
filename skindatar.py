import streamlit as st
import pandas as pd
import os

def skindatar():
    # Load  CSV
    #st.write("Current working directory:", os.getcwd())
    df = pd.read_csv('skin_scan_data.csv')

    # Display the DataFrame in the Streamlit app
    st.write(df)

if __name__ == "__main__":
    skindatar()
