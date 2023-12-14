import streamlit as st
import time
pont = 0

st.title('Ok, nível selecionado foi fácil...')

q1 = st.radio('1°)  Em Python, como você imprime "Hello, World!" na tela?', ['a) print("Hello, World!")','b) echo("Hello, World!")', 'c) display("Hello, World!")'])

if q1 == 'a) print("Hello, World!")':
    pont += 1

q2 = st.radio('2°)  Qual é o operador de atribuição em Python?', ['a) ==','b) :=','c) ='])

if q2 == 'c) =':
    pont += 1

q3 = st.radio('3°) Qual é o operador usado para calcular a divisão inteira em Python?', ['a) /','b) //','c) %'])

if q3 == 'b) //':
    pont += 1

q4 = st.radio('4°) Como você verifica o comprimento de uma lista em Python?' ,['a) len(lista)','b) size(lista)','c) count(lista)'])

if q4 == 'a) len(lista)':
    pont += 1

q5 = st.radio('5°) Como você comenta múltiplas linhas em Python?' , ['a) /* ... */','b) // ...',"c) '''...'''"])

if q5 == "c) '''...'''":
    pont += 1 

q6 = st.radio('6°) Qual é a função utilizada para obter a entrada do usuário em Python?', ['a) get()','b) input()','c) read()'])

if q6 == 'b) input()':
    pont += 1

q7 = st.radio('7°) Qual é a principal finalidade do comando if em Python?',['a) Realizar loops','b) Definir funções','c) Executar blocos de código condicionalmente'])

if q7 == 'c) Executar blocos de código condicionalmente':
    pont += 1

q8 = st.radio('8°) O que o código range(5) faz em Python?',['a) Gera uma lista de números de 0 a 4','b) Gera uma lista de números de 1 a 5' ,'c) Gera uma lista de números de 0 a 5' ])

if q8 == 'a) Gera uma lista de números de 0 a 4':
    pont += 1

q9 = st.radio('9°) Como você converte uma string para minúsculas em Python?', ['a) str.lower()', 'b) str.to_lowercase()', 'c) lowercase(str)'])

if q9 == 'a) str.lower()':
    pont += 1    
   
q10 = st.radio('10°) Qual é o resultado da expressão booleana True and False?', ['a) True','b) False','c) None'])

if q10 == 'b) False':
    pont += 1

with st.spinner('Espere o resultado...'):
    time.sleep(5)

if pont == 0:
    st.text(f'Que pena...sua nota foi {pont}')
if pont < 5:
    st.text(f'A prática leva a perfeição...sua nota foi {pont}')
if pont >= 5 and pont <= 8:
    st.text(f'Caramba você está indo muito bem!...sua nota foi {pont}')
if pont == 9:
    st.text(f'Arrasou! Foi quase lá, continue assim!...sua nota foi{pont}')
if pont == 10:
    st.text(f'Você Brilhou!!!! Aproveite esse momento é seu!...sua nota é {pont}')
