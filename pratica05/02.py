"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaço e pontuação). Se o resultado é True, responda "Sim", se o resultado for False, responda "Não
"""

def verifica_palindromo(texto):
  texto_lower = texto.lower()
  if texto_lower == texto_lower[::-1]:
    return "Sim"
  else:
    return "Não"

print(verifica_palindromo("Ana"))
print(verifica_palindromo("Teste"))