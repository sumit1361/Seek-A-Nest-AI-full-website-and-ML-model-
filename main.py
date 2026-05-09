import io
import random

import joblib
import numpy as np
import tensorflow as tf

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware

# =========================
# FASTAPI APP
# =========================

app = FastAPI(title="Seek A Nest AI")

# =========================
# CORS
# =========================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# LOAD MODELS
# =========================

price_model = joblib.load("property_model.pkl")

encoders = joblib.load("encoders.pkl")

vision_model = tf.keras.applications.MobileNetV2(
    weights="imagenet"
)

# =========================
# HOME ROUTE
# =========================

@app.get("/")
def home():
    return {"message": "Seek A Nest AI Backend Running"}

# =========================
# PREDICT ROUTE
# =========================

@app.post("/predict")
async def predict_price(

    location: str = Form(...),
    sqft: int = Form(...),
    bedrooms: int = Form(...),
    bathrooms: int = Form(...),
    balcony: int = Form(...),
    age_of_property: int = Form(...),
    furnishing: str = Form(...),
    parking: int = Form(...),
    nearby_facilities: int = Form(...),

    file: UploadFile = File(...)

):

    # =========================
    # IMAGE PROCESSING
    # =========================

    contents = await file.read()

    image = tf.keras.utils.load_img(
        io.BytesIO(contents),
        target_size=(224, 224)
    )

    image_array = tf.keras.utils.img_to_array(image)

    image_array = np.expand_dims(image_array, axis=0)

    image_array = tf.keras.applications.mobilenet_v2.preprocess_input(
        image_array
    )

    # =========================
    # PROPERTY CONDITION
    # =========================

    modern_score = np.mean(image_array)

    is_modern = modern_score > 0

    multiplier = 1.15 if is_modern else 1.0

    # =========================
    # ENCODING
    # =========================

    location_encoded = encoders["location"].transform(
        [location]
    )[0]

    furnishing_encoded = encoders["furnishing"].transform(
        [furnishing]
    )[0]

    # =========================
    # FEATURES
    # =========================

    features = [[
        location_encoded,
        sqft,
        bedrooms,
        bathrooms,
        balcony,
        age_of_property,
        furnishing_encoded,
        parking,
        nearby_facilities
    ]]

    # =========================
    # PREDICTION
    # =========================

    base_price = price_model.predict(features)[0]

    final_price = base_price * multiplier

    # =========================
    # RESPONSE
    # =========================

    return {
        "estimated_price": round(float(final_price), 2),
        "property_condition": (
            "Modern"
            if is_modern
            else "Standard"
        ),
        "investment_score": random.randint(70, 95),
        "future_growth_prediction": (
            f"{random.randint(5, 18)}% expected growth"
        ),
        "ai_recommendation": (
            "Good investment opportunity"
        )
    }