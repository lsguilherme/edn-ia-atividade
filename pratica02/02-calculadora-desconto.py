"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""
print("-=-=-=- Calculador de Desconto -=-=-=-")

produto = "Camiseta"
preco_original = 50.00
porcentagem = 0.2

preco_final = round(preco_original - (preco_original * porcentagem), 2)
print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Valor do desconto: {int(porcentagem * 100)}%")
print("-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(f"Preço final: R$ {preco_final:.2f}")