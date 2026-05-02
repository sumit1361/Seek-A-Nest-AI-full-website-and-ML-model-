import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Simple dummy data: [Sqft, Beds]
X = [[500, 1], [1000, 2], [1500, 3], [2000, 4], [2500, 5]]
y = [100000, 200000, 300000, 400000, 500000]

model = RandomForestRegressor(n_estimators=10)
model.fit(X, y)

joblib.dump(model, 'property_model.pkl')
print("Model trained and saved as property_model.pkl")