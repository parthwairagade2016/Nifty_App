import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Nifty_Stocks.csv")

# Ensure date is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Title
st.title("Nifty Stocks Viewer")

# Select category
categories = df['Category'].unique()
selected_category = st.selectbox("Select Category", categories)

# Filter by selected category
filtered_df = df[df['Category'] == selected_category]

# Select symbol
symbols = filtered_df['Symbol'].unique()
selected_symbol = st.selectbox("Select Symbol", symbols)

# Filter by selected symbol
symbol_df = filtered_df[filtered_df['Symbol'] == selected_symbol]

# Plot
st.subheader(f"Closing Price of {selected_symbol} Over Time")

plt.figure(figsize=(12, 6))
sb.lineplot(data=symbol_df, x='Date', y='Close')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)
