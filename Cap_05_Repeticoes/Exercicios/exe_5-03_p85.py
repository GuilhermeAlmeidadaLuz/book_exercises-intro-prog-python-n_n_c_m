# Data: 04/01/2024

# ============ EXERCÍCIO 5.3 (PÁG 85) ============

# Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve
# imprimir 10, 9, 8, ... , 1, 0 e Fogo! na tela.

contagem = 10
while contagem >= 0:
    print(contagem)
    contagem = contagem - 1
print('Fogo!')
