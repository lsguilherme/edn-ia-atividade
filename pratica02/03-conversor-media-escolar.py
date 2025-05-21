"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""
print("-=-=-=- Calculador de Média Escolar -=-=-=-")
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = round((nota1 + nota2 + nota3) / 3, 2)

print(f"Primeira nota: {nota1:.2f}\nSegunda nota: {nota2:.2f}\nTerceira nota: {nota3:.2f}")
print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"Média final: {media:.2f}")