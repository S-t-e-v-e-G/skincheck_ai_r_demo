import streamlit as st
from quickcheckr import quickcheckr
from home import home
from bodycheckr import bodycheckr
from skintrackr import skintrackr
from skindatar import skindatar

### Page Configuration ####
st.set_page_config(page_title="skincheck(ai)R",
                   layout="wide",
                   initial_sidebar_state="expanded",
                   page_icon="📖")

# Sidebar for module selection
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Select a function:",
    ["🏠 Home", "🧐 Quick Check", "🔎 Skin Check", "📊 Dashboard", "📋 Data Records"]
)

def main():
    if page == "🏠 Home":
       home()

    elif page == "🧐 Quick Check":
        quickcheckr()

    elif page == "🔎 Skin Check":
        bodycheckr()

    elif page == "📊 Dashboard":
        skintrackr()

    elif page == "📋 Data Records":  # Matching the page with the emoji
        skindatar()

if __name__ == "__main__":
    main()
