"""
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. O programa deve exibir o nome, email e país do usuário gerado."
"""
import requests

def gerar_perfil_usuario():
  url = "https://randomuser.me/api/"
  response = requests.get(url)
  data = response.json()
  usuario = data['results'][0]
  
  nome = f"{usuario['name']['first']} {usuario['name']['last']}"
  email = usuario['email']
  pais = usuario['location']['country']

  print("-=-=-=- Perfil de Usuário Aleatório -=-=-=-")
  print(f"Nome: {nome}")
  print(f"Email: {email}")
  print(f"País: {pais}")
  print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

gerar_perfil_usuario()
