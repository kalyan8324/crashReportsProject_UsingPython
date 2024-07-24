import streamlit as st
import requests

st.title("My app")

if st.button("Fetch Data"):
    resp = requests.get("http://127.0.0.1:8000/")
    if resp.status_code == 200:
        st.write(resp.json())
    else:
        st.write("Something went wrong")