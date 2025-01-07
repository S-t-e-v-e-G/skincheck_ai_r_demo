import streamlit as st
import pandas as pd

def skintrackr():
    # Load the scan data
    try:
        df = pd.read_csv("skin_scan_data.csv")
    except FileNotFoundError:
        st.error("No scan data found. Please make sure the CSV file exists.")
        return

    # Ensure 'Date' is in datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Create a new column 'Category' based on 'Recommended Action'
    def categorize_action(action):
        if 'malignant' in action.lower():
            return 'Malignant'
        elif 'benign' in action.lower():
            return 'Benign'
        else:
            return 'Unsure'

    df['Category'] = df['Recommended Action'].apply(categorize_action)

    # Group by month and category and count the number of scans
    monthly_counts = df.groupby([df['Date'].dt.to_period('M'), 'Category']).size().unstack(fill_value=0)

    # Convert period index to string format 'YYYY-MM'
    monthly_counts.index = monthly_counts.index.astype(str)

    # Add a total count column for each month
    monthly_counts['Total'] = monthly_counts.sum(axis=1)

    # Display the title
    st.write("### Scans per Month (Grouped by Category)")

    # Display the bar chart
    st.bar_chart(monthly_counts)


# Run the function
if __name__ == "__main__":
    skintrackr()
