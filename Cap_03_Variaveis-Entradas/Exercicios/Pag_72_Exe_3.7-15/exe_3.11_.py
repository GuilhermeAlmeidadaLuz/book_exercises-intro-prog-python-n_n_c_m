# Data: 03/09/2024

# ============ EXERCÍCIO 3.11 ====================

# Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
# Exiba o valor do desconto e o preço a pagar.

print()
print('========= Cálculo de Desconto de Mercadoria ===========\n')
preco_mercadoria = float(input('Digite o preço do produto: '))
percent_desc = float(input('Digite o percentual de desconto: '))
print()
val_desc = preco_mercadoria * (percent_desc/100)
novo_pco_merc = preco_mercadoria - val_desc
print('{:.0f}% de {:.2f} é igual a: {:.2f}'.format(percent_desc, preco_mercadoria, val_desc))
print(f'Preço final do produto com desconto de {percent_desc:.0f}%: {novo_pco_merc:.2f}')
print()
