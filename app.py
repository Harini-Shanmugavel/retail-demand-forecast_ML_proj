import streamlit as st
import pandas as pd
import numpy as np
import pickle

# -------------------------------
# Load files
# -------------------------------
model = pickle.load(open('model.pkl', 'rb'))
feature_cols = pickle.load(open('features.pkl', 'rb'))
df = pd.read_csv('final_data.csv.gz')

df['Date'] = pd.to_datetime(df['Date'], format='mixed', errors='coerce')

# -------------------------------
# Store & Department Mapping
# -------------------------------
store_map = {
    1: "Chennai Central",
    2: "Coimbatore Mall",
    3: "Bangalore City",
    4: "Hyderabad Hub",
    5: "Mumbai Plaza"
}

dept_map = {
    1: "Groceries",
    2: "Electronics",
    3: "Clothing",
    4: "Home Essentials",
    5: "Snacks & Beverages"
}

# -------------------------------
# UI
# -------------------------------
st.title("🛒 Smart Retail Demand Forecasting")

st.info("Predict future sales for a selected store and product category.")

store = st.selectbox("Select Store", list(store_map.keys()), format_func=lambda x: store_map[x])
dept = st.selectbox("Select Department", list(dept_map.keys()), format_func=lambda x: dept_map[x])

weeks = st.selectbox("Select Forecast Horizon (Weeks)", [1, 2, 3, 4])

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict"):

    temp = df[(df['Store'] == store) & (df['Dept'] == dept)].sort_values('Date')

    if len(temp) < 30:
        st.error("Not enough historical data for this selection.")
    else:
        future_predictions = []
        temp_copy = temp.copy()

        for i in range(weeks):

            last_row = temp_copy.iloc[-1]

            # Create full feature row
            input_dict = {}

            for col in feature_cols:
                if col in last_row:
                    input_dict[col] = last_row[col]
                else:
                    input_dict[col] = 0

            input_df = pd.DataFrame([input_dict])

            pred = model.predict(input_df)[0]
            future_predictions.append(pred)

            # Create new row for next iteration
            new_row = last_row.copy()
            new_row['Weekly_Sales'] = pred
            new_row['Date'] = last_row['Date'] + pd.Timedelta(days=7)

            temp_copy = pd.concat([temp_copy, pd.DataFrame([new_row])], ignore_index=True)

        # -------------------------------
        # Show Results
        # -------------------------------
        st.success(f"""
📍 Store: {store_map[store]}  
🛍️ Department: {dept_map[dept]}  
📅 Forecast for next {weeks} week(s)
""")

        for i, val in enumerate(future_predictions):
            st.write(f"Week {i+1}: ₹{val:.2f}")

        # -------------------------------
        # Graph (Past + Future)
        # -------------------------------
        st.subheader("📊 Sales Forecast Trend")

        past = temp[['Date', 'Weekly_Sales']]

        future_dates = pd.date_range(
            start=past['Date'].iloc[-1] + pd.Timedelta(days=7),
            periods=weeks,
            freq='W'
        )

        future_df = pd.DataFrame({
            'Date': future_dates,
            'Weekly_Sales': future_predictions
        })

        combined = pd.concat([past, future_df])

        st.line_chart(combined.set_index('Date'))

        # -------------------------------
        # Save Predictions
        # -------------------------------
        new_rows = []

        for i, val in enumerate(future_predictions):
            new_rows.append({
                "Store": store,
                "Dept": dept,
                "Date": past['Date'].iloc[-1] + pd.Timedelta(days=7*(i+1)),
                "Weekly_Sales": val
            })

        df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)
        df.to_csv("final_data.csv", index=False)