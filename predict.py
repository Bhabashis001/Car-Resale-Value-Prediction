#!/usr/bin/env python3
import sys
import numpy as np
import joblib
import warnings

warnings.filterwarnings("ignore")

try:
    # Expecting 11 arguments (plus script name = 12 total)
    if len(sys.argv) != 12:
        print("Usage: python predict.py <year> <km_driven> <mileage> <engine> <max_power> <seats> <owner> <name> <fuel> <seller_type> <transmission>")
        sys.exit(1)
    
    # Parse numeric inputs
    year = float(sys.argv[1])
    km_driven = float(sys.argv[2])
    mileage = float(sys.argv[3])
    engine = float(sys.argv[4])
    max_power = float(sys.argv[5])
    seats = float(sys.argv[6])
    owner = float(sys.argv[7])
    
    # Parse categorical inputs:
    # For name, take the first word as the brand (in lowercase)
    name_input = sys.argv[8].strip()
    brand_input = name_input.split()[0].lower()
    
    fuel_input = sys.argv[9].strip()       # Expected: CNG, Diesel, Petrol
    seller_type_input = sys.argv[10].strip()  # Expected: Individual, Trustmark Dealer
    transmission_input = sys.argv[11].strip() # Expected: Automatic, Manual
    
    # Load the trained model and feature columns list
    model = joblib.load('car_resale_model.pkl')
    feature_cols = joblib.load('feature_columns.pkl')
    
    # Initialize a dictionary for all features.
    # For numeric columns, we know they are: 'year', 'km_driven', 'mileage', 'engine', 'max_power', 'seats', 'owner'
    features_dict = {
        'year': year,
        'km_driven': km_driven,
        'mileage': mileage,
        'engine': engine,
        'max_power': max_power,
        'seats': seats,
        'owner': owner
    }
    
    # For dummy features, we go through each feature name in feature_cols that is not a numeric column.
    # We assume that dummy columns start with one of these prefixes: 'fuel_', 'seller_type_', 'transmission_', 'brand_'
    for col in feature_cols:
        if col in features_dict:
            continue  # already set numeric value
        value = 0  # default value
        if col.startswith("fuel_"):
            # Example: col = "fuel_Diesel"
            category = col.split("_", 1)[1].lower()
            if fuel_input.lower() == category:
                value = 1
        elif col.startswith("seller_type_"):
            # Example: col = "seller_type_Individual"
            category = col.split("_", 1)[1].lower()
            if seller_type_input.lower() == category:
                value = 1
        elif col.startswith("transmission_"):
            # Example: col = "transmission_Manual"
            category = col.split("_", 1)[1].lower()
            if transmission_input.lower() == category:
                value = 1
        elif col.startswith("brand_"):
            # Example: col = "brand_honda"
            category = col.split("_", 1)[1].lower()
            if brand_input == category:
                value = 1
        # Set the value in the dictionary.
        features_dict[col] = value
    
    # Now, build the final feature vector in the order of feature_cols.
    final_features = []
    for col in feature_cols:
        # If the column was not in our dictionary, set it to 0.
        final_features.append(features_dict.get(col, 0))
    
    # Convert to numpy array and reshape
    final_features = np.array(final_features).reshape(1, -1)
    
    # Predict the selling price
    predicted_price = model.predict(final_features)[0]
    print(predicted_price)
    
except Exception as e:
    print("Error in predict.py:", str(e))
