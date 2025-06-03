"""
Leia um arquivo que contém dados de log de treinamento de modelos de Machine Learning. Calcule a média e o desvio padrão do tempo de execução constantes. 
"""

import pandas as pd

def logs_treinamento_ml(caminho_arquivo):
  try:
    df = pd.read_csv(caminho_arquivo)
    media = df['tempo_execucao'].mean()
    desvio_padrao_tempo = df['tempo_execucao'].std()
    print(f"Média: {media:.2f} segundos.")
    print(f"Desvio padrão do tempo de execução: {desvio_padrao_tempo:.2f} segundos.")
  except FileNotFoundError:
    print("Arquivo não encontrado ou caminho incorreto.")

logs_treinamento_ml('logs_treinamento.csv')
