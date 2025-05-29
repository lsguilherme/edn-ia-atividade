"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
"""
import requests

def consultar_cotacao_moeda(moeda):
  url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

  resposta = requests.get(url)
  dados = resposta.json()
  
  chave = f"{moeda}BRL"

  cotacao = dados[chave]
  print(f"\nCotação de {moeda} para BRL:")
  print(f"Valor atual: R${cotacao['bid']}")
  print(f"Valor mínimo: R${cotacao['low']}")
  print(f"Valor máximo: R${cotacao['high']}")
  print(f"Última atualização: {cotacao['create_date']}")

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
consultar_cotacao_moeda(moeda)
