import requests
import streamlit as st

API_URL = "https://YOUR-DEPLOYED-API-URL/v1"

st.title("Auracelle Charlie – Mission Console")

actor = st.selectbox("Select Actor", ["US", "UK", "EU", "China"])

if st.button("Fetch Metrics"):
    response = requests.get(f"{API_URL}/metrics", params={"actor": actor})
    st.json(response.json())
