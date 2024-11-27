# Data: 21/10/2024

# ============ EXERCÍCIO 4.4 (PÁG 79) ============

# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("\nQual seu salário: R$ "))
aumento = 0
if salario > 1250:
    percentual = 0.10
    aumento = (salario * percentual)
if salario <= 1250:
    percentual = 0.15
    aumento = (salario * percentual)
print(f"\nPara o salario de R$ {salario:.2f}, o aumento é de R$ {aumento:.2f}\n")

# salário = float(input("Digite seu salário: "))
# pc_aumento = 0.15
# if salário > 1250:
#     pc_aumento = 0.10
# aumento = salário * pc_aumento
# print(f"Seu aumento será de: R$ {aumento:7.2f}")
