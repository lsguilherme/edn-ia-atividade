"""
Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""

import csv

def ler_csv_pessoas(nome_arquivo):
  try:
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo_csv:
      reader = csv.reader(arquivo_csv)
      for linha in reader:
        print(linha)
  except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

ler_csv_pessoas('pessoas.csv')