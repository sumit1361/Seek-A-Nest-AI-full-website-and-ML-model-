import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor


data = {
    "location": [
        "Jagatpura", "Jagatpura", "Jagatpura",
        "Malviya Nagar", "Malviya Nagar",
        "Mansarovar", "Mansarovar",
        "Vaishali Nagar", "Vaishali Nagar",
        "C-Scheme", "C-Scheme",
        "Ajmer Road", "Ajmer Road"
    ],
    "sqft": [1050, 1400, 1800, 1500, 2200, 1250, 1800, 1100, 1700, 1800, 3000, 1500, 2400],
    "bedrooms": [2, 3, 3, 3, 4, 2, 3, 2, 3, 3, 5, 0, 3],
    "bathrooms": [2, 2, 3, 2, 4, 2, 3, 2, 3, 3, 5, 0, 3],
    "balcony": [1, 2, 2, 2, 3, 1, 2, 1, 2, 2, 4, 0, 2],
    "age_of_property": [4, 3, 2, 7, 4, 8, 5, 6, 3, 10, 3, 0, 2],
    "furnishing": [
        "Semi-Furnished", "Fully Furnished", "Semi-Furnished",
        "Semi-Furnished", "Fully Furnished",
        "Semi-Furnished", "Fully Furnished",
        "Unfurnished", "Semi-Furnished",
        "Fully Furnished", "Fully Furnished",
        "Unfurnished", "Semi-Furnished"
    ],
    "parking": [1, 1, 2, 1, 2, 1, 2, 1, 1, 2, 3, 0, 2],
    "nearby_facilities": [8, 9, 9, 9, 10, 7, 8, 8, 9, 10, 10, 6, 7],
    "price": [
        3800000, 5200000, 7000000,
        8200000, 12500000,
        5500000, 7600000,
        4800000, 7200000,
        12000000, 18500000,
        4200000, 6800000
    ]
}

df = pd.DataFrame(data)

encoders = {}

for col in ["location", "furnishing"]:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])
    encoders[col] = encoder

X = df[
    [
        "location",
        "sqft",
        "bedrooms",
        "bathrooms",
        "balcony",
        "age_of_property",
        "furnishing",
        "parking",
        "nearby_facilities"
    ]
]

y = df["price"]

model = XGBRegressor(
    n_estimators=250,
    learning_rate=0.08,
    max_depth=5,
    subsample=0.9,
    colsample_bytree=0.9,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "property_model.pkl")
joblib.dump(encoders, "encoders.pkl")

print("Model and encoders saved successfully.")