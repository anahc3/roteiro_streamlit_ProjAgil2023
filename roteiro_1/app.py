import streamlit as st

st.title("Roteiro 1: Primeiros Passos com Streamlit")

input = st.text_input(label="Digite algo")

if st.button("Clique-me"):
    st.write("O que você escreveu foi:", input)
