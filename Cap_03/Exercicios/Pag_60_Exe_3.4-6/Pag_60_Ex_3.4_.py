# Guilherme Almeida da Luz

# Exercício 3.4 - Escreva uma expressão para determinar se uma pessoa deve
# ou não pagar imposto. Considere que pagam imposto pessoas cujo salário é
# maior que R$ 1.200,00.

salário = float(input("Digite seu salário: "))

pagar = salário > 1_200.00

print("Deve pagar imposto: ", pagar)

print("Deve pagar imposto: ", pagar and pagar)

print("Deve pagar imposto: ", salário > 1_200.00 and salário > 1_200.00)