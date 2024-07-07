import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

st.title("🎈 Compound Interest Calculator")
st.write("### Input Data")

col1, col2 = st.columns(2)
initial_investment = col1.number_input("Initial Investment", value=5000)
interest_rate = col1.number_input("Interest rate (%)", value=15) / 100
duration = col1.number_input("Duration in years", value=15)

n = 1 # Compounded yearly

year_by_year = {"Year 0": initial_investment}
current_value = initial_investment

for i in range(1, duration + 1):
    current_value = initial_investment * (1 + interest_rate / n) ** (n * i)
    year_by_year[f"Year {i}"] = current_value

if st.button("Calculate"):
    years = list(year_by_year.keys())
    values = list(year_by_year.values())

    plt.figure(figsize=(10, 5))
    plt.plot(years, values, marker='o')
    plt.title('Compound Interest Over Time')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(plt)

    st.write(year_by_year)
