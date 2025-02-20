# Data: 18/02/2025

# ============ EXERCÍCIO 5.11 (PÁG. 90) ============

'''Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança. Exiba os valores 
mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.'''

depositoInicial = float(input("Digite o seu depósito inicial: "))
txJurosMes = float(input(f"Digite a taxa de juros (0% - ... %): "))
print(f"Você definiu a taxa de Juros para {txJurosMes:5.2f}%"
      "\n")

mes = 1  # mês é um contador
poupanca = depositoInicial  # poupança é um acumulador
while mes <= 24:
    poupanca = poupanca + (poupanca * (txJurosMes/100))
    print(f"Valor no final do {mes}° mês: {poupanca: 5.2f}", end="\n")
    mes = mes + 1
print("\n"
      f"O total ganho com juros no período de 24 meses é: {(poupanca - depositoInicial): .2f}"
      "\n")
