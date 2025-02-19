# Data: 10/02/2025

# ============ EXERCÍCIO 5.9 (PÁG. 88) ============

'''Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim 
como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. 
Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes 
que podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco 
vezes de 20.'''

num1 = int(input('\nDigite o primeito número: '))
num2 = int(input('Digite o segundo número: '))
resto = 0           # resto será armazenado
quociente = 0       # quociente da divisão será como um contador
decremento = num1

while decremento > num2:
    decremento -= num2      # subtrações sucessivas de num1 - num2 armazenadas em decremento
    quociente += 1          # contagem do quociente
    if decremento < num2:
        resto = decremento
print()
print(f'[Resultado da divisão inteira]\n'
      f'\n{num1} // {num2} = {quociente} (Quociente)\n'
      f'Resto = {resto}\n')