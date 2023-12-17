"""
Lista 6 - Programação Aplicada a Agricultura
Programa para plotar gráficos de dados de um silo de milho
Adriana Amaral - 96355
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# importar o arquivo
dadosTodos = pd.read_csv('Dados.csv', encoding = "ISO-8859-1",  sep=';')

if dadosTodos.empty:
    print('Arquivo não encontrado !!!')
    exit(0)

# converte DataFrame Pandas para Array Numpy
dadoNumerico = dadosTodos.to_numpy()

linha = 55*'_'

def graficoHoraTempAmbiente():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,1], 'r')
    plt.xlabel('Hora')
    plt.ylabel('Temperatura do ar ambiente (°C)')
    plt.title('Temperatura do ar ambiente')
    plt.grid(True)
    plt.show()

def graficoHoraUmidadeRelativaAmbiente():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,2], 'r')
    plt.xlabel('Hora')
    plt.ylabel('Umidade relativa do ar ambiente (%)')
    plt.title('Umidade relativa do ar ambiente')
    plt.grid(True)
    plt.show()

def graficoHoraTempAquecido():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,3], 'r')
    plt.xlabel('Hora')
    plt.ylabel('Temperatura do ar aquecido \napós passar pelo ventilador do silo (°C)')
    plt.title('Temperatura do ar aquecido \napós passar pelo ventilador do silo')
    plt.grid(True)
    plt.show()

def graficoHoraUmidadeRelativaAquecido():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,4], 'r')
    plt.xlabel('Hora')
    plt.ylabel('Umidade relativa do ar aquecido \napós passar pelo ventilador do silo (%)')
    plt.title('Umidade relativa do ar aquecido \napós passar pelo ventilador do silo')
    plt.grid(True)
    plt.show()

def graficoHoraTeorAguaEquilibrio():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,5], 'r')
    plt.xlabel('Hora')
    plt.ylabel('Teor de água de equilíbrio (%)')
    plt.title('Teor de água de equilíbrio')
    plt.grid(True)
    plt.show()

def graficoHoraAquecimentoResfriamento():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,6], 'r')
    plt.xlabel('Hora')
    plt.ylabel('Aquecimento ou resfriamento (°C)')
    plt.title('Aquecimento ou resfriamento')
    plt.grid(True)
    plt.show()

def graficoHoraTempAmbienteTempAquecido():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,1], 'r', label='Temperatura do ar ambiente')
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,3], 'b', label='Temperatura do ar aquecido \napós passar pelo ventilador do silo')
    plt.xlabel('Hora')
    plt.ylabel('Temperatura (°C)')
    plt.title('Temperatura do ar ambiente e Temperatura do ar \naquecido após passar pelo ventilador do silo')
    plt.legend()
    plt.grid(True)
    plt.show()

def graficoHoraUmidadeRelativaAmbienteUmidadeRelativaAquecido():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,2], 'r', label='Umidade relativa do ar ambiente')
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,4], 'b', label='Umidade relativa do ar aquecido \napós passar pelo ventilador do silo')
    plt.xlabel('Hora')
    plt.ylabel('Umidade relativa (%)')
    plt.title('Umidade relativa do ar ambiente e Umidade relativa do ar\naquecido após passar pelo ventilador do silo')
    plt.legend()
    plt.grid(True)
    plt.show()

def graficoHoraTempAmbienteUmidadeRelativaAmbiente():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,1], 'r', label='Temperatura do ar ambiente')
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,2], 'b', label='Umidade relativa do ar ambiente')
    plt.xlabel('Hora')
    plt.ylabel('Temperatura (°C) e Umidade relativa (%)')
    plt.title('Temperatura do ar ambiente e Umidade relativa do ar ambiente')
    plt.legend()
    plt.grid(True)
    plt.show()

def graficoHoraTempAquecidoUmidadeRelativaAquecido():
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,3], 'r', label='Temperatura do ar aquecido\napós passar pelo ventilador do silo')
    plt.plot(dadoNumerico[:,0], dadoNumerico[:,4], 'b', label='Umidade relativa do ar aquecido\napós passar pelo ventilador do silo')
    plt.xlabel('Hora')
    plt.ylabel('Temperatura (°C) e Umidade relativa (%)')
    plt.title('Temperatura do ar aquecido após passar pelo ventilador do silo\ne Umidade relativa do ar aquecido após passar pelo ventilador do silo')
    plt.legend()
    plt.grid(True)
    plt.show()

def menu():
    print(linha)
    print('{:^55s}'.format('ENG 390 - Programação Aplicada a Agricultura'))
    print(linha)
    print('{:^55s}'.format('Menu'))
    print(linha)
    print('{:<55s}'.format('1. Hora versus Temperatura do ar ambiente'))
    print('{:<55s}'.format('2. Hora versus Umidade relativa do ar ambiente'))
    print('{:<55s}'.format('3. Hora versus Temperatura do ar aquecido após\n   passar pelo ventilador do silo'))
    print('{:<55s}'.format('4. Hora versus Umidade relativa do ar aquecido após\n   passar pelo ventilador do silo'))
    print('{:<55s}'.format('5. Hora versus Teor de água de equilíbrio'))
    print('{:<55s}'.format('6. Hora versus Aquecimento ou resfriamento'))
    print('{:<55s}'.format('7. Hora versus Temperatura do ar ambiente e Temperatura do ar\n   aquecido após passar pelo ventilador do silo'))
    print('{:<55s}'.format('8. Hora versus Umidade relativa do ar ambiente e Umidade relativa do ar\n   aquecido após passar pelo ventilador do silo'))
    print('{:<55s}'.format('9. Hora versus Temperatura do ar ambiente e Umidade relativa do ar ambiente'))
    print('{:<55s}'.format('10. Hora versus Temperatura do ar aquecido após passar pelo ventilador do silo\n    e Umidade relativa do ar aquecido após passar pelo ventilador do silo'))
    print(linha)
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 1:
        graficoHoraTempAmbiente()
    elif opcao == 2:
        graficoHoraUmidadeRelativaAmbiente()
    elif opcao == 3:
        graficoHoraTempAquecido()
    elif opcao == 4:
        graficoHoraUmidadeRelativaAquecido()
    elif opcao == 5:
        graficoHoraTeorAguaEquilibrio()
    elif opcao == 6:
        graficoHoraAquecimentoResfriamento()
    elif opcao == 7:
        graficoHoraTempAmbienteTempAquecido()
    elif opcao == 8:
        graficoHoraUmidadeRelativaAmbienteUmidadeRelativaAquecido()
    elif opcao == 9:
        graficoHoraTempAmbienteUmidadeRelativaAmbiente()
    elif opcao == 10:
        graficoHoraTempAquecidoUmidadeRelativaAquecido()
    else:
        print('Opção inválida')

menu()