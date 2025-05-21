# 4 - Calculadora de Preço Total

print("-=-=-=- Calculadora de Preço Total -=-=-=-")

preco_unitario = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade de produto comprada: "))
preco_total = preco_unitario * quantidade

print("Preço total da compra:", preco_total)