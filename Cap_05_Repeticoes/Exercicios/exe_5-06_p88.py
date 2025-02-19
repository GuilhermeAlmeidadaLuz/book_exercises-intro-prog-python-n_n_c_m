# Data: 06/02/2025

# ============ EXERCÍCIO 5.6 (PÁG. 88) ============
#
# n = int(input("Tabuada de: "))
# x = 1
# while x <= 10:
#     print(n + x)
#     x = x + 1
#
# Altere o programa anterior para exibir os resultados no mesmo formato de uma tabuada: 2x1 = 2, 2x2 = 4,
# ...
#

n = int(input("Tabuada de: "))
x = 1
while x <= 10:
    print(f'{n} x {x: >2} = {(n * x): >3}')
    x += 1
