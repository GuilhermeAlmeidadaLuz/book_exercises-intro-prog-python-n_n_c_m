# Data: 03/09/2024

# ============ EXERCÍCIO 3.14 ===============

# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
# assim como a quantidade de dias pelos quais o carro foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por km rodado.

print()
print('='*10 + ' Cálculo de Preço de Locação de Carro ' + '='*10)
km_rodados = float(input("\nDigite a distância percorrida em 'Km': "))
dias_alugado = int(input("Dias de locação do carro: "))
custo_p_dia = 60
custo_p_km = 0.15
pagamento = ( custo_p_dia * dias_alugado) + (custo_p_km * km_rodados)
print('\nPreço a pagar: R$ %.2f' % pagamento)
print()