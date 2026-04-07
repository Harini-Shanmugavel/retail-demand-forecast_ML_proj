#  Smart Retail Demand Forecasting System

##  Overview

This project predicts future product demand for retail stores using machine learning. It helps businesses estimate upcoming sales and manage inventory efficiently.

---
##  Live Demo
https://retail-demand-forecastmlproj-pujrkkf8sy9asemenhr2m5.streamlit.app/

##  Features

*  Predicts sales for next 1–4 weeks
*  Store & department-based forecasting
*  Visualizes historical and future trends
*  Real-time predictions using a web app
*  Automatic data update for continuous usage

---

## Problem Statement

Retail businesses often struggle with:

* Overstocking (wasted inventory)
* Stockouts (lost sales)

This project solves that by predicting future demand based on past sales patterns.

---

##  Dataset

* Walmart Store Sales Dataset
* Includes:

  * Store ID (location)
  * Department (product category)
  * Weekly Sales (target)
  * Date (time-based data)
  * External features (temperature, fuel price, holidays)

---

##  Tech Stack

* Python
* Pandas, NumPy
* XGBoost (ML Model)
* Streamlit (Web App)

---

##  ML Pipeline

1. Data Collection & Merging
2. Data Cleaning & Preprocessing
3. Feature Engineering (lag, rolling features)
4. Model Training (XGBoost Regressor)
5. Evaluation (MAE, RMSE)
6. Deployment using Streamlit

---

##  Output

* Predicts future sales for selected store & department
* Supports multi-week forecasting (up to 4 weeks)
* Displays interactive sales trend graph

---

##  How It Works

The model learns patterns from historical sales data and predicts future demand using recent trends and statistical features.

---

##  Project Structure

```
├── app.py
├── model.pkl
├── features.pkl
├── final_data.csv.gz
├── requirements.txt
└── README.md
```

---

##  Key Highlights

* End-to-end ML project
* Real-world retail use case
* Multi-step forecasting
* Deployed on cloud

---

##  Limitations

* Predicts short-term demand (1–4 weeks)
* Accuracy may decrease for longer forecasts

---

##  Future Improvements

* Add real-time data updates
* Auto model retraining
* Advanced forecasting models (LSTM, Prophet)

