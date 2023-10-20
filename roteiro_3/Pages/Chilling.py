import streamlit as st
import datetime

st.title("Roteiro 3: Organizando sua Interface")

st.header("Chilling Space")
tab1, tab2, tab3 = st.tabs(["Diary", "Tasks", "Movies"])
today = datetime.date.today()
formatted_date = today.strftime("%d/%m")

with tab1:
    st.write(f"Dia {formatted_date}")
    with st.expander("Diary", expanded=False):
        feeling = st.text_input("What are you feeling?")
        button_key = f"Sentimentos_{formatted_date}"
        if st.button("Sentimentos", key=button_key):
            st.write(f"Seu sentimento de hoje ({formatted_date}) é: {feeling}")

with tab2:
    st.write("Hoje")
    if 'tasks_hoje' not in st.session_state:
            st.session_state.tasks_hoje = []
    with st.expander("Tasks do dia", expanded=False):
        with st.form("O que você precisa fazer hoje?"):
            task = st.text_input("O que você precisa fazer hoje?")
            if st.form_submit_button("Adicionar Task"):
                st.session_state.tasks_hoje.append(task)

        st.write("Lista de tasks para hoje")
        for task in st.session_state.tasks_hoje:
            st.write(f"- {task}")

    st.write("Semana")
    if 'tasks_semana' not in st.session_state:
            st.session_state.tasks_semana = []
    with st.expander("Tasks da semana", expanded=False):
        with st.form("O que você precisa fazer essa semana?"):
            task = st.text_input("O que você precisa fazer essa semana?")
            if st.form_submit_button("Adicionar Task"):
                st.session_state.tasks_semana.append(task)

        st.write("Lista de tasks para a semana")
        for task in st.session_state.tasks_semana:
            st.write(f"- {task}")

    st.write("À longo prazo")
    if 'tasks_longo_prazo' not in st.session_state:
            st.session_state.tasks_longo_prazo = []
    with st.expander("Tasks à longo prazo", expanded=False):
        with st.form("O que você precisa fazer à longo prazo?"):
            task = st.text_input("O que você precisa fazer à longo prazo?")
            if st.form_submit_button("Adicionar Task"):
                st.session_state.tasks_longo_prazo.append(task)

        st.write("Lista de tasks à longo prazo")
        for task in st.session_state.tasks_longo_prazo:
            st.write(f"- {task}")

with tab3:
    st.write("Filmes")
    col1, col2 = st.columns(2)
    with col1:
        if 'filmes_para_assistir' not in st.session_state:
            st.session_state.filmes_para_assistir = []
        with st.expander("Filmes para assistir", expanded=False):
            with st.form("Formulário de Filmes para assistir"):
                movie = st.text_input("Qual filme você quer assistir?")
                if st.form_submit_button("Adicionar Filme"):
                    st.session_state.filmes_para_assistir.append(movie)

            st.write("Lista de filmes para assistir:")
            for filme in st.session_state.filmes_para_assistir:
                st.write(f"- {filme}")

    with col2:
        if 'filmes_assistidos' not in st.session_state:
            st.session_state.filmes_assistidos = []
        with st.expander("Filmes assistidos", expanded=False):
            with st.form("Formulário de Filmes assistidos"):
                movie = st.text_input("Quais filmes você já assistiu?")
                if st.form_submit_button("Adicionar Filme"):
                    st.session_state.filmes_assistidos.append(movie)

            st.write("Lista de filmes assistidos:")
            for filme in st.session_state.filmes_assistidos:
                st.write(f"- {filme}")