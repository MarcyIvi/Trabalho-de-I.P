import streamlit as st

control = 0
if control == 0:
    st.title('PyQuiz')

base_url = f"https://trabalho-de-ip-fjwgwjqeqnhtsxhyb6ntrx.streamlit.app"  # Link base com a porta dinâmica

if st.button('Start!'):
    st.title('''Olá, seja bem-vindo(a) ao PyQuiz!
            Escolha um nível de dificuldade: ''')

    # Criação de links relativos aos níveis de dificuldade
    facil_link = f'[Fácil]({base_url}/Facil)'
    medio_link = f'[Médio]({base_url}/Medio)'
    dificil_link = f'[Difícil]({base_url}/Dificil)'

    st.markdown(facil_link)
    st.markdown(medio_link)
    st.markdown(dificil_link)
