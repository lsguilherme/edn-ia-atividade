"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

def consultar_cep():
  print("-=-=-=- Consulta de CEP -=-=-=-")
  cep = input("Digite o CEP: ")
  url = f"https://viacep.com.br/ws/{cep}/json/"

  response = requests.get(url)
  data = response.json()

  print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
  print(f"CEP: {data['cep']}")
  print(f"Logradouro: {data['logradouro']}")
  print(f"Bairro: {data['bairro']}")
  print(f"Cidade: {data['localidade']}")
  print(f"Estado: {data['uf']}")
  print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

# Executar a função para consultar o CEP
consultar_cep()
