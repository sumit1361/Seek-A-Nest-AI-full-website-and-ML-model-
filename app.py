import streamlit as st
import requests

st.set_page_config(page_title="Real Estate AI", layout="centered")
st.title("🏠 AI Property Valuator")

sqft = st.number_input("Square Footage", 500, 5000, 1500)
beds = st.slider("Bedrooms", 1, 5, 2)
img_file = st.file_uploader("Upload Property Image", type=['jpg', 'png'])

if st.button("Calculate Value"):
    if img_file:
        files = {"file": img_file.getvalue()}
        data = {"sqft": sqft, "beds": beds}
        res = requests.post("http://127.0.0.1:8000/predict", data=data, files=files).json()
        
        st.success(f"Estimated Value: ${res['final_valuation']:,}")
        st.write(f"Detected Condition: **{res['condition']}** ({res['adjustment']}x multiplier)")
    else:
        st.warning("Please upload a photo.")