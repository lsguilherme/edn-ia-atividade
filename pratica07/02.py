"""
Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""

import csv

def escrever_csv_pessoas(nome_arquivo, dados):
  with open(nome_arquivo, mode="w", newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerows(dados)
  print("Dados escritos em: ", nome_arquivo)

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Guilherme", 23, "Recife"],
    ["Gustavo", 30, "São Paulo"]
]

escrever_csv_pessoas('pessoas.csv', dados)