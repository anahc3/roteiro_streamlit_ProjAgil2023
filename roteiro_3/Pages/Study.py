import streamlit as st
import datetime

st.title("Roteiro 3: Organizando sua Interface")

st.header("Study Space")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Inspo for my life")
    st.image("https://i.pinimg.com/564x/4b/78/c1/4b78c117bb8197079644d6cb85284a08.jpg")

with col2:
    st.subheader("Inspo for my study")
    st.image("https://i.pinimg.com/564x/4b/7a/8f/4b7a8f652ee8f8220a4f892272f8e409.jpg")