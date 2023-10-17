import streamlit as st
import requests

st.title("Roteiro 4: Integração com APIs")

pais = st.text_input("Digite o nome de um país")

botao = st.button("Buscar informações")

if botao:
    r = requests.get(f'https://restcountries.com/v3.1/name/{pais}')
    st.write("Esse é o nome comum do país procurado:")
    st.write(r.json()[0]["name"]["nativeName"]["por"]["common"])
    st.write("Esse é o nome oficial do país procurado:")
    st.write(r.json()[0]["name"]["nativeName"]["por"]["official"])