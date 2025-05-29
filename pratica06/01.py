"""
Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória. 
"""

import random
import string

def gerar_senha(tamanho):
  caracteres = string.ascii_letters + string.digits + string.punctuation
  senha = ""
  for _ in range(tamanho):
    senha += random.choice(caracteres)
  return senha

print("-=-=-=- Gerador de Senha Aleatória -=-=-=-")
tamanho_senha = int(input("Digite a quantidade de caracteres para a senha: "))
senha_gerada = gerar_senha(tamanho_senha)
print(f"Sua senha aleatória é: {senha_gerada}")