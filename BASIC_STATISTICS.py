#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:41:08 2023

@author: Vicky
"""

#ESTATÍSTICA BÁSICA

#Medidas de tendência central

#Média aritmética
import numpy as np

# Exemplo de lista de valores
valores = [15, 5, 10, 25, 20]

# Calcular a média usando a função mean() do Numpy
media = np.mean(valores)

# Imprimir o resultado
print("A média dos valores é:", media)

#Média ponderada
import numpy as np

# Lista de observações
observacoes = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]

# Lista de pesos correspondentes às observações
pesos = [0.1, 0.2, 0.05, 0.15, 0.1, 0.05, 0.05, 0.01, 0.01, 0.03, 0.02, 0.04, 0.03, 0.01, 0.02, 0.02, 0.03, 0.01, 0.02, 0.01]

# Verificar se o número de observações é igual ao número de pesos
if len(observacoes) != len(pesos):
    raise ValueError("O número de observações deve ser igual ao número de pesos")

# Converter as listas para arrays numpy
observacoes = np.array(observacoes)
pesos = np.array(pesos)

# Calcular a média ponderada
media_ponderada = np.average(observacoes, weights=pesos)

# Imprimir o resultado
print("A média ponderada é: {:.2f}".format(media_ponderada))

#Média geométrica
import numpy as np

# Lista de observações
observacoes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# Converter as observações para um array numpy
observacoes = np.array(observacoes)

# Calcular a média geométrica
media_geometrica = np.prod(observacoes) ** (1 / len(observacoes))

# Imprimir o resultado
print("A média geométrica é: {:.2f}".format(media_geometrica))

#Mediana
import numpy as np

# Exemplo de lista de valores
valores = [14, 13, 14, 15, 12, 16, 1750, 24, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# lista ordenada de valores
valores_ordenados = np.sort(valores)

# Imprimir o resultado

# calcular a mediana obtendo o valor que divide o conjunto ao meio
mediana_valores_ordenados = valores_ordenados[len(valores_ordenados) // 2]

# Imprimir a mediana calculada
print("A mediana dos valores é: {:.2f}".format(mediana_valores_ordenados))

# Calcular a mediana usando a função median() do Numpy
mediana = np.median(valores)

# Imprimir a mediana calculada
print("A mediana dos valores é: {:.2f}".format(mediana))

# Calcular a media usando a função mean() do Numpy
media = np.mean(valores)

# Imprimir a média calculada
print("A media dos valores é: {:.2f}".format(media))

#Moda
from scipy import stats

# Exemplo de lista de valores
valores = [5, 10, 15, 20, 20, 25, 30, 30, 30]

# Calcular a moda usando a função mode do SciPy
moda = stats.mode(valores)

# Imprimir o resultado
print("A moda dos valores é:", moda.mode[0])

###############################################################################

#Medidas de dispersão

#Variância
import numpy as np

# Exemplo de lista de valores
valores = [5, 10, 15, 20, 25]

# Calcular a variância usando a função var do NumPy
variancia = np.var(valores)

# Imprimir o resultado
print("A variância dos valores é:", variancia)

#Desvio padrão
import numpy as np

# Exemplo de lista de valores
valores = [5, 10, 15, 20, 25]

# Calcular o desvio padrão usando a função std do NumPy
desvio_padrao = np.std(valores)

# Imprimir o resultado
print("O desvio padrão dos valores é:", desvio_padrao)

###############################################################################

#Probabilidade

#Probabilidade Clássica
# Importar a biblioteca random
import random

# Definir o espaço amostral e o evento de interesse
espaco_amostral = ['C', 'K']
evento_cara = 'C'

# Simular o lançamento da moeda várias vezes
num_lancamentos = 1000
contador_cara = 0

for _ in range(num_lancamentos):
    resultado = random.choice(espaco_amostral)
    if resultado == evento_cara:
        contador_cara += 1

# Calcular a probabilidade clássica
probabilidade = contador_cara / num_lancamentos

# Imprimir o resultado
print("A probabilidade de obter cara é:", probabilidade)

#Probabilidade Empírica
# Importar a biblioteca random
import random

# Definir a caixa com bolas
caixa = ['vermelha', 'azul']

# Realizar uma série de experimentos
num_experimentos = 100
contador_vermelha = 0

for _ in range(num_experimentos):
    bola = random.choice(caixa)
    if bola == 'vermelha':
        contador_vermelha += 1

# Calcular a probabilidade empírica
probabilidade_empirica = contador_vermelha / num_experimentos

# Imprimir o resultado
print("A probabilidade empírica de retirar uma bola vermelha é:", probabilidade_empirica)

#Probabilidade condicional
# Importar a biblioteca random
import random

# Definir a urna com bolas
urna = ['vermelha', 'azul', 'azul']

# Realizar a primeira retirada
primeira_bola = random.choice(urna)

# Verificar se a primeira bola é azul
if primeira_bola == 'azul':
    # Retirar uma segunda bola da urna
    segunda_bola = random.choice(urna)
    if segunda_bola == 'vermelha':
        # Calcular a probabilidade condicional P(A|B)
        prob_condicional = 1.0
    else:
        prob_condicional = 0.0
else:
    prob_condicional = 0.0

# Imprimir o resultado
print("A probabilidade condicional de tirar uma bola vermelha dado que a primeira bola foi azul é:", prob_condicional)

#Espaço Amostral
import numpy as np

# Definindo o espaço amostral
espaco_amostral = np.array([1, 2, 3, 4, 5, 6])

# Imprimindo o espaço amostral
print("Espaço Amostral:", espaco_amostral)

#Eventos
# Importando a biblioteca random para gerar números aleatórios
import random

# Definindo a função para simular o lançamento de um dado
def lancamento_dado():
    return random.randint(1, 6)

# Definindo o número de experimentos
num_experimentos = 1000

# Contador para o número de vezes que o evento "4" ocorre
num_evento_4 = 0

# Realizando os experimentos
for _ in range(num_experimentos):
    resultado = lancamento_dado()
    if resultado == 4:
        num_evento_4 += 1

# Calculando a probabilidade do evento "4"
probabilidade_4 = num_evento_4 / num_experimentos

# Imprimindo o resultado
print("Probabilidade de obter o resultado 4:", probabilidade_4)

#Evento Composto
# Importando a biblioteca random para gerar números aleatórios
import random

# Definindo a função para simular o lançamento de uma moeda
def lancamento_moeda():
    return random.choice(['cara', 'coroa'])

# Definindo a função para simular o lançamento de um dado
def lancamento_dado():
    return random.randint(1, 6)

# Definindo o número de experimentos
num_experimentos = 1000

# Contador para o número de vezes que o evento composto ocorre
num_evento_composto = 0

# Realizando os experimentos
for _ in range(num_experimentos):
    resultado_moeda = lancamento_moeda()
    resultado_dado = lancamento_dado()
    if resultado_moeda == 'cara' and resultado_dado == 5:
        num_evento_composto += 1

# Calculando a probabilidade do evento composto
probabilidade_evento_composto = num_evento_composto / num_experimentos

# Imprimindo o resultado
print("Probabilidade de obter 'cara' na moeda e '5' no dado:", probabilidade_evento_composto)

#Eventos Mutuamente Exclusivo
# Importando a biblioteca random para gerar números aleatórios
import random

# Definindo a função para simular o lançamento de um dado
def lancamento_dado():
    return random.randint(1, 6)

# Definindo o número de experimentos
num_experimentos = 1000

# Contadores para o número de vezes que cada evento ocorre
num_par = 0
num_impar = 0

# Realizando os experimentos
for _ in range(num_experimentos):
    resultado = lancamento_dado()
    if resultado % 2 == 0:
        num_par += 1
    else:
        num_impar += 1

# Calculando a probabilidade de um dos eventos ocorrer
probabilidade_mutuamente_exclusivo = (num_par + num_impar) / num_experimentos

# Imprimindo os resultados
print("Probabilidade de ocorrer um número par ou ímpar:", probabilidade_mutuamente_exclusivo)
print("Probabilidade de ocorrer um número par:", num_par / num_experimentos)
print("Probabilidade de ocorrer um número ímpar:", num_impar / num_experimentos)

#Eventos Independentes
# Importando a biblioteca random para gerar números aleatórios
import random

# Definindo a função para simular o lançamento de uma moeda
def lancamento_moeda():
    return random.choice(['cara', 'coroa'])

# Definindo a função para simular o lançamento de um dado
def lancamento_dado():
    return random.randint(1, 6)

# Definindo o número de experimentos
num_experimentos = 1000

# Contadores para o número de vezes que ambos os eventos ocorrem
num_cara_e_par = 0

# Realizando os experimentos
for _ in range(num_experimentos):
    resultado_moeda = lancamento_moeda()
    resultado_dado = lancamento_dado()
    if resultado_moeda == 'cara' and resultado_dado % 2 == 0:
        num_cara_e_par += 1

# Calculando a probabilidade de ambos os eventos ocorrerem
probabilidade_independente = num_cara_e_par / num_experimentos

# Imprimindo o resultado
print("Probabilidade de obter cara e número par:", probabilidade_independente)

#Interpretação Frequentista
import random

def experimento_lancamento_dado():
    # Simula o lançamento de um dado de seis faces
    return random.randint(1, 6)

def experimentos_repetidos(n, evento):
    # Realiza n experimentos repetidos
    ocorrencias = 0
    for _ in range(n):
        resultado = experimento_lancamento_dado()
        if resultado == evento:
            ocorrencias += 1
    return ocorrencias

# Configurações do experimento
num_repeticoes = 10000
numero_evento = 4

# Realiza os experimentos repetidos
ocorrencias_evento = experimentos_repetidos(num_repeticoes, numero_evento)

# Calcula a frequência relativa do evento
frequencia_relativa = ocorrencias_evento / num_repeticoes

# Imprime o resultado
print(f"A frequência relativa do número {numero_evento} é de {frequencia_relativa:.4f}")

#Frequência relativa
def calcular_frequencia_relativa(observacoes, evento):
    ocorrencias = observacoes.count(evento)
    total_observacoes = len(observacoes)
    frequencia_relativa = ocorrencias / total_observacoes
    return frequencia_relativa

# Exemplo de observações
observacoes = [1, 2, 3, 1, 4, 1, 5, 1, 6, 1]

# Evento a ser calculado a frequência relativa
evento = 1

# Cálculo da frequência relativa
frequencia = calcular_frequencia_relativa(observacoes, evento)

# Imprimir o resultado
print(f"A frequência relativa do evento {evento} é de {frequencia:.2f}")

#Estabilidade no longo prazo
import random

def estimar_probabilidade(numero_desejado, num_lancamentos):
    ocorrencias = 0
    for _ in range(num_lancamentos):
        resultado = random.randint(1, 6)
        if resultado == numero_desejado:
            ocorrencias += 1
    probabilidade = ocorrencias / num_lancamentos
    return probabilidade

# Configurações do experimento
numero_desejado = 6
num_lancamentos = 10000

# Estimativa inicial da probabilidade
probabilidade_estimada = estimar_probabilidade(numero_desejado, num_lancamentos)
print(f"Estimativa inicial da probabilidade: {probabilidade_estimada:.4f}")

# Aumentar o número de lançamentos
num_lancamentos *= 10
probabilidade_estimada = estimar_probabilidade(numero_desejado, num_lancamentos)
print(f"Estimativa após {num_lancamentos} lançamentos: {probabilidade_estimada:.4f}")

# Aumentar o número de lançamentos novamente
num_lancamentos *= 10
probabilidade_estimada = estimar_probabilidade(numero_desejado, num_lancamentos)
print(f"Estimativa após {num_lancamentos} lançamentos: {probabilidade_estimada:.4f}")

# Aumentar o número de lançamentos novamente
num_lancamentos *= 10
probabilidade_estimada = estimar_probabilidade(numero_desejado, num_lancamentos)
print(f"Estimativa após {num_lancamentos} lançamentos: {probabilidade_estimada:.4f}")

#Probabilidade como proporção
import random

def calcular_probabilidade(evento, num_lancamentos):
    ocorrencias = 0
    for _ in range(num_lancamentos):
        resultado = random.randint(1, 6)
        if resultado == evento:
            ocorrencias += 1
    probabilidade = ocorrencias / num_lancamentos
    return probabilidade

# Configurações do experimento
evento = 3
num_lancamentos = 10000

# Calcular a probabilidade
probabilidade = calcular_probabilidade(evento, num_lancamentos)
print(f"A probabilidade de obter o número {evento} é: {probabilidade:.4f}")


#Limitações na interpretação frequentista - A interpretação frequentista da 
      #probabilidade tem sido amplamente utilizada e é baseada na ideia de que 
      #a probabilidade de um evento é igual à frequência relativa desse evento 
      #em um grande número de experimentos repetidos. No entanto, essa 
      #interpretação tem algumas limitações e críticas associadas a ela.


#Interpretação Axiomática ou Clássica - Na interpretação axiomática ou clássica
      #da probabilidade, a probabilidade é definida com base em um conjunto de 
      #axiomas ou regras matemáticas.


#Interpretação Subjetiva  - Na interpretação subjetiva, a probabilidade não 
      #está associada a frequências observadas ou propriedades físicas do mundo,
      #mas sim às crenças e opiniões do indivíduo.

#Graus de Crença
# Importar bibliotecas
import numpy as np

# Definir uma lista de graus de crença
graus_crenca = [0.2, 0.6, 0.8, 0.4, 0.9]

# Função para verificar se um evento ocorre com base no grau de crença
def ocorre_evento(grau_crenca):
    return np.random.random() < grau_crenca

# Simulação de eventos com base nos graus de crença
for grau_crenca in graus_crenca:
    if ocorre_evento(grau_crenca):
        print("Evento ocorre com grau de crença:", grau_crenca)
    else:
        print("Evento não ocorre com grau de crença:", grau_crenca)
        
#Atualização das Crenças
# Importar bibliotecas
import numpy as np

# Definir as probabilidades a priori
probabilidade_priori = 0.5

# Definir a verossimilhança
verossimilhanca = 0.7

# Definir a probabilidade a posteriori
probabilidade_posteriori = (verossimilhanca * probabilidade_priori) / ((verossimilhanca * probabilidade_priori) + ((1 - verossimilhanca) * (1 - probabilidade_priori)))

# Imprimir a probabilidade a posteriori
print("Probabilidade a posteriori:", probabilidade_posteriori)

#Contextualidade
# Importar bibliotecas
import numpy as np

# Definir as informações/contexto disponíveis
informacoes = {
    'Evento A': 0.6,
    'Evento B': 0.4,
    'Evento C': 0.3
}

# Calcular a probabilidade subjetiva com base nas informações/contexto
probabilidade_subjetiva = np.random.choice(list(informacoes.values()))

# Imprimir a probabilidade subjetiva
print("Probabilidade subjetiva:", probabilidade_subjetiva)

#Uso em tomadas de decisão
# Importar bibliotecas
import numpy as np

# Definir as probabilidades subjetivas
prob_A = 0.6  # Probabilidade subjetiva do evento A
prob_B = 0.4  # Probabilidade subjetiva do evento B

# Simular uma tomada de decisão
decisao = np.random.choice(['A', 'B'], p=[prob_A, prob_B])

# Imprimir a decisão tomada
print("Decisão tomada:", decisao)

#Interpretações modernas da probabilidade - TEORIA FUZZY EENTRA AQUI!

#Regras

#Regra da adição
# Importar a biblioteca random
import random

# Definir os eventos A e B
evento_A = [2, 4, 6]  # Números pares
evento_B = [1, 3, 5]  # Números ímpares

# Simular o lançamento de um dado
resultado = random.randint(1, 6)

# Verificar se o resultado pertence ao evento A ou B
if resultado in evento_A or resultado in evento_B:
    # Calcular a probabilidade da união P(A ou B)
    prob_uniao = len(evento_A) / 6 + len(evento_B) / 6 - len(evento_A and evento_B) / 6
else:
    prob_uniao = 0.0

# Imprimir o resultado
print("A probabilidade da união dos eventos A ou B é:", prob_uniao)

#Regra da multiplicação
# Importar a biblioteca random
import random

# Definir as probabilidades dos eventos A e B
prob_A = 0.5  # Probabilidade de obter cara
prob_B = 0.5  # Probabilidade de obter um número par

# Simular o lançamento da moeda e do dado
resultado_moeda = random.choice(["cara", "coroa"])
resultado_dado = random.choice([1, 2, 3, 4, 5, 6])

# Verificar se os resultados satisfazem os eventos A e B
if resultado_moeda == "cara" and resultado_dado % 2 == 0:
    # Calcular a probabilidade da ocorrência conjunta P(A e B)
    prob_conjunta = prob_A * prob_B
else:
    prob_conjunta = 0.0

# Imprimir o resultado
print("A probabilidade da ocorrência conjunta dos eventos A e B é:", prob_conjunta)

#Regra da complementaridade - A regra da complementaridade é um conceito 
        #fundamental da teoria das probabilidades. Ela estabelece uma relação 
        #entre a probabilidade de um evento ocorrer e a probabilidade de seu 
        #complemento ocorrer.
        
#Regra da probabilidade condicional - A probabilidade condicional é a 
        #probabilidade de um evento A ocorrer dado que outro evento B já ocorreu. 
        
#Regra da probabilidade total - Essa regra é usada quando um evento pode ocorrer
        #de várias maneiras, sendo que cada uma dessas maneiras tem uma 
        #probabilidade associada. 
        
#Regra de Bayes - A regra de Bayes permite atualizar probabilidades com base em 
        #informações adicionais. Ela é especialmente útil quando se deseja 
        #determinar a probabilidade de um evento A ocorrer dado que outro evento B 
        #já ocorreu. 
        
###############################################################################

#Distribuições estatísticas - distribuição de Gauss e Função de densidade de 
        #probabilidade entram aqui.
        
#Função de densidade de probabilidade (PDF)
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros da distribuição normal
mu = 0  # média
sigma = 1  # desvio padrão

# Valores de x para plotagem da função de densidade de probabilidade
x = np.linspace(-5, 5, 100)

# Calcula a PDF da distribuição normal
pdf = norm.pdf(x, mu, sigma)

# Plota a PDF
plt.plot(x, pdf)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Função de Densidade de Probabilidade (Distribuição Normal)')
plt.grid(True)
plt.show()

#Função de distribuição acumulada
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parâmetros da distribuição normal
mu = 0  # média
sigma = 1  # desvio padrão

# Valores de x para plotagem da função de distribuição acumulada
x = np.linspace(-5, 5, 100)

# Calcula a função de distribuição acumulada da distribuição normal
cdf = norm.cdf(x, mu, sigma)

# Plota a função de distribuição acumulada
plt.plot(x, cdf)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.title('Função de Distribuição Acumulada (Distribuição Normal)')
plt.grid(True)
plt.show()

#Momentos de uma distribuição - Opção 1
import numpy as np

# Lista de valores
valores = [2, 4, 6, 8, 10]

# Cálculo da média
media = np.mean(valores)

# Cálculo da variância
variancia = np.var(valores)

print("Média:", media)
print("Variância:", variancia)

#Momentos de uma distribuição - Opção 2    
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis

# Lista de valores
valores = [2, 4, 6, 8, 10]

# Cálculo da assimetria
assimetria = skew(valores)

# Cálculo da curtose
curtose = kurtosis(valores)

print("Assimetria:", assimetria)
print("Curtose:", curtose)

###############################################################################

#Intervalos de confiança e testes de hipóteses

#Estimativa pontual e a estimativa por intervalo - A estimativa pontual envolve 
        #o cálculo de um único valor numérico que representa a melhor estimativa 
        #possível do parâmetro populacional.
        #Essa faixa de valores é conhecida como intervalo de confiança e indica 
        #a incerteza associada à estimativa. Por exemplo, a média amostral é 
        #frequentemente usada como uma estimativa pontual da média populacional. 
        #a estimativa por intervalo fornece uma faixa de valores plausíveis para 
        #o parâmetro populacional.

###############################################################################

#Testes de hipóteses - Os testes de hipóteses são procedimentos estatísticos 
        #utilizados para tomar decisões sobre a validade de uma afirmação feita 
        #sobre um parâmetro populacional. Essas afirmações são formuladas em 
        #termos de hipótese nula (H0) e hipótese alternativa (H1), também 
        #conhecida como hipótese de pesquisa. 
        
###############################################################################

#Gráficos e visualizações

#Tendências, discrepâncias e insights sobre os dados - Os gráficos e 
        #visualizações desempenham um papel essencial na identificação de 
        #tendências, discrepâncias e insights ocultos nos dados.
        
#Gráfico de barras
import matplotlib.pyplot as plt

# Dados das categorias e seus valores
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']
valores = [20, 35, 30, 15]

# Criar o gráfico de barras
plt.bar(categorias, valores)

# Personalizar o gráfico
plt.title('Gráfico de Barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Exibir o gráfico
plt.show()

#Gráfico de colunas
import matplotlib.pyplot as plt

# Dados das categorias e seus valores
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']
valores = [20, 35, 30, 15]

# Criar o gráfico de colunas
plt.bar(categorias, valores)

# Personalizar o gráfico
plt.title('Gráfico de Colunas')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Exibir o gráfico
plt.show()

#Gráfico de setores
import matplotlib.pyplot as plt

# Dados das categorias e seus valores
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4']
valores = [20, 35, 30, 15]

# Criar o gráfico de setores
plt.pie(valores, labels=categorias)

# Personalizar o gráfico
plt.title('Gráfico de Setores')

# Exibir o gráfico
plt.show()

#Histograma
import matplotlib.pyplot as plt

# Dados da variável
dados = [22, 30, 32, 35, 38, 40, 42, 45, 50, 55, 60, 65, 70, 72, 75]

# Criar o histograma
plt.hist(dados, bins=5)

# Personalizar o histograma
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frequência')

# Exibir o histograma
plt.show()

#Gráfico de dispersão
import matplotlib.pyplot as plt

# Dados das variáveis
x = [1, 2, 3, 4, 5, 6]
y = [3, 5, 4, 6, 8, 7]

# Criar o gráfico de dispersão
plt.scatter(x, y)

# Personalizar o gráfico
plt.title('Gráfico de Dispersão')
plt.xlabel('Variável X')
plt.ylabel('Variável Y')

# Exibir o gráfico
plt.show()

#Gráfico de linhas
import matplotlib.pyplot as plt

# Dados das variáveis
x = [1, 2, 3, 4, 5, 6]
y = [3, 5, 4, 6, 8, 7]

# Criar o gráfico de linhas
plt.plot(x, y)

# Personalizar o gráfico
plt.title('Gráfico de Linhas')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibir o gráfico
plt.show()

#Gráfico de caixas (boxplot)
import seaborn as sns

# Dados das variáveis
grupo1 = [10, 12, 15, 18, 20, 22, 25]
grupo2 = [5, 8, 10, 12, 15, 18, 20]

# Criar o gráfico de caixas
sns.boxplot(data=[grupo1, grupo2])

# Personalizar o gráfico
plt.title('Gráfico de Caixas')
plt.ylabel('Valores')

# Exibir o gráfico
plt.show()

#Gráfico de área
import matplotlib.pyplot as plt

# Dados das categorias
categorias = ['Categoria A', 'Categoria B', 'Categoria C', 'Categoria D']
valores = [30, 45, 25, 50]

# Criar o gráfico de área
plt.stackplot(categorias, valores, labels=categorias)

# Personalizar o gráfico
plt.title('Gráfico de Área')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Exibir as legendas
plt.legend(loc='upper left')

# Exibir o gráfico
plt.show()

#Gráfico de dispersão com bolhas
import matplotlib.pyplot as plt
import numpy as np

# Dados das variáveis
x = np.random.rand(50)  # Exemplo de valores aleatórios para o eixo x
y = np.random.rand(50)  # Exemplo de valores aleatórios para o eixo y
z = np.random.rand(50)  # Exemplo de valores aleatórios para a terceira variável

# Criar o gráfico de dispersão com bolhas
plt.scatter(x, y, s=z*1000, alpha=0.5)

# Personalizar o gráfico
plt.title('Gráfico de Dispersão com Bolhas')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibir o gráfico
plt.show()

#Mapas e gráficos geoespaciais
import folium

# Criar um objeto de mapa
mapa = folium.Map(location=[-22.9068, -43.1729], zoom_start=12)

# Adicionar um marcador no mapa
folium.Marker([-22.9068, -43.1729], popup='Rio de Janeiro').add_to(mapa)

# Exibir o mapa
mapa.save('mapa.html')

#Gráfico de área empilhada
import matplotlib.pyplot as plt

# Dados das categorias
categorias = ['Categoria A', 'Categoria B', 'Categoria C']
valores1 = [20, 35, 15]  # Valores para a primeira categoria
valores2 = [30, 15, 25]  # Valores para a segunda categoria
valores3 = [10, 30, 20]  # Valores para a terceira categoria

# Criar o gráfico de área empilhada
plt.stackplot(categorias, valores1, valores2, valores3, labels=['Valor 1', 'Valor 2', 'Valor 3'])

# Personalizar o gráfico
plt.title('Gráfico de Área Empilhada')
plt.xlabel('Categorias')
plt.ylabel('Valores')

# Exibir as legendas
plt.legend(loc='upper left')

# Exibir o gráfico
plt.show()

#Gráfico de radar
import numpy as np
import matplotlib.pyplot as plt

# Dados das variáveis e categorias
variaveis = ['Variável A', 'Variável B', 'Variável C', 'Variável D', 'Variável E', 'Variável F']
categorias = ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4', 'Categoria 5', 'Categoria 6']

# Valores para cada categoria e variável
valores_categoria1 = [3, 4, 2, 5, 3]
valores_categoria2 = [4, 2, 3, 2, 5]
valores_categoria3 = [2, 5, 4, 3, 2]
valores_categoria4 = [5, 3, 2, 4, 4]
valores_categoria5 = [3, 2, 5, 3, 4]
valores_categoria6 = [4, 2, 2, 3, 3]

# Criar o gráfico de radar
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
ax.set_theta_offset(np.pi/2)
ax.set_theta_direction(-1)

# Calcular os ângulos para cada variável
angulos = np.linspace(0, 2*np.pi, len(variaveis), endpoint=False).tolist()

# Adicionar as linhas de dados para cada categoria
ax.plot(angulos, valores_categoria1 + [valores_categoria1[0]], label='Categoria 1')
ax.plot(angulos, valores_categoria2 + [valores_categoria2[0]], label='Categoria 2')
ax.plot(angulos, valores_categoria3 + [valores_categoria3[0]], label='Categoria 3')
ax.plot(angulos, valores_categoria4 + [valores_categoria4[0]], label='Categoria 4')
ax.plot(angulos, valores_categoria5 + [valores_categoria5[0]], label='Categoria 5')
ax.plot(angulos, valores_categoria6 + [valores_categoria6[0]], label='Categoria 6')

# Personalizar o gráfico
ax.set_xticks(angulos)
ax.set_xticklabels(variaveis)
ax.yaxis.grid(True)
ax.legend()

# Exibir o gráfico
plt.show()

#Gráfico de Gantt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Dados das tarefas
tarefas = ['Tarefa A', 'Tarefa B', 'Tarefa C', 'Tarefa D']
datas_inicio = ['2023-01-01', '2023-01-05', '2023-01-10', '2023-01-15']
duracoes = [5, 8, 6, 4]  # Duração em dias

# Converter as datas para o formato apropriado
datas_inicio = [mdates.datestr2num(data) for data in datas_inicio]

# Criar o gráfico de Gantt
fig, ax = plt.subplots()

# Configurar o eixo x como datas
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))

# Plotar as barras de tarefas
ax.barh(tarefas, duracoes, left=datas_inicio)

# Personalizar o gráfico
ax.set_xlabel('Data')
ax.set_ylabel('Tarefas')
ax.set_title('Gráfico de Gantt')

# Exibir o gráfico
plt.show()

#Gráfico de bolhas
import numpy as np
import matplotlib.pyplot as plt

# Dados das variáveis
x = np.random.rand(50)  # Valores para o eixo x
y = np.random.rand(50)  # Valores para o eixo y
tamanhos = np.random.rand(50) * 100  # Valores para o tamanho das bolhas

# Criar o gráfico de bolhas
plt.scatter(x, y, s=tamanhos, alpha=0.5)

# Personalizar o gráfico
plt.title('Gráfico de Bolhas')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Exibir o gráfico
plt.show()

#Gráfico de Sankey
import networkx as nx
import matplotlib.pyplot as plt

# Criar um objeto de grafo
G = nx.Graph()

# Adicionar nós ao grafo
G.add_nodes_from([1, 2, 3, 4, 5])

# Adicionar arestas ao grafo
G.add_edges_from([(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 5)])

# Layout do grafo
pos = nx.spring_layout(G)

# Desenhar os nós
nx.draw_networkx_nodes(G, pos)

# Desenhar as arestas
nx.draw_networkx_edges(G, pos)

# Adicionar rótulos aos nós
nx.draw_networkx_labels(G, pos)

# Exibir o grafo
plt.axis('off')
plt.show()

#Gráfico de cascata (waterfall chart)
import matplotlib.pyplot as plt

# Dados dos componentes
componentes = ['Receita', 'Custos', 'Impostos', 'Despesas', 'Lucro']
valores = [100, -50, -20, -30, 40]

# Calcular os níveis intermediários
niveis = [0] + [sum(valores[:i+1]) for i in range(len(valores)-1)]

# Criar o gráfico de cascata
plt.bar(componentes, valores, bottom=niveis, color=['g', 'r', 'r', 'r', 'b'])

# Personalizar o gráfico
plt.title('Gráfico de Cascata')
plt.xlabel('Componentes')
plt.ylabel('Valor')
plt.grid(True)

# Exibir o gráfico
plt.show()

#Gráfico de controle
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
dados = np.array([5.1, 5.3, 5.2, 5.4, 5.6, 5.3, 5.5, 5.2, 5.4, 5.6, 5.2, 5.3, 5.5])

# Média e desvio padrão dos dados
media = np.mean(dados)
desvio_padrao = np.std(dados)

# Limite superior e inferior de controle
limite_superior = media + 3 * desvio_padrao
limite_inferior = media - 3 * desvio_padrao

# Plotagem do gráfico de controle
plt.plot(dados, 'bo-', label='Dados')
plt.axhline(media, color='r', linestyle='-', linewidth=2, label='Média')
plt.axhline(limite_superior, color='g', linestyle='--', linewidth=1, label='Limite Superior de Controle')
plt.axhline(limite_inferior, color='g', linestyle='--', linewidth=1, label='Limite Inferior de Controle')

# Configurações do gráfico
plt.title('Gráfico de Controle para Dados Individuais')
plt.xlabel('Amostras')
plt.ylabel('Valores')
plt.legend()

# Exibição do gráfico
plt.show()

#Gráfico de densidade
import seaborn as sns
import matplotlib.pyplot as plt

# Dados de exemplo
dados = [1.2, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.3, 3.4]

# Criar o gráfico de densidade
sns.kdeplot(dados)

# Personalizar o gráfico
plt.title('Gráfico de Densidade')
plt.xlabel('Valores')
plt.ylabel('Densidade')

# Exibir o gráfico
plt.show()

#Gráfico de heat map
import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
dados = np.random.rand(5, 5)  # Matriz de valores aleatórios 5x5

# Criar o gráfico de heatmap
plt.imshow(dados, cmap='hot', interpolation='nearest')

# Personalizar o gráfico
plt.title('Gráfico de Heatmap')
plt.colorbar()

# Exibir o gráfico
plt.show()

#Gráficos compostos

#Gráfico de linhas com gráfico de barras
import matplotlib.pyplot as plt
import seaborn as sns

# Dados de exemplo
anos = [2010, 2011, 2012, 2013, 2014, 2015]
valores_linha = [50, 60, 55, 70, 80, 75]
valores_barra = [45, 55, 60, 65, 70, 75]

# Criar a figura e os eixos
fig, ax1 = plt.subplots()

# Plotar o gráfico de linhas
ax1.plot(anos, valores_linha, marker='o', color='blue')
ax1.set_xlabel('Anos')
ax1.set_ylabel('Valores Linha', color='blue')

# Plotar o gráfico de barras
ax2 = ax1.twinx()
ax2.bar(anos, valores_barra, alpha=0.5, color='red')
ax2.set_ylabel('Valores Barra', color='red')

# Personalizar o gráfico
plt.title('Gráfico de Linhas com Gráfico de Barras')
plt.grid(True)

# Exibir o gráfico
plt.show()

#Gráfico de dispersão com linha de regressão
import matplotlib.pyplot as plt
import seaborn as sns

# Dados de exemplo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [3, 5, 7, 8, 9, 10, 11, 13, 15, 16]

# Criar o gráfico de dispersão com linha de regressão
sns.regplot(x=x, y=y)

# Personalizar o gráfico
plt.title('Gráfico de Dispersão com Linha de Regressão')
plt.xlabel('Variável X')
plt.ylabel('Variável Y')

# Exibir o gráfico
plt.show()

#Gráfico de barras empilhadas
import matplotlib.pyplot as plt

# Dados de exemplo
categorias = ['A', 'B', 'C', 'D']
valores1 = [10, 15, 12, 8]
valores2 = [5, 8, 6, 9]
valores3 = [7, 9, 11, 6]

# Criar o gráfico de barras empilhadas
plt.bar(categorias, valores1, label='Grupo 1')
plt.bar(categorias, valores2, bottom=valores1, label='Grupo 2')
plt.bar(categorias, valores3, bottom=[i+j for i,j in zip(valores1, valores2)], label='Grupo 3')

# Personalizar o gráfico
plt.title('Gráfico de Barras Empilhadas')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.legend()

# Exibir o gráfico
plt.show()

#Gráfico de área empilhada"
import matplotlib.pyplot as plt

# Dados de exemplo
categorias = ['A', 'B', 'C', 'D']
valores1 = [10, 15, 12, 8]
valores2 = [5, 8, 6, 9]
valores3 = [7, 9, 11, 6]

# Criar o gráfico de área empilhada
plt.stackplot(categorias, valores1, valores2, valores3, labels=['Grupo 1', 'Grupo 2', 'Grupo 3'])

# Personalizar o gráfico
plt.title('Gráfico de Área Empilhada')
plt.xlabel('Categorias')
plt.ylabel('Valores')
plt.legend(loc='upper left')

# Exibir o gráfico
plt.show()

#Gráfico de barras e gráfico de setores
import matplotlib.pyplot as plt

# Dados de exemplo
categorias = ['A', 'B', 'C', 'D']
valores = [20, 35, 30, 15]

# Gráfico de barras
plt.subplot(121)
plt.bar(categorias, valores)
plt.title('Gráfico de Barras')

# Gráfico de setores
plt.subplot(122)
plt.pie(valores, labels=categorias, autopct='%1.1f%%')
plt.title('Gráfico de Setores')

# Ajustar o layout
plt.tight_layout()

# Exibir os gráficos
plt.show()

#Gráfico de dispersão com tamanho de bolhas
import matplotlib.pyplot as plt
import seaborn as sns

# Dados de exemplo
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 12, 8]
sizes = [30, 50, 20, 40, 10]

# Criar o gráfico de dispersão com tamanho de bolhas
plt.scatter(x, y, s=sizes)

# Personalizar o gráfico
plt.title('Gráfico de Dispersão com Tamanho de Bolhas')
plt.xlabel('Variável X')
plt.ylabel('Variável Y')

# Exibir o gráfico
plt.show()

