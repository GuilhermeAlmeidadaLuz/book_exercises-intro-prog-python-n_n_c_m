# Data: 10/03/2025

# ============ EXERCÍCIO 5.14 (PÁG. 91) ============

'''Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o 
usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a 
soma e a média aritmética.'''

qtd_nums = 0
soma = 0

while True:
    num = int(input("Digite um número inteiro: "))
    if num == 0:
        print("Finalizando operação...")
        break
    else:
        qtd_nums += 1
        soma += num
media_aritm = soma / qtd_nums
print(f'Quantidade de números digitados: {qtd_nums}\n'
      f'Soma: {soma}', '\n'
      f'Média Aritmética: {media_aritm:8.2f}', '\n')