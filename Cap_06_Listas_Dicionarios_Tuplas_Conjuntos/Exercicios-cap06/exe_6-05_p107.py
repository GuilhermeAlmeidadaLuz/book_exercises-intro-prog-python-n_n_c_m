# Data: 29/04/2025

# ============ EXERCÍCIO 6.05 (PÁG. 107) ============

''' Altere o Programa 6.7 de forma a poder trabalhar com vários comandos digitados de uma só vez. 
Atualmente, apenas um comando pode ser inserido por vez. Altere-o de forma a considerar operação 
como uma string.
Exemplo: FFFAAAS significaria três chegadas de novos clientes, três atendimentos e, finalmente, a 
saída do programa

# programa 6.7 - Simulação de uma fila de banco
último = 10
fila = list(range(1, último + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operação "
                     "(F, A ou S): ")
    if operação == "A":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif operação == "F":
        último += 1         # incrementa o ticket do novo cliente
        fila.append(último)
    elif operação == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")
'''

último = 10
fila = list(range(1, último + 1))
while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila,")
    print("ou A para realizar o atendimento. S para sair.")
    operação = input("Operaração (F, A ou S) - uma ou mais, exemplo 'FFAAS': ")
    contador = 0
    # percorrerá a cadeia de caracteres, sendo atribuído ao contador um índice dela a cada repetição
    while contador < len(operação):
        if operação[contador] == "A":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif operação[contador] == "F":
            último += 1     # incrementa o ticket do novo cliente
            fila.append(último)     # incluído no final da fila
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        contador += 1       # incrementa o contador para o próximo índice da string 'operação', quando contador == 5, sai do laço de repetição
    if (operação[contador-1] == "S"):
        break