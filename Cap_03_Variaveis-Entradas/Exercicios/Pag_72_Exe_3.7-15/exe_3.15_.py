# Data: 03/09/2024

# ============ EXERCÍCIO 3.15 ====================

# Escreva um programa para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá.
# Exiba o total em dias.

print()
print('='*10 + ' Cálculo da Redução de Tempo de Vida de Um Fumante ' + '='*10)
print()
qtd_cigarros_dia = int(input("Quantos cigarros fumados por dia: "))
anos_fumando = int(input("Quantos anos fumando: ")) 
min_perd_por_cig = 10 # minutos

min_perd_dia = qtd_cigarros_dia * min_perd_por_cig # minutos perdidos em um dia

_1ano_em_dias = 365

min_perd_ano = _1ano_em_dias * min_perd_dia # minutos perdidos em um ano

total_min_perd = anos_fumando * min_perd_ano # total de minutos perdidos pela quantidade de anos fumando

# 1 dia = 24h x 60min = 1440min 
total_dias_perd_vida = total_min_perd // 1440

print('Dias de vida perdidos pelo fumante: %d' % total_dias_perd_vida)
print()

# ----------------------------------------------
# --------------------------------------

cigarros_por_dia = int(input("Quantidade de cigarros por dia:"))
anos_fumando = float(input("Quantidade de anos fumando:"))
redução_em_minutos = anos_fumando * 365 * cigarros_por_dia * 10
# Um dia tem 24 x 60 minutos
redução_em_dias = redução_em_minutos / (24 * 60)
print("Redução do tempo de vida %8.2f dias." % redução_em_dias)