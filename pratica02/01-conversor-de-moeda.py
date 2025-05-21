"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""
print("-=-=-=- Conversor de Moeda -=-=-=-")

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

print(f"R$ {valor_reais:.2f} equivalem a US$ {valor_dolar:.2f}")
print(f"R$ {valor_reais:.2f} equivalem a € {valor_euro:.2f}")