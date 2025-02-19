# Data: 06/02/2025

# ============ EXERCÍCIO 5.8 (PÁG. 88) ============

'''Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo 
segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que 
podemos entender a multiplicação de dois números como somas sucessivas de um deles. Assim, 4 × 5 = 5 
+ 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.'''

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
cont = 0
result = 0

if num1 >= num2:
    inicio = num2
    fim = num1
else:
    inicio = num1
    fim = num2

while cont < fim:
    result = result + inicio
    cont += 1

print(f"{num1: <2} x {num2: >2} = {result: >2}\n"
      "\n(Obtido a partir de sucessivas somas)")
