# Data: 23/04/2025

# ============ EXERCÍCIO 6.02 (PÁG. 105) ============

# Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.

lista1 = list()
lista2 = []

while True:
    n1 = int(input("Digite um número inteiro para a lista 1 (0 sai): "))
    if n1 == 0:
        print()
        break
    else:
        lista1.append(n1)
while True:
    n2 = int(input("Digite número inteiro para a lista 2 (0 sai): "))
    if n2 == 0:
        print()
        break
    else:
        lista2 += [n2]
# junção das listas em uma 3ª lista:
##
# alternativa 1:
lista3 = []
lista3.extend(lista1 + lista2)
##
# altenativa 2:
# lista3 = lista1 + lista2
##
print(f'Lista 1 - {lista1} + Lista 2 - {lista2} = Lista 3 - {lista3}')
