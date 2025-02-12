# Data: 23/10/2024

# ============ EXERCÍCIO 4.8 (PÁG 83) ============

# Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/).
# Exiba o resultado da operação solicitada.

num1 = float(input('\nDigite o primero número: '))
num2 = float(input('\nDigite o segundo número: '))
operação = str(input('\nQual operação você deseja realizar?'
                     '\nsoma (+)'
                     '\nsubtração (-)'
                     '\nmultiplicação (x)'
                     '\ndivisão (/)'
                     '\n----------------\n'
                     'operação: '))
if operação == 'soma' or operação == '+':
    print(f'\n{num1} + {num2} = {num1 + num2}')
elif operação == 'subtração' or operação == '-':
    print(f'\n{num1} - {num2} = {num1 - num2}')
elif operação == 'multiplicação' or operação == 'x':
    print(f'\n{num1} x {num2} = {num1 * num2}')
elif operação == 'divisão' or operação == '/':
    print(f'\n{num1} / {num2} = {num1 / num2}')
else:
    print('Operação inválida! Tente novamente.')
print()