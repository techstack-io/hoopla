import streamlit as st
import pandas as pd

st.title("Company Product-Page Visits")

# 1️⃣ Upload or auto-load the CSV
uploaded_file = st.file_uploader("Upload your company_page_visits.csv", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    try:
        df = pd.read_csv("company_page_visits.csv")
        st.info("Loaded local company_page_visits.csv")
    except FileNotFoundError:
        st.warning("Upload the CSV to begin.")
        st.stop()  # ⚠️ This stops execution, so nothing below runs

# Clean column names
df.columns = df.columns.str.strip()
COMPANY_COLUMN_NAME = "Company Name"

if COMPANY_COLUMN_NAME not in df.columns:
    st.error(f"Error: Required column '{COMPANY_COLUMN_NAME}' not found.")
    st.stop()

# 2️⃣ Preview data
st.subheader("Preview")
st.dataframe(df.head(20))

# 3️⃣ Metrics
st.subheader("Summary")
total_companies = df[COMPANY_COLUMN_NAME].nunique()
total_visits = len(df)
st.metric("Unique Companies", total_companies)
st.metric("Total Product Page Visits", total_visits)

# 4️⃣ Chart
top = df[COMPANY_COLUMN_NAME].value_counts().head(20).reset_index()
top.columns = [COMPANY_COLUMN_NAME, "Visits"]
st.bar_chart(top.set_index(COMPANY_COLUMN_NAME))

# ✅ ADD YOUR TEXT INPUT HERE (after all the data loading)
st.subheader("Ask Questions")
question = st.text_input("What would you like to know?")

if question:
    st.write(f"You asked: {question}")
    # Add your question handling logic here