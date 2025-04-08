import streamlit as st
import pandas as pd
st.title("Patent Valuation Tool")

# Option 1: Use built-in sample data
if st.button("Use Sample Data"):
    data = pd.read_csv("data/sample_patents.csv")
    st.session_state.data = data
    st.success("Loaded sample data!")

# Option 2: File upload
uploaded_file = st.file_uploader("Or upload your CSV", type=["csv"])
if uploaded_file:
    st.session_state.data = pd.read_csv(uploaded_file)

# Display and analyze data
if "data" in st.session_state:
    st.write(st.session_state.data.head())
    avg_value = st.session_state.data["value"].mean()
    st.metric("Average Value", f"${avg_value:,.2f}")
