# Data: 05/02/2025

# ============ EXERCÍCIO 5.5 (PÁG. 87) ============

# fim = int(input('Digite o último número a imprimir: '))
# x = 0
# while x <= fim:
#     if x % 2 != 0:
#         print(x)
#     x = x + 1

# Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.

contador = 1
dezMultiplos = 10
x = 1
while contador <= dezMultiplos:
    if x % 3 == 0:
        print(x)
        contador += 1
    x = x + 1
