# Data: 25/03/2025

# ============ EXERCÍCIO 5.19 (PÁG. 93) ============

#  Modifique o programa para aceitar valores decimais, ou seja, também contar moedas de 0,01, 0,02, 0,05, 0,10 e 0,50

''' Obs: alguns valores não serão calculados corretamente 
    devido a problemas com arredondamento e da representação de 0.01 
    em ponto flutuante. Uma alternativa é multiplicar todos os valores 
    por 100 e realizar todos os cálculos com números inteiros. '''

# Programa 5.1 - Contagem de cédulas
print(f"\n{'=' * 10} Programa 5.1 - Contagem de cédulas {'=' * 10}\n")
valor = float(input("Digite o valor a pagar: "))
cédulas = 0                     # quantidade de cédulas para pagar o valor
# inicia com cédula com quantia de R$ 100,00. Prioridade da maior para a menor na contagem de cédulas
atual = 100
apagar = valor                  # valor a ser pago inicializado na variável 'apagar'

while True:
    if atual <= apagar:         # efetua esse bloco 'if' quando cédula 'atual' é menor ou igual que o valor a pagar no momento, portanto, 'atual' pode descontar do valor que está em 'apagar'
        apagar -= atual         # utilizou a variável 'atual' - que representa a cédula do momento - para descontar do valor a pagar que se encontra na variável 'apagar'
        cédulas += 1            # contabiliza mais 1 cédula utilizada da cédula 'atual'

    else:
        if atual >= 1:
            print(f"{cédulas} cédula(s) de R$ {atual}")
        else:
            print(f"{cédulas} moeda(s) de {atual:5.2f}")

        # if para variável 'apagar':
        if apagar < 0.01:       # por conta do float não gerar correspondência exata, o valor estará entre 0.0 e 0.01, sendo ele bem próximo do 0.0
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
            atual = 1           # atual recebe 1

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 1, altera 'atual' para '0.5' (a próxima cédula de maior valor)
        elif atual == 1:
            atual = 0.50         # atual recebe 0.50 - moeda

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 0.50, altera 'atual' para '0.10' (a próxima cédula de maior valor)
        elif atual == 0.50:
            atual = 0.10        # atual recebe 0.10 - moeda

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 0.10, altera 'atual' para '0.05' (a próxima cédula de maior valor)
        elif atual == 0.10:
            atual = 0.05        # atual recebe 0.05 - moeda

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 0.05, altera 'atual' para '0.02' (a próxima cédula de maior valor)
        elif atual == 0.05:
            atual = 0.02        # atual recebe 0.02 - moeda

        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 0.02, altera 'atual' para '0.01' (a próxima cédula de maior valor)
        elif atual == 0.02:
            atual = 0.01        # atual recebe 0.01 - moeda

        # a quantidade de cédulas usadas de 'atual' é zerada para contagem com novo valor de atual (valor da cédula no momento)
        cédulas = 0

print()
