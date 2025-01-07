import streamlit as st

def home():

    st.markdown("<h1 style='text-align: center;'>📸 SKINCHECK (ai) R</h1>", unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)


    st.markdown("<h2 style='text-align: center;'>SCAN. SCREEN. STOP.</h2>", unsafe_allow_html=True)


    st.markdown("<br><br>", unsafe_allow_html=True)

    st.write("---")
    st.markdown("<p style='text-align: center; font-size: 20px;'>SKINCHECKR uses data science to help stop the impact of skin cancer.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>Upload an image, scan and monitor your skin health.</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>This is a demo of a project created as part of Le Wagon Tokyo Data Science & AI Bootcamp.</p>", unsafe_allow_html=True)
    st.markdown(
    "<p style='text-align: center; font-size: 20px;'>See the following link for further details: "
    "<a href='https://github.com/S-t-e-v-e-G/skincheck_ai_r_demo/blob/40250065f1869ad65af4827270f4c9a63ed3e337/Skincheck-ai-r%20Demo.pdf' target='_blank'>Project Showcase</a></p>",
    unsafe_allow_html=True)
    st.write("---")

    st.markdown(
        "<p style='text-align: center; font-size: 15px; font-style: italic;'>"
        "The information and recommendations provided by this app are for informational purposes only and are not intended to replace professional medical advice, diagnosis, or treatment. "
        "The predictions and suggested actions are based on machine learning algorithms and image analysis, which are not infallible and should not be used as a sole basis for medical decisions. "
        "Always consult with a qualified healthcare professional for concerns related to your health or any potential medical conditions."
        "</p>",
        unsafe_allow_html=True)


if __name__ == "__main__":
    home()
