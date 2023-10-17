import streamlit as st

st.title("Roteiro 2: Widgets Interativos")

value = st.slider("Escolha um valor", 0, 100)

with st.container():
    toggle = st.toggle("Você quer participar do quiz?", value=False)
    if toggle:
        checkbox = st.checkbox("Sou perfeita!")
        radio = st.radio("Escolhe a opção correta", ["Selecione uma opção", "Cacetudo", "Roro", "Lolo", "Chuck Bass", "Zé Gotinha", "Todas as opções!"])
        select_box = st.selectbox("Do que eu mais preciso agora?", ["Selecione uma opção", "PRECISO me relacionar sexualmente", "Quero beijar ele (dica: ele é cacetudo)", "Terapia", "Treinar", "Todas as opções!"])
        button = st.button("Mostrar valor do slider")
        if checkbox and button:
            st.write("Cliquei no checkbox e concordo com o que está escrito!")
        if button:
            st.write(f"Valor escolhido: {value}")
        if radio == "Todas as opções!" and button:
            st.write("Eu sou seletiva amore! Dos piores rsrsrsrsrs")
        if radio == "Cacetudo" and button:
            st.write("Você acertou no Cacetudo! #Souapaixonada #Elenãomequer #Masvoucontinuarsonhando")
        if radio == "Roro" and button:
            st.write("Você errou! Mas foi um belo chute! Afinal, Roro é a segunda opção mais correta!")
        if radio == "Lolo" and button:
            st.write("Você errou! Lolo é platônico!")
        if radio == "Chuck Bass" and button:
            st.write("Você errou, o Chuck Bass é o amor da minha vida, mas ele não é a opção mais correta, visto que me olhou e ficou de bla bla bla!")
        if radio == "Zé Gotinha" and button:
            st.write("Você errou! Zé Gotinha é um broxa!")
        if select_box == "PRECISO me relacionar sexualmente" and button:
            st.write("De fato.")
        if select_box == "Quero beijar ele (dica: ele é cacetudo)" and button:
            st.write("Se ele é cacetudo mesmo ou não, cpa que nunca saberemos, no entanto, eu quero mesmo.")
        if select_box == "Terapia" and button:
            st.write("Eu preciso mesmo.")
        if select_box == "Treinar" and button:
            st.write("To querendo também. Mas podia ser com ele, né? Pós é cardio com ele (cacetudo).")
        if select_box == "Todas as opções!" and button:
            st.write("De fato. É um mar de opções corretas. E necessárias.")