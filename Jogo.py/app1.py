import streamlit as st
import random

st.set_page_config(page_title = 'PyWord')



titlle = st.title('PyQuiz')
botao = st.button("Começar")
if not botao: 
   with st.container(): 
     st.text("""Você está no PyQuiz, onde teremos várias perguntas relacionadas a programação. 
                Clique no botão abaixo para começar.""")


if botao == True: 
   escolha = st.radio("Escolha o nível de dificuldade: ", ['facil' , 'médio' ,'dificil'])

   if escolha == 'facil' : 
     pg1= st.radio('qual é dmdkd?', ['xxx','add','ccc'])
     
        


    #pg1 = st.text_input('qual hpgktg gm?') 
    #r = ['xxx','add','ccc']                        if escolha == 'facil': 
 #escolha = st.radio("Escolha o nível de dificuldade: ", ['facil' , 'médio' ,'dificil'])
