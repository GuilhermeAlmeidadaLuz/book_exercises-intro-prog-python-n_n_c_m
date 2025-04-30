# Programa 6.3 – Apresentação de números
números = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    números[x] = int(input(f"Número {x + 1}:"))
    x += 1
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número: {números[escolhido - 1]}")
