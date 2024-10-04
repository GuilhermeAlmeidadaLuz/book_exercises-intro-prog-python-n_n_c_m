# Exercício 2.6 - Modifique o Programa 2.2, de forma que ele calcule um aumento de 15%
# para um salário de R$ 750.

salário = 750 # salário de R$ 750,00
aumento = 5/100 # 5% = 5/100
novo_salário = salário + (salário * aumento) # salário + (salário x 5%)
print('\nInício do Programa\n')
print(f"O salário inicial de R$ {salário} com aumento de {aumento*100} % é: R$ {novo_salário}")
print()