# Data: 25/03/2025

# ============ EXERCÍCIO 5.17 (PÁG. 93) ============

# O que acontece se digitarmos 0 (zero) no valor a pagar?
#
# Resposta =>   Será efetuada a verificação no 1º 'if' que se encontra na linha seguinte a instrução 'while', que retorna 'False' pois a variável
#               'atual = 50' não é menor ou igual que a variável 'apagar = 0', portanto, esse bloco não é executado e entra no bloco de instruções
#               do 1º 'else', imprime a mensagem que informa a quantidade de cédulas utilizadas (qtd = 0 cédulas) da variável 'atual = 50' para
#               abater do valor a pagar e em seguida entra em outro bloco de instrução de um 2º 'if', que tem a vericação com retorno 'True', pois
#               a variável 'apagar = 0' que recebeu 0 satisfaz a condição 'apagar == 0', e então, o comando 'break' é efetuado, interrompendo o fluxo
#               do programa.

# Programa 5.1 - Contagem de cédulas
print(f"\n{'=' * 10} Programa 5.1 - Contagem de cédulas {'=' * 10}\n")
valor = int(input("Digite o valor a pagar: "))
cédulas = 0                     # quantidade de cédulas para pagar o valor
# inicia com cédula com quantia de R$ 50,00. Prioridade da maior para a menor na contagem de cédulas
atual = 50
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

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 50, altera 'atual' para '20' (a próxima cédula de maior valor)
        if atual == 50:
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
