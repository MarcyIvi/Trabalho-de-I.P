import streamlit as st
import time
pont = 0

st.title("Ok, nível selecionado foi médio...")

q1 = st.radio('1°)  Pergunta: Como você manipula datas e horas em Python?', ['a) Utilizando a biblioteca time.', 'b) Utilizando a biblioteca datetime.','c) Utilizando a função timestamp().','d) Não é possível manipular datas e horas em Python.' ])

if q1 == 'b) Utilizando a biblioteca datetime.':
    pont += 1

q2 = st.radio('2°)   Qual é a função da palavra-chave else em uma estrutura if em Python?', ['a) Introduzir um bloco de código que sempre é executado.','b) Lidar com exceções.','c) Iniciar um loop.','d) Indicar um bloco de código que é executado apenas se a condição do if não for verdadeira.'])

if q2 == 'd) Indicar um bloco de código que é executado apenas se a condição do if não for verdadeira.':
    pont += 1

q3 = st.radio('3°) O que é um loop for em Python?', ['a) Um loop que só pode ser usado com números inteiros.','b) Um loop que itera sobre uma sequência (por exemplo, uma lista ou string).','c) Um loop exclusivo para dicionários.','d) Uma instrução condicional.'])

if q3 == 'b) Um loop que itera sobre uma sequência (por exemplo, uma lista ou string).':
    pont += 1

q4 = st.radio('4°) O que é uma lista em Python?' ,['a) Um conjunto ordenado de elementos, acessíveis por índices.','b) Uma função para realizar operações matemáticas.','c) Uma estrutura de controle de fluxo.','d) Um tipo especial de string.'])

if q4 == 'a) Um conjunto ordenado de elementos, acessíveis por índices.':
    pont += 1

q5 = st.radio('5°) O que é um dicionário em Python?' , ['a) Uma sequência ordenada de elementos.','b) Uma estrutura de controle de fluxo.','c) Um conjunto desordenado de elementos, acessíveis por chaves.','d) Uma função para realizar operações matemáticas.'])

if q5 == 'c) Um conjunto desordenado de elementos, acessíveis por chaves.':
    pont += 1 

q6 = st.radio('6°) Como você converte uma string em minúsculas em Python?', ['a) string.lower()' , 'b) string.toLower()', 'c) string.casefold()', 'd) string.lowercase()'])

if q6 == 'a) string.lower()':
    pont += 1

q7 = st.radio('7°) Qual é a finalidade do método append() em listas Python?', ['a) Adicionar um elemento ao início da lista.','b) Adicionar um elemento ao final da lista.','c) Remover o último elemento da lista.','d) Verificar se um elemento existe na lista.'])

if q7 == 'b) Adicionar um elemento ao final da lista.':
    pont += 1

q8 = st.radio('8°) O que é a palavra-chave None em Python?',['a) Uma constante que representa o número zero.','b) Um marcador que indica a ausência de um valor.' ,'c) Uma palavra reservada para declarar variáveis nulas.','d) Um valor booleano que representa "nenhum".' ])

if q8 == 'd) Um valor booleano que representa "nenhum".':
    pont += 1

q9 = st.radio('9°) Como você converte uma string para minúsculas em Python?', ['a) str.lower()', 'b) str.to_lowercase()', 'c) lowercase(str)','d) str.convertToLower().'])

if q9 == 'a) str.lower()':
    pont += 1    
   
q10 = st.radio('10°) Como você comenta múltiplas linhas em Python?', ['a) // Comentário de linha única','b) /* Comentário */',"c) # Comentário de linha única ou ''' Comentário de múltiplas linhas ''' ",'d) -- Comentário --' ])

if q10 == "c) # Comentário de linha única ou ''' Comentário de múltiplas linhas ''' ":
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
