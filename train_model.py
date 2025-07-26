import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

# Load dataset (ensure car_data.csv is in the same folder)
data = pd.read_csv('car_data.csv')

# --- Extract brand from name ---
# Take the first word from "name" as the brand (converted to lowercase)
data['brand'] = data['name'].str.split().str[0].str.lower()
# Drop the original name column
data.drop('name', axis=1, inplace=True)

# --- Rename mileage column for simplicity ---
if 'mileage(km/ltr/kg)' in data.columns:
    data.rename(columns={"mileage(km/ltr/kg)": "mileage"}, inplace=True)

# --- Convert numeric columns and clean data ---
numeric_cols = ['year', 'selling_price', 'km_driven', 'mileage', 'engine', 'max_power', 'seats']
for col in numeric_cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')
data.dropna(subset=numeric_cols, inplace=True)

# --- Convert owner column ---
owner_mapping = {
    'First Owner': 1,
    'Second Owner': 2,
    'Third Owner': 3,
    'Fourth & Above Owner': 4
}
data['owner'] = data['owner'].map(owner_mapping)
data['owner'] = data['owner'].fillna(0)

# --- One-hot encode categorical variables ---
# For brand and transmission, use drop_first=True to avoid multicollinearity.
data = pd.get_dummies(data, columns=['brand', 'transmission'], drop_first=True)
# For fuel and seller_type, keep all dummies.
data = pd.get_dummies(data, columns=['fuel', 'seller_type'], drop_first=False)

# --- Separate features and target ---
X = data.drop('selling_price', axis=1)
y = data['selling_price']

# Save the feature columns (this list will have 45 features if that is what your data yields)
feature_cols = X.columns.tolist()
joblib.dump(feature_cols, 'feature_columns.pkl')
print("Final feature columns ({}):".format(len(feature_cols)), feature_cols)

# --- Split the data ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Train the model ---
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error: {mae:.2f}")

# Save the trained model to disk
joblib.dump(model, 'car_resale_model.pkl')
print("Model saved as car_resale_model.pkl")
