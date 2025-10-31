import streamlit as st
import pandas as pd
from agent import agent
from tools import set_dataframe

st.title("Data Analysis Agent")

uploaded_file = st.file_uploader("Upload CSV", type=['csv'])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    set_dataframe(df)
    st.success(f"Loaded {len(df)} rows")

user_input = st.text_input("Ask about your data:")

if user_input:
    response = agent.chat(user_input)
    st.write(str(response))