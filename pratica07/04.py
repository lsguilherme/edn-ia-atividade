"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
"""

import json

def escreve_json(nome_arquivo, dados):
  with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
    json.dump(dados, arquivo_json, ensure_ascii=False, indent=2)
  print(f"Dados escritos em '{nome_arquivo}'")

def ler_json(nome_arquivo):
  try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
      dados = json.load(arquivo_json)
      print(f"Dados do arquivo '{nome_arquivo}':")
      print(json.dumps(dados, ensure_ascii=False, indent=2))
  except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

dados = {
    "nome": "Guilherme",
    "idade": 23,
    "cidade": "Recife"
}

escreve_json('pessoa.json', dados)
print('----------------------------------')

ler_json('pessoa.json')