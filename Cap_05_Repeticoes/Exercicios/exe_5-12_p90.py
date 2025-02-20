# Data: 19/02/2025

# ============ EXERCÍCIO 5.12 (PÁG. 90) ============

# depositoInicial = float(input("Digite o seu depósito inicial: "))
# txJurosMes = float(input(f"Digite a taxa de juros (0% - ... %): "))
# print(f"Você definiu a taxa de Juros para {txJurosMes:5.2f}%"
#       "\n")

# mes = 1  # mês é um contador
# poupanca = depositoInicial  # poupança é um acumulador
# while mes <= 24:
#     poupanca = poupanca + (poupanca * (txJurosMes/100))
#     print(f"Valor no final do {mes}° mês: {poupanca: 5.2f}", end="\n")
#     mes = mes + 1
# print("\n"
#       f"O total ganho com juros no período de 24 meses é: {(poupanca - depositoInicial): .2f}"
#       "\n")

'''Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será 
depositado no início de cada mês, e você deve considerá-lo para o cálculo de juros do mês seguinte.'''

depositoInicial = float(input("Digite o seu depósito inicial: "))
txJurosMes = float(input(f"Digite a taxa de juros (0% - ... %): "))
print(f"Você definiu a taxa de Juros ao mês como: {txJurosMes:5.2f}%"
      "\n")
depositoMensal = float(
    input("Digite o valor que será depositado no início de cada mês: "))

mes = 1  # mês é um contador
poupanca = depositoInicial  # poupança é um acumulador
while mes <= 24:
    # cálculo em cima do valor base (depósito inicial) que resulta no valor de rendimento
    poupanca = poupanca + (poupanca * (txJurosMes/100))
    # acréscimo do depósito mensal sobre o que já rendeu
    poupanca = poupanca + depositoMensal
    print(f"Valor no final do {mes}° mês: {poupanca: 5.2f}", end="\n")
    mes = mes + 1
print("\n"
      f"O total ganho com juros no período de 24 meses é: {(poupanca - depositoInicial): .2f}"
      "\n")
