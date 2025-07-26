# 🚗 Car Resale Value Prediction App

car-resale-value-predictor/
├── car_data.csv
├── index.html
├── style.css
├── backend.php
├── train_model.py
├── predict.py
├── car_resale_model.pkl
├── feature_columns.pkl
├── brand_columns.json   


A full-stack machine learning web app that predicts used car resale prices based on real-world input attributes like brand, fuel type, transmission, mileage, and more.
---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** PHP
- **ML Model:** Python (scikit-learn, joblib)
- **Server:** XAMPP (Apache + PHP)
- **Algorithm:** Random Forest Regressor

---

## 🚀 Features

- 🎯 Predict resale price of a car based on user input
- ⚙️ Integrated `PHP` backend that calls a `Python` model script
- 🧠 Model trained with preprocessing, feature encoding, and regression
- ⚡ ~30% faster response time via model serialization using `joblib`
- 🖥️ Fully functional local deployment via XAMPP

---

## 📊 Machine Learning Details

- Target: `selling_price`
- Features: year, km_driven, mileage, engine, max_power, seats, owner, fuel, seller_type, transmission, brand
- Techniques:
  - Numeric conversion & cleaning
  - One-hot encoding (brand, fuel, transmission, etc.)
  - Random Forest Regressor
- Model saved using: `joblib`

---

## 📂 Folder Contents

| File | Purpose |
|------|---------|
| `index.html` | Frontend UI |
| `style.css` | Styling |
| `backend.php` | PHP to call Python model |
| `predict.py` | Python script to load model and predict |
| `car_resale_model.pkl` | Trained ML model |
| `feature_columns.pkl` | Column order for features |
| `brand_columns.json` | Optional reference for brand encoding |
| `requirements.txt` | Python dependencies |

---

## 🔧 Setup (XAMPP)

1. Place files in: `htdocs/car_resale_value_predictor/`
2. Start Apache from XAMPP
3. Visit: `http://localhost/car_resale_value_predictor/index.html`
4. Enter car details and click **Predict**

---

## ⏱️ Benchmark

| Phase | Time |
|-------|------|
| Raw Python CLI | ~2.2s |
| Optimized with joblib | ~1.5s |
| ⚡ Improvement | ~30% |

---

## 📦 Requirements (Python)
```bash
pip install numpy joblib scikit-learn

