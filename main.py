import streamlit as st
import requests


url = st.secrets["my_secrets"]["url"]
response = requests.get(url)
st.write(response.json())