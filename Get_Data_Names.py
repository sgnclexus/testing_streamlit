import streamlit as st
import pandas as pd

names_link = 'dataset.csv'
names_data = pd.read_csv(names_link)

st.title('Get data from CSV')
st.dataframe(names_data)