# Data: 27/03/2025

# ============ EXERCÍCIO 5.26 (PÁG. 94) ============


''' Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as 
operações de soma e subtração para calcular o resultado. '''

print(f'\n{'=' * 5} resto da divisão inteira {'=' * 5}\n')
numerador = int(input('Digite o 1º número (numerador): '))
denominador = int(input('Digite o 2º número (denominador): '))

if denominador == 0:
    print(
        f'\nNão é possível dividir pelo denominador {denominador}, tente outro número no denominador!\n')
if (numerador >= 0) and (denominador > 0) and (numerador > denominador):     # para divisão inteira
    resto = numerador
    quociente = 0
    while denominador <= resto:         # alternativa: resto >= denominador
        # caso em que numerador e denominador são exclusivamente positivos
        # lembrando que resto recebeu o valor do numerador, o número maior
        resto = resto - denominador
        # resto positivo <= (+) (+) = (+)
        quociente += 1
    print(f'{'=' * 36}\n'
          f'Resultado da divisão inteira de {numerador} // {denominador} = {quociente}\n'
          f'Resto da divisão inteira é: {resto}'
          '\n')
