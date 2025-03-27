# Data: 26/03/2025

# ============ EXERCÍCIO 5.23 (PÁG. 94) ============

''' Escreva um programa que leia um número e verifique se é ou não um número primo. Para fazer essa 
verificação, calcule o resto da divisão do número por 2 e depois por todos os números ímpares até o 
número lido. Se o resto de uma dessas divisões for igual a zero, o número não é primo. Observe que 0 e 1 
não são primos e que 2 é o único número primo que é par. '''

num = int(input("Digite um número natural (positivo): "))

if num == 0 or num == 1:
    print(f'{num} não é primo! Pois é caso especial')
elif num == 2:
    print(f'{num} é primo!')
elif num % 2 == 0:
    print(f'{num} não é primo! Pois é divisível por 2')
else:
    divisor = 1
    contagem_divisores = 0
    while divisor <= num:
        if num % divisor == 0:
            contagem_divisores += 1
        divisor += 2
    if contagem_divisores == 2:
        # um número primo sempre terá dois divisores, o 1 e ele mesmo
        print(
            f'{num} é primo! Pois tem como divisores o \'1\' e o \'{num}\' (ele mesmo)')
    else:
        print(f'{num} não é primo!')

# Obs.: abordagem com mais custo computacional dentro do 'while', poderia verificar como Nilo, que ao encontrar divisor diferente de 1,
#       deu instrução 'break' ao while e verificou se divisor == num,
#       para determinar que é primo em caso afirmativo (retorno True) ou que não primo em caso negativo (retorno False).
