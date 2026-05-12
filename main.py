import joblib
import numpy as np

from fastapi import FastAPI, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Seek A Nest AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

price_model = joblib.load("property_model.pkl")
encoders = joblib.load("encoders.pkl")


LOCALITY_DATA = {
    "Jagatpura": {
        "crime_score": 78,
        "locality_score": 88,
        "future_appreciation": "12-16%",
        "airport_distance": "7 km",
        "railway_distance": "13 km",
        "hospitals": 6,
        "gyms": 12,
        "schools": 8,
        "best_for": "students, investors and affordable buyers"
    },
    "Malviya Nagar": {
        "crime_score": 84,
        "locality_score": 91,
        "future_appreciation": "8-11%",
        "airport_distance": "3 km",
        "railway_distance": "9 km",
        "hospitals": 10,
        "gyms": 18,
        "schools": 14,
        "best_for": "families and working professionals"
    },
    "Mansarovar": {
        "crime_score": 80,
        "locality_score": 85,
        "future_appreciation": "7-10%",
        "airport_distance": "10 km",
        "railway_distance": "8 km",
        "hospitals": 8,
        "gyms": 15,
        "schools": 12,
        "best_for": "families and budget buyers"
    },
    "Vaishali Nagar": {
        "crime_score": 82,
        "locality_score": 87,
        "future_appreciation": "8-12%",
        "airport_distance": "13 km",
        "railway_distance": "7 km",
        "hospitals": 9,
        "gyms": 16,
        "schools": 11,
        "best_for": "renters, families and professionals"
    },
    "C-Scheme": {
        "crime_score": 86,
        "locality_score": 95,
        "future_appreciation": "6-9%",
        "airport_distance": "11 km",
        "railway_distance": "4 km",
        "hospitals": 12,
        "gyms": 20,
        "schools": 10,
        "best_for": "luxury buyers and premium investors"
    }
}


PROPERTY_DATABASE = [
    {"title": "Jagatpura 2 BHK Near Colleges", "location": "Jagatpura", "price": 3800000, "bhk": 2, "purpose": "Buy", "facilities": 8},
    {"title": "Jagatpura Student Rental", "location": "Jagatpura", "price": 12000, "bhk": 1, "purpose": "Rent", "facilities": 9},
    {"title": "Malviya Nagar 3 BHK", "location": "Malviya Nagar", "price": 8200000, "bhk": 3, "purpose": "Buy", "facilities": 9},
    {"title": "Mansarovar Family Apartment", "location": "Mansarovar", "price": 5500000, "bhk": 2, "purpose": "Buy", "facilities": 7},
    {"title": "Vaishali Nagar PG Room", "location": "Vaishali Nagar", "price": 8500, "bhk": 1, "purpose": "Rent", "facilities": 8},
]


@app.get("/")
def home():
    return {"message": "Seek A Nest AI backend is running."}


def safe_encode(column_name, value):
    encoder = encoders[column_name]

    if value not in encoder.classes_:
        value = encoder.classes_[0]

    return encoder.transform([value])[0]


def recommend_properties(location, budget, bedrooms, purpose, nearby_facilities):
    recommendations = []

    for prop in PROPERTY_DATABASE:
        score = 0

        if prop["location"] == location:
            score += 35

        if prop["purpose"] == purpose:
            score += 25

        if purpose == "Buy" and prop["price"] <= budget:
            score += 20

        if purpose == "Rent" and prop["price"] <= budget:
            score += 20

        if abs(prop["bhk"] - bedrooms) <= 1:
            score += 10

        if prop["facilities"] >= nearby_facilities - 1:
            score += 10

        recommendations.append({
            "title": prop["title"],
            "location": prop["location"],
            "price": prop["price"],
            "purpose": prop["purpose"],
            "match_score": score
        })

    recommendations.sort(key=lambda x: x["match_score"], reverse=True)
    return recommendations[:5]


def advisor_reply(question, location, price, locality):
    q = question.lower()

    if "investment" in q:
        return f"{location} has expected appreciation of {locality['future_appreciation']}. It can be a good investment if your holding period is 3-5 years."

    if "rent" in q:
        return f"{location} is suitable for rental demand, especially because it is best for {locality['best_for']}."

    if "safe" in q or "crime" in q:
        return f"The safety score for {location} is {locality['crime_score']}/100. Higher score means relatively safer locality."

    if "facility" in q or "hospital" in q or "gym" in q:
        return f"Nearby facilities include {locality['hospitals']} hospitals, {locality['gyms']} gyms and {locality['schools']} schools."

    if "future" in q or "growth" in q:
        return f"Future appreciation prediction for {location} is {locality['future_appreciation']}."

    return f"This property is estimated around ₹{int(price):,}. {location} is best for {locality['best_for']} with locality score {locality['locality_score']}/100."


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
    purpose: str = Form("Buy"),
    file: UploadFile = File(None)
):
    location_encoded = safe_encode("location", location)
    furnishing_encoded = safe_encode("furnishing", furnishing)

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

    estimated_price = float(price_model.predict(features)[0])

    locality = LOCALITY_DATA.get(location, LOCALITY_DATA["Jagatpura"])

    property_condition = "Good"
    investment_score = int(
        (locality["locality_score"] * 0.45)
        + (locality["crime_score"] * 0.25)
        + (nearby_facilities * 3)
    )

    estimated_monthly_rent = int((estimated_price * 0.025) / 12)

    similar_properties = recommend_properties(
        location=location,
        budget=estimated_price if purpose == "Buy" else estimated_monthly_rent,
        bedrooms=bedrooms,
        purpose=purpose,
        nearby_facilities=nearby_facilities
    )

    advisor_message = (
        f"This property in {location} is best suited for {locality['best_for']}. "
        f"Locality score is {locality['locality_score']}/100, safety score is {locality['crime_score']}/100, "
        f"and expected appreciation is {locality['future_appreciation']}."
    )

    return {
        "estimated_price": round(estimated_price, 2),
        "property_condition": property_condition,
        "investment_score": investment_score,
        "future_growth_prediction": locality["future_appreciation"],
        "ai_recommendation": advisor_message,
        "crime_score": locality["crime_score"],
        "locality_score": locality["locality_score"],
        "estimated_monthly_rent": estimated_monthly_rent,
        "nearby_facilities_data": {
            "airport_distance": locality["airport_distance"],
            "railway_distance": locality["railway_distance"],
            "hospitals": locality["hospitals"],
            "gyms": locality["gyms"],
            "schools": locality["schools"]
        },
        "similar_properties": similar_properties
    }


@app.post("/advisor")
def advisor(
    question: str = Form(...),
    location: str = Form(...),
    estimated_price: float = Form(...)
):
    locality = LOCALITY_DATA.get(location, LOCALITY_DATA["Jagatpura"])

    return {
        "reply": advisor_reply(
            question=question,
            location=location,
            price=estimated_price,
            locality=locality
        )
    }