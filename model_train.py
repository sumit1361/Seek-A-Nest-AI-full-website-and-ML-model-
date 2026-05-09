import pandas as pd
import joblib

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

# =========================
# SAMPLE DATA
# =========================

data = {

    "location": [
        "Malviya Nagar",
        "Mansarovar",
        "Vaishali Nagar",
        "Jagatpura",
        "C-Scheme"
    ],

    "sqft": [
        1200,
        1500,
        1800,
        2200,
        3000
    ],

    "bedrooms": [
        2,
        3,
        3,
        4,
        5
    ],

    "bathrooms": [
        2,
        2,
        3,
        4,
        5
    ],

    "balcony": [
        1,
        2,
        2,
        3,
        4
    ],

    "age_of_property": [
        10,
        7,
        5,
        3,
        1
    ],

    "furnishing": [
        "Semi-Furnished",
        "Fully Furnished",
        "Semi-Furnished",
        "Fully Furnished",
        "Fully Furnished"
    ],

    "parking": [
        1,
        1,
        2,
        2,
        3
    ],

    "nearby_facilities": [
        6,
        7,
        8,
        9,
        10
    ],

    "price": [
        4500000,
        6500000,
        8500000,
        12000000,
        18000000
    ]
}

# =========================
# DATAFRAME
# =========================

df = pd.DataFrame(data)

# =========================
# LABEL ENCODERS
# =========================

location_encoder = LabelEncoder()
furnishing_encoder = LabelEncoder()

df["location"] = location_encoder.fit_transform(df["location"])

df["furnishing"] = furnishing_encoder.fit_transform(
    df["furnishing"]
)

# =========================
# FEATURES
# =========================

X = df[[
    "location",
    "sqft",
    "bedrooms",
    "bathrooms",
    "balcony",
    "age_of_property",
    "furnishing",
    "parking",
    "nearby_facilities"
]]

# =========================
# TARGET
# =========================

y = df["price"]

# =========================
# MODEL
# =========================

model = RandomForestRegressor()

model.fit(X, y)

# =========================
# SAVE MODEL
# =========================

joblib.dump(model, "property_model.pkl")

encoders = {
    "location": location_encoder,
    "furnishing": furnishing_encoder
}

joblib.dump(encoders, "encoders.pkl")

print("FILES CREATED SUCCESSFULLY")