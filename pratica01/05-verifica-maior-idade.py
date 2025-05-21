# Crie um exemplo prático que verifica se uma pessoa antigiu a maioridade (18 anos ou mais) e exibe uma mensagem apropriada.
print("-=-=-=- Verificador de Maioridade -=-=-=-")

idade = int(input("Digite a idade da pessoa: "))

if idade >= 18:
  print("A pessoa atingiu a maioridade.")
else:
  print("A pessoa ainda não atingiu a maioridade.")