# Data: 22/10/2024

# ============ EXERCÍCIO 4.6 (PÁG 80) ============

# Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km. Calcule o 
# preço da passagem, cobrando R$ 0,50 por km para viagens de até de 200 km, e R$ 0,45 para viagens mais 
# longas.

dist_percorrer = float(input("\nQual distância você deseja percorrer (km): "))
if dist_percorrer <= 200:
    tx_por_km = 0.5
    preço_pass = dist_percorrer * tx_por_km
else:
    tx_por_km = 0.45
    preço_pass = dist_percorrer * tx_por_km
print(f"O preço de sua passagem R$ {preço_pass:7.2f}")