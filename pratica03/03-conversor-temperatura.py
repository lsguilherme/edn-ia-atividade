"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
print("-=-=-=- Conversor de Temperatura -=-=-=-")

temperatura = float(input("Digite a temperatura: "))

unidade_origem = input("Informe a unidade de origem (C, F ou K): ").upper()

unidade_destino = input("Informe a unidade de destino (C, F ou K): ").upper()

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
if unidade_origem == unidade_destino:
    resultado = temperatura
elif unidade_origem == "C":
    if unidade_destino == "F":
        resultado = (temperatura * 9/5) + 32
    else:
        resultado = temperatura + 273.15
elif unidade_origem == "F":
    if unidade_destino == "C":
        resultado = (temperatura - 32) * 5/9
    else:
        resultado = (temperatura - 32) * 5/9 + 273.15
elif unidade_origem == "K":
    if unidade_destino == "C":
        resultado = temperatura - 273.15
    else:
        resultado = (temperatura - 273.15) * 9/5 + 32

if unidade_origem in ["C", "F", "K"] and unidade_destino in ["C", "F", "K"]:
    print(f"{temperatura:.2f} {unidade_origem} = {resultado:.2f} {unidade_destino}")
else:
    print("Unidade inválida. Use C, F ou K.")