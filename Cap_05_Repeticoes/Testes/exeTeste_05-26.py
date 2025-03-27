# Data: 27/03/2025

# ============ EXERCÍCIO 5.26 (PÁG. 94) ============


''' Escreva um programa que calcule o resto da divisão inteira entre dois números. Utilize apenas as
operações de soma e subtração para calcular o resultado. '''

# ALTERNATIVA PARA QUE ACEITE NÚMEROS NEGATIVOS: (gambiarra)

print(f'\n{'=' * 5} resto da divisão inteira {'=' * 5}\n')
numerador = int(input('Digite o 1º número (numerador): '))
denominador = int(input('Digite o 2º número (denominador): '))

if denominador == 0:
    print(
        f'\nNão é possível dividir pelo denominador {denominador}, tente outro número no denominador!\n')
resto = numerador
quociente = 0  # contador
# para divisão inteira de dois números positivos ou o (1º positivo e o 2º negativo), exemplo: [5 > 2 = True] ou [5 > -2 = True]
if numerador > denominador:
    # resto = numerador
    # quociente = 0
    if (numerador >= 0 and denominador > 0):
        # caso em que numerador e denominador são exclusivamente positivos
        while denominador <= resto:
            # resto positivo ---- resto = [resto (+)] - [denominador (+)]
            resto -= denominador
            quociente += 1          # (+) / (+) = (+) => quociente positivo
########################################################################################
    elif (numerador >= 0 and denominador < 0):                                          #
        # caso em que numerador e denominador são, respectivamente, (+) (-)             #
        # |denominador| (módulo)
        denominador = abs(denominador)
        while denominador <= resto:                                                     #
            # resto positivo --- resto = [resto (+)] - [denominador (-)]                #
            resto = resto - denominador
            # (+) / (-) = (-) => quociente negativo                                     #
            quociente -= 1
########################################################################################
    print(f'{'=' * 36}\n'
          f'{numerador} / {denominador} = {quociente}\n'
          f'resto da divisão é: {resto}'
          '\n')
# para divisão inteira de dois números negativos ou o (1º negativo e o 2º positivo), exemplo: [-5 < -2 = True] ou [-5 < 2 = True]
elif numerador < denominador:
    # resto = numerador
    # quociente = 0
    if (numerador < 0 and denominador < 0):
        # caso em que numerador e denominador são exclusivamente negativos
        while resto <= denominador:
            # resto negativo ---- resto = [resto (-)] - [denominador (-)]
            resto -= denominador
            quociente += 1          # (-) / (-) = (+) => quociente positivo
########################################################################################
    elif (numerador < 0 and denominador > 0):                                           #
        # caso em que numerador e denominador são, respectivamente, (-) (+)             #
        resto = abs(resto)                              # |resto| (módulo)
        while resto >= denominador:
            #
            # resto negativo ---- resto = [resto (-)] + [denominador (+)]               #
            #
            resto = denominador - resto
            if resto < 0:
                resto = abs(resto)
            # (-) / (+) = (-) => quociente negativo                                     #
            quociente -= 1
        resto = 0 - resto
########################################################################################
    print(f'{'=' * 36}\n'
          f'Divisão inteira {numerador} // {denominador} = {quociente}\n'
          f'Resto da divisão inteira é: {resto}'
          '\n')
