# Data: 10/03/2025

# ============ EXERCÍCIO 5.15 (PÁG. 92) ============

''' Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário 
que digite o código do produto e a quantidade comprada. Utilize a tabela de códigos a seguir para obter o 
preço de cada produto:
|Código | Preço 
|   1   |  0,50 
|   2   |  1,00 
|   3   |  4,00 
|   5   |  7,00 
|   9   |  8,00
Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve 
gerar a mensagem de erro “Código inválido”. '''

#
#

print(f'\n{'=' * 10} Máquina Registradora de Compras {'=' * 10}\n')
total_compras = 0
preco = 0
while True:
    cod_produto = int(input("Digite o código do produto: "))

    if cod_produto == 0:
        break
    elif cod_produto == 1:
        preco = 0.5
        qtd_comprada = int(input("Digite a quantidade comprada: "))
        total_compras += preco * qtd_comprada
        print("...enviado para o carrinho de compras...\n")
    elif cod_produto == 2:
        preco = 1
        qtd_comprada = int(input("Digite a quantidade comprada: "))
        total_compras += preco * qtd_comprada
        print("...enviado para o carrinho de compras...\n")
    elif cod_produto == 3:
        preco = 4
        qtd_comprada = int(input("Digite a quantidade comprada: "))
        total_compras += preco * qtd_comprada
        print("...enviado para o carrinho de compras...\n")
    elif cod_produto == 5:
        preco = 7
        qtd_comprada = int(input("Digite a quantidade comprada: "))
        total_compras += preco * qtd_comprada
        print("...enviado para o carrinho de compras...\n")
    elif cod_produto == 9:
        preco = 8
        qtd_comprada = int(input("Digite a quantidade comprada: "))
        total_compras += preco * qtd_comprada
        print("...enviado para o carrinho de compras...\n")
    else:
        print('Erro: .... Código inválido .... falha ao enviar para o carrinho de compras ....\n')
print(f'{'=' * 50}')
print(f'Total do carrinho de compras: R$ {total_compras:>8.2f}\n')
