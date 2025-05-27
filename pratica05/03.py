"""
Crie uma função que calcule a idade de uma pessoa em dias baseada no ano de nascimento.
"""

from datetime import datetime

def calcular_idade_em_dias(ano_de_nascimento):
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_de_nascimento
    idade_dias = idade_anos * 365 
    return idade_dias

print(calcular_idade_em_dias(2001))