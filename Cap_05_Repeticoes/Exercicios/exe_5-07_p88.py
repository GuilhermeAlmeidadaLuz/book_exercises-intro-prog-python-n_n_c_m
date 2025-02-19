# Data: 06/02/2025

# ============ EXERCÍCIO 5.7 (PÁG. 88) ============
#
# n = int(input("Tabuada de: "))
# x = 1
# while x <= 10:
#     print(f'{n} x {x: >2} = {(n * x): >3}')
#     x += 1
#
# Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, em vez
# de começar com 1 e 10.
#
n = int(input("Tabuada de: "))
inicio = int(
    input(f"Digite o primeiro (1º) número que multiplicará >>> {n} <<<: "))
fim = int(input(f"Digite o último número que multiplicará >>> {n} <<<: "))

while inicio <= fim:
    print(f'{n: <2} x {inicio: >2} = {(n * inicio): >3}')
    inicio += 1
