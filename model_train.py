import joblib
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from xgboost import XGBRegressor


locations = [
    "Jagatpura",
    "Malviya Nagar",
    "Mansarovar",
    "Vaishali Nagar",
    "C-Scheme",
    "Ajmer Road"
]

furnishings = [
    "Unfurnished",
    "Semi-Furnished",
    "Fully Furnished"
]

rows = []

base_prices = {
    "Jagatpura": 4200,
    "Malviya Nagar": 6800,
    "Mansarovar": 5200,
    "Vaishali Nagar": 6100,
    "C-Scheme": 10500,
    "Ajmer Road": 3600
}

for location in locations:
    for sqft in [800, 1050, 1250, 1500, 1800, 2200, 2600]:
        for bedrooms in [1, 2, 3, 4]:
            for furnishing in furnishings:
                bathrooms = max(1, bedrooms - 1)
                balcony = min(3, bedrooms)
                age_of_property = 5
                parking = 1 if bedrooms <= 2 else 2
                nearby_facilities = 7

                furnishing_bonus = {
                    "Unfurnished": 0,
                    "Semi-Furnished": 350000,
                    "Fully Furnished": 700000
                }[furnishing]

                price = (
                    sqft * base_prices[location]
                    + bedrooms * 250000
                    + bathrooms * 120000
                    + balcony * 70000
                    + parking * 200000
                    + furnishing_bonus
                    + nearby_facilities * 50000
                )

                rows.append({
                    "location": location,
                    "sqft": sqft,
                    "bedrooms": bedrooms,
                    "bathrooms": bathrooms,
                    "balcony": balcony,
                    "age_of_property": age_of_property,
                    "furnishing": furnishing,
                    "parking": parking,
                    "nearby_facilities": nearby_facilities,
                    "price": price
                })

df = pd.DataFrame(rows)

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
    n_estimators=300,
    learning_rate=0.07,
    max_depth=5,
    subsample=0.9,
    colsample_bytree=0.9,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "property_model.pkl")
joblib.dump(encoders, "encoders.pkl")

print("Advanced Seek A Nest model trained successfully.")