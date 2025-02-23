import streamlit as st

st.write('oi')
i = st.secrets["my_secrets"]["api_key"]
st.write(i)