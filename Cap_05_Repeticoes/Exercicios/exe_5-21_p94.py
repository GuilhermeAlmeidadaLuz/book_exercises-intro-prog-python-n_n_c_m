# Data: 25/03/2025

# ============ EXERCÍCIO 5.21 (PÁG. 94) ============

# Reescreva o Programa 5.1 de forma a continuar executando até que o valor digitado seja 0. Utilize
# repetições aninhadas.

# Programa 5.1 - Contagem de cédulas

while True:         # 1º while
    print(f"\n{'=' * 10} Programa 5.1 - Contagem de cédulas {'=' * 10}\n")
    valor = int(input("Digite o valor a pagar: "))
    cédulas = 0
    atual = 50
    apagar = valor

    if valor == 0:
        print(f"\n...Sem nenhum valor a pagar, finalizando programa de Contagem de Cédulas...\n")
        break       # interrompe 1º while
    else:
        pass

    while True:             # 2º while
        if atual <= apagar:
            apagar -= atual
            cédulas += 1
        else:
            print(f"{cédulas} cédula(s) de R$ {atual}")
            # bloco 1:
            if apagar == 0:
                break       # interrompe 2º while
            else:
                pass    # fim bloco 1

            # bloco 2:
            if atual == 50:
                atual = 20
            elif atual == 20:
                atual = 10
            elif atual == 10:
                atual = 5
            elif atual == 5:
                atual = 1
            # fim bloco 2

            cédulas = 0
