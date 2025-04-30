# Data: 24/04/2025

# ============ EXERCÍCIO 6.03 (PÁG. 105) ============

# Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.

lista1 = []
lista2 = []
while True:
    n1 = int(input("Digite um número inteiro para a 1ª lista (0 para interromper): "))
    if n1 == 0:
        print()
        break
    lista1.append(n1)
while True:
    n2 = int(input("Digite um numero inteiro para a 2ª lista (0 para interromper): "))
    if n2 == 0:
        print()
        break
    lista2 += [n2]
######################
lista3 = []
juncao_l1_l2 = lista1
juncao_l1_l2.extend(lista2)

contador1 = 0
while contador1 < len(juncao_l1_l2): # para percorrer a lista formada por lista1 e lista 2 que pode conter elementos repetidos
    contador2 = 0
    while contador2 < len(lista3):  # para percorrer a lista 3 oriunda da junção de lista 1 com lista 2, sem elementos repetidos, a medida que ela se forma e seu tamanho cresce
        if juncao_l1_l2[contador1] == lista3[contador2]:
            break   # se houver elementos repetidos, esse bloco while é interrompido e vai só incrementar no contador 1
        contador2 = contador2 + 1
    if contador2 == len(lista3):    # lista estava vazia no 1º caso ou não havia número repetido na verificação do 2º while
        lista3.append(juncao_l1_l2[contador1])
    contador1 += 1
# impressão de cada elemento da lista 3 em seu respectivo índice:
print('Lista 3:\n')
idx = 0
while idx < len(lista3):
    print(f"Índice {idx}: {lista3[idx]}")
    idx += 1
print(lista3)