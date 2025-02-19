# Data: 05/02/2025

# ============ EXERCÍCIO 5.4 (PÁG. 87) ============
#
# fim = int(input("Digite o último número a imprimir:"))
# x = 0
# while x <= fim:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1
#
# fim = int(input("Digite o último número a imprimir:"))
# x = 0
# while x <= fim:
#     print(x)
#     x = x + 2
#
# Modifique o programa anterior para imprimir de 1 até o número digitado pelo usuário, mas, dessa vez,
# apenas os números 'ímpares'

fim = int(input('Digite o último número que limita o que pode ser impresso: '))
x = 1
while x <= fim:
    if x % 2 != 0:
        print(x)
    x = x + 1
