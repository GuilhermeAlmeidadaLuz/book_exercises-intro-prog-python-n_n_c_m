# Data: 27/03/2025

# ============ EXERCÍCIO 5.27 (PÁG. 94) ============

''' Escreva um programa que verifique se um número é palíndromo. Um número é palíndromo se continua o 
mesmo caso seus dígitos sejam invertidos. Exemplos: 454, 10501 '''

print(f'\n{'=' * 10} Verificador de Número Palíndromo {'=' * 10}')
num = int(input("Digite um número: "))
print()
num_string = str(num)
num_str_reversed = ''
count = len(num_string)
while count > 0:
    num_str_reversed = num_str_reversed + num_string[count - 1]
    count -= 1
if num_str_reversed == num_string:
    print(f'É palíndromo!\n'
          f'{'=' * 54}'
          '\n'
          f'{num_string} \t - número'
          '\n'
          f'{num_str_reversed} \t - número invertido'
          '\n')
else:
    print(f'Não é palíndromo!\n'
          f'{'=' * 54}'
          '\n'
          f'{num_string} \t - número'
          '\n'
          f'{num_str_reversed} \t - número invertido'
          '\n')
