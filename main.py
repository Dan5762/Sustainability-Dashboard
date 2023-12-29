import streamlit as st
import pandas as pd

data_df = pd.read_csv("data.csv")

print(data_df.head())

st.write("Here's our first attempt at using data to create a table:")
st.write(data_df)
