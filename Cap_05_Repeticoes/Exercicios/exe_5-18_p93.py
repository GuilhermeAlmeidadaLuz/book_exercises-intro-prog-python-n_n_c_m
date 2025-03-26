# Data: 25/03/2025

# ============ EXERCÍCIO 5.18 (PÁG. 93) ============

#  Modifique o programa para também trabalhar com notas de R$ 100.

# Programa 5.1 - Contagem de cédulas
print(f"\n{'=' * 10} Programa 5.1 - Contagem de cédulas {'=' * 10}\n")
valor = int(input("Digite o valor a pagar: "))
cédulas = 0                     # quantidade de cédulas para pagar o valor
# inicia com cédula com quantia de R$ 100,00. Prioridade da maior para a menor na contagem de cédulas
atual = 100
apagar = valor                  # valor a ser pago inicializado na variável 'apagar'

while True:
    if atual <= apagar:         # efetua esse bloco 'if' quando cédula 'atual' é menor ou igual que o valor a pagar no momento, portanto, 'atual' pode descontar do valor que está em 'apagar'
        apagar -= atual         # utilizou a variável 'atual' - que representa a cédula do momento - para descontar do valor a pagar que se encontra na variável 'apagar'
        cédulas += 1            # contabiliza mais 1 cédula utilizada da cédula 'atual'

    else:
        print(f"{cédulas} cédula(s) de R$ {atual}")

        # if para variável 'apagar':
        if apagar == 0:
            break               # quando o valor a ser pago é zero, interrompe-se o fluxo do 'while' com o comando 'break'

        # ifs e elifs para variável 'atual':

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 100, altera 'atual' para '50' (a próxima cédula de maior valor)
        if atual == 100:
            atual = 50

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 50, altera 'atual' para '20' (a próxima cédula de maior valor)
        elif atual == 50:
            atual = 20          # atual recebe 20

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 20, altera 'atual' para '10' (a próxima cédula de maior valor)
        elif atual == 20:
            atual = 10          # atual recebe 10

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 10, altera 'atual' para '5' (a próxima cédula de maior valor)
        elif atual == 10:
            atual = 5           # atual recebe 5

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 5, altera 'atual' para '5' (a próxima cédula de maior valor)
        elif atual == 5:
            atual = 1           # atual recebe 1 - última cédula útil

        # a quantidade de cédulas usadas de 'atual' é zerada para contagem com novo valor de atual (valor da cédula no momento)
        cédulas = 0
print()
