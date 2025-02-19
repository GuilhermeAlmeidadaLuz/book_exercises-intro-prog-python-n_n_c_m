# Data: 04/10/2024

# ============ EXERCÍCIO 4.3 (PÁG 79) ============

# Escreva um programa que leia três números e que imprima o maior e o menor

print()
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))
maior = num1
menor = num1
# abordagem usando somente if's e sem aninhá-los
if num1 > num2:
    maior = num1
    menor = num2
if num1 < num2:
    maior = num2
    menor = num1
if maior < num3:  # atualiza o maior
    maior = num3
if menor > num3:  # atualiza o menor
    menor = num3
print(f"\nO maior é: {maior}")
print(f"\nO menor é: {menor}\n")
