import streamlit as st
import time
pont = 0

st.title('Ok, nível selecionado foi dificil...')

q1 = st.radio('1°) Qual das seguintes opções melhor descreve a principal diferença entre um iterador e um gerador em Python?', ['a) Um gerador é uma expressão que gera sequências, enquanto um iterador é uma função iterável. ','b) Um gerador é uma função que gera sequências, enquanto um iterador é um objeto iterável.', 'c) Ambos são termos intercambiáveis em Python ', 'd) Um iterador é uma função que gera sequências, enquanto um gerador é um objeto iterável. '])

if q1 == 'b) Um gerador é uma função que gera sequências, enquanto um iterador é um objeto iterável.':
    pont += 1

q2 = st.radio('2°) Qual é o propósito principal do GIL (Global Interpreter Lock) em Python?', ['a) Evitar condições de corrida em operações de memória compartilhada.','b) Garantir a consistência em operações de E/S.','c) Melhorar o desempenho geral do interpretador Python.','d) Facilitar a execução paralela de threads.'])

if q2 == 'a) Evitar condições de corrida em operações de memória compartilhada.':
    pont += 1

q3 = st.radio('3°) Qual é uma desvantagem do uso do módulo asyncio para concorrência em comparação com o módulo threading?', ['a) Adiciona métodos à classe.','b) Altera o comportamento de todas as instâncias de uma classe.','c) Limitações em operações de CPU intensivas.','d) Mais facilidade de depuração.'])

if q3 == 'c) Limitações em operações de CPU intensivas.':
    pont += 1

q4 = st.radio('4°) O que uma metaclass em Python permite que você faça? ' ,['a) Adiciona métodos à classe.','b) Define propriedades da classe.','c) Substitui a classe base de uma hierarquia de herança.','d) Altera o comportamento de todas as instâncias de uma classe.'])

if q4 == 'd) Altera o comportamento de todas as instâncias de uma classe.':
    pont += 1

q5 = st.radio('5°) Qual método mágico é chamado quando você usa o operador de adição (+) entre dois objetos em Python?' , ['a) __ plus __','b) __ add __','c) __ sum __','d) __ concat __'])

if q5 == 'b) "__ add __"':
    pont += 1 

q6 = st.radio('6°) O que acontece se você tentar abrir e ler um arquivo que não existe em Python sem usar blocos de tratamento de exceções?', ['a) Um erro de compilação é gerado.','b) Uma exceção do tipo FileNotFoundError é levantada.','c) O programa continua a execução normalmente.','d) O programa entra em um loop infinito.'])

if q6 == 'b) Uma exceção do tipo FileNotFoundError é levantada.':
    pont += 1

q7 = st.radio('7°) Como você verifica se uma chave existe em um dicionário em Python?',['a) key in dictionary','b) dictionary[key] != None','c) dictionary.containsKey(key)','d) dictionary.exists(key)'])

if q7 == 'a) key in dictionary':
    pont += 1

q8 = st.radio('8°) O que é um método estático em uma classe Python?',['a) Um método que não pode acessar atributos da classe.','b) Um método que pertence à instância da classe.' ,'c) Um método que pertence à classe, não à instância.','d) Um método que não pode ser chamado fora da classe.' ])

if q8 == 'c) Um método que pertence à classe, não à instância.':
    pont += 1

q9 = st.radio('9°) Qual é a diferença entre os métodos append() e extend() em uma lista?', ['a) Ambos fazem a mesma coisa; são apenas nomes diferentes para a mesma operação.', 'b) append() adiciona um elemento à frente da lista, enquanto extend() adiciona uma lista à frente da lista.','c) append() adiciona um elemento ao final da lista, enquanto extend() adiciona uma lista ao final da lista.','d) extend() adiciona um elemento ao final da lista, enquanto append() adiciona uma lista ao final da lista.'])

if q9 == 'c) append() adiciona um elemento ao final da lista, enquanto extend() adiciona uma lista ao final da lista.':
    pont += 1    
   
q10 = st.radio('10°) Como você adicionaria um título a um gráfico criado com a Matplotlib?', ['a) title()','b) add_title()','c) plot_title()','d) set_title()'])

if q10 == 'd)':
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
