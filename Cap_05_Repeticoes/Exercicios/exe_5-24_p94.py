# Data: 26/03/2025

# ============ EXERCÍCIO 5.24 (PÁG. 94) ============

# Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos.

n = int(input("Digite um número: "))
if n < 0:
    print('Inválido, digite um número positivo')
else:
    contador = 1
    numero = 3
    while contador <= n:
        if contador == 1:
            print(f'{contador:>}º número primo: {2:>}')
            contador += 1
        else:
            divisor = 3
            while divisor <= numero:
                if numero % divisor == 0:
                    break
                divisor += 2
            if numero == divisor:
                print(f'{contador:>4}º número primo: {numero:>4}')
                numero += 2
                contador += 1
            else:
                numero += 2

# Obs.: abordagem pela contagem de divisores de um número primo (2 divisores: 1 e ele mesmo), que tem mais custo computacional dentro do 'while'
#       foi abandonada, por esta:
#       ao encontrar divisor diferente de 1 (o caso do 2 foi resolvido 1º), deu instrução 'break' ao while e verificou se divisor == num,
#       para determinar que é primo em caso afirmativo (retorno True) ou que não primo em caso negativo (retorno False).
