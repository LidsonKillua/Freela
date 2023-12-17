# Title: LISTA DE EXERCÍCIO 5 – Estatística – Bibliotecas Numpy & Pandas
# Description:
#   Este programa lê um arquivo CSV contendo dados de temperatura e umidade relativa do ar e cria um dataframe com os dados.
#   Além disso, o programa adiciona novas linhas contendo os valores mínimo e máximo, a média, o desvio padrão e o coeficiente 
#   de variação das variáveis Tamb, URamb, Aqv, Taqv, URaqv e Aqq.


import pandas as pd
import numpy as np
import os

def ler_arquivo():
    arquivo = input("Digite o nome do arquivo: ")

    while not os.path.exists(arquivo) or not arquivo.endswith('.csv'):
        print("Arquivo inválido")
        arquivo = input("Digite o nome do arquivo: ")

    return pd.read_csv(arquivo)
    
def criar_dataframe(dados):
    df = pd.DataFrame(dados, columns=['Tamb', 'URamb', 'Taqv', 'URaqv', 'UEaqv', 'Aqq'])

    # Ajustando o índice para começar de 1
    df.index = df.index + 1
    
    # Formatando as colunas
    df['Tamb'] = df['Tamb'].map('{:,.2f}'.format)
    df['URamb'] = df['URamb'].map('{:,.2f}'.format)
    df['Taqv'] = df['Taqv'].map('{:,.2f}'.format)
    df['URaqv'] = df['URaqv'].map('{:,.2f}'.format)
    df['UEaqv'] = df['UEaqv'].map('{:,.2f}'.format)
    df['Aqq'] = df['Aqq'].map('{:,.2f}'.format)

    return df
    
def apresentar_tabela(df):     
    print("=-"*30)
    print(df)
    print("=-"*30)

def totalizarDados(df):    
    # Convertendo as colunas para numéricas
    dfnum = df.apply(pd.to_numeric, errors='ignore')
    
    # Criando as novas linhas com numpy
    dfnum.loc['mínimo'] = np.min(dfnum.values, axis=0)
    dfnum.loc['máximo'] = np.max(dfnum.values, axis=0)
    dfnum.loc['média'] = np.mean(dfnum.values, axis=0)
    dfnum.loc['Desvio padrão'] = np.std(dfnum.values, axis=0)
    dfnum.loc['Coeficiente de variação'] = np.std(dfnum.values, axis=0) / np.mean(dfnum.values, axis=0)
    
    df2 = df.copy()

    # Formatando as linhas novas
    df2.loc['mínimo'] = dfnum.loc['mínimo'].map('{:,.2f}'.format)
    df2.loc['máximo'] = dfnum.loc['máximo'].map('{:,.2f}'.format)
    df2.loc['média'] = dfnum.loc['média'].map('{:,.2f}'.format)
    df2.loc['Desvio padrão'] = dfnum.loc['Desvio padrão'].map('{:,.2f}'.format)
    df2.loc['Coeficiente de variação'] = dfnum.loc['Coeficiente de variação'].map('{:,.2f}'.format)

    return df2

def gravar_arquivo(dados):
    arquivo = input("Digite o nome do arquivo: ")
    dados.to_csv(arquivo, index=False)
    print("Arquivo gravado com sucesso")


###
# Programa principal
###

dados = ler_arquivo()

# Criando o dataframe
df = criar_dataframe(dados)
# DataFrame com os dados totalizados   
dfTotalizado = totalizarDados(df)

opcao = 0

# O programa entra em um loop enquanto a opção não for 4 (que é a opção para sair)
while opcao != 4:
    print("1 - Apresentar tabela com os dados lidos do arquivo CSV")
    print("2 - Apresentar tabela com os dados totalizados")
    print("3 - Gravar arquivo CSV com os dados totalizados")
    print("4 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        apresentar_tabela(df)
    elif opcao == 2:
        apresentar_tabela(dfTotalizado)
    elif opcao == 3:
        gravar_arquivo(dfTotalizado)
    elif opcao == 4:
        print("Fim do programa")
    else:
        print("Opção inválida")