# Streamlit dashboard for factory optimization and recommendation system

import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("Nassau_Candy_Distributor1.csv")

# Title
st.title("Nassau Candy Factory Optimization Dashboard")

# Sidebar filters
st.sidebar.header("Filters")

# Product selector
selected_product = st.sidebar.selectbox(
    "Select Product",
    df['Product Name'].unique()
)

# Region selector
selected_region = st.sidebar.selectbox(
    "Select Region",
    df['Region'].unique()
)

# Ship mode filter
selected_ship_mode = st.sidebar.selectbox(
    "Select Ship Mode",
    df['Ship Mode'].unique()
)

# Filter dataset
filtered_df = df[
    (df['Product Name'] == selected_product) &
    (df['Region'] == selected_region) &
    (df['Ship Mode'] == selected_ship_mode)
]

# Product details
st.subheader("Filtered Product Data")
st.write(filtered_df)

# Recommendation dashboard
st.subheader("Recommendation Dashboard")

recommendation_summary = df.groupby('Product Name').agg({
    'Sales': 'sum',
    'Gross Profit': 'mean'
}).reset_index()

st.write(
    recommendation_summary.sort_values(
        by='Sales',
        ascending=False
    ).head(10)
)

# Risk and impact panel
st.subheader("Risk and Impact Panel")

average_profit = filtered_df['Gross Profit'].mean()

if average_profit < 5:
    st.warning(
        "High Risk Reassignment Warning: Low Gross Profit"
    )
else:
    st.success(
        "Low Risk: Stable Gross Profit"
    )

# What-if scenario analysis
st.subheader("What-if Scenario Analysis")

st.write(
    "Simulated 10% sales improvement and 5% profit improvement"
)







# Add KPI metrics and optimization priority controls

# Optimization priority slider
st.sidebar.subheader("Optimization Priority")

priority = st.sidebar.slider(
    "Choose Optimization Priority",
    0,
    100,
    50
)

# KPI Metrics
st.subheader("Key Performance Indicators")

total_sales = filtered_df['Sales'].sum()
total_units = filtered_df['Units'].sum()
average_profit = filtered_df['Gross Profit'].mean()

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Sales",
    round(total_sales, 2)
)

col2.metric(
    "Units Sold",
    int(total_units)
)

col3.metric(
    "Average Gross Profit",
    round(average_profit, 2)
)

# Optimization insight
st.subheader("Optimization Insight")

if priority > 50:
    st.write(
        "Priority set towards speed and operational efficiency."
    )
else:
    st.write(
        "Priority set towards profitability and financial stability."
    )
