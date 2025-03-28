# Data: 10/03/2025

# ============ EXERCÍCIO 5.16 (PÁG. 93) ============

# Execute o Programa 5.1 para os seguintes valores: 501, 745, 384, 2, 7 e 1

# Programa 5.1 - Contagem de cédulas
print(f"\n{ '=' * 10} Programa 5.1 - Contagem de cédulas { '=' * 10 }\n")
valor = int(input("Digite o valor a pagar: "))
cédulas = 0                     # quantidade de cédulas para pagar o valor
atual = 50                      # inicia com cédula com quantia de R$ 50,00. Prioridade da maior para a menor na contagem de cédulas
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
        
        # if e elifs para variável 'atual':
        
        if atual == 50:         # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 50, altera 'atual' para '20' (a próxima cédula de maior valor) 
            atual = 20          # atual recebe 20
        
        elif atual == 20:       # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 20, altera 'atual' para '10' (a próxima cédula de maior valor)
            atual = 10          # atual recebe 10
        
        elif atual == 10:       # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 10, altera 'atual' para '5' (a próxima cédula de maior valor)
            atual = 5           # atual recebe 5
        
        elif atual == 5:        # após verificar que 'atual <= apagar' retorna 'False' para 'atual' == 5, altera 'atual' para '5' (a próxima cédula de maior valor)
            atual = 1           # atual recebe 1 - última cédula útil
 
        cédulas = 0             # a quantidade de cédulas usadas de 'atual' é zerada para contagem com novo valor de atual (valor da cédula no momento)
print()