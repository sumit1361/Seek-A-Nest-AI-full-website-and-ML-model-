import numpy as np
import joblib
from fastapi import FastAPI, UploadFile, File, Form
import io

# We only import tensorflow. This is the most compatible way.
import tensorflow as tf

app = FastAPI()

# Accessing models via the tf.keras namespace
# This tells VS Code exactly where to look within the tensorflow folder
vision_model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Load your local ML model
try:
    price_model = joblib.load('property_model.pkl')
except Exception as e:
    print(f"Model Load Error: {e}")

@app.post("/predict")
async def estimate_price(sqft: int = Form(...), beds: int = Form(...), file: UploadFile = File(...)):
    # 1. Process Image
    contents = await file.read()
    
    # Using tf.keras.utils instead of standalone keras
    img = tf.keras.utils.load_img(io.BytesIO(contents), target_size=(224, 224))
    x = tf.keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    
    # Preprocess using the mobilenet_v2 specific scaler
    x = tf.keras.applications.mobilenet_v2.preprocess_input(x)
    
    # 2. Logic for "Modern" check
    is_modern = np.mean(x) > 0 
    multiplier = 1.20 if is_modern else 1.0
    
    # 3. ML Price Prediction
    base_price = price_model.predict([[sqft, beds]])[0]
    final_price = base_price * multiplier
    
    return {
        "final_valuation": round(float(final_price), 2),
        "condition": "Modern" if is_modern else "Standard",
        "adjustment": multiplier
    }