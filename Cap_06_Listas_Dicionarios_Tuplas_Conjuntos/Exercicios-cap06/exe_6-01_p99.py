# Data: 27/03/2025

# ============ EXERCÍCIO 6.01 (PÁG. 99) ============

# Modifique o Programa 6.2 para ler 7 notas em vez de 5.

# Programa 6.2 - Cálculo da média com notas digitadas
# notas = [0, 0, 0, 0, 0]
# soma = 0
# x = 0
# while x < 5:
#     notas[x] = float(input(f"Nota {x}:"))
#     soma += notas[x]
#     x += 1
# x = 0
# while x < 5:
#     print(f"Nota {x}: {notas[x]:6.2f}")
#     x += 1
# print(f"Média: {soma / x:5.2f}")

print(f"\n{'=' * 5} Cálculo da média com 7 notas digitadas {'=' * 5}\n")
notas = [0]*7
soma = 0
x = 0
while x < 7:
    notas[x] = float(input(f"Nota {x}: "))
    soma += notas[x]
    x += 1
print()
x = 0
while x < 7:
    print(f"Nota {x}: {notas[x]:6.2f}")
    x += 1
print(f"\nMedia: {soma / x:5.2f}")
