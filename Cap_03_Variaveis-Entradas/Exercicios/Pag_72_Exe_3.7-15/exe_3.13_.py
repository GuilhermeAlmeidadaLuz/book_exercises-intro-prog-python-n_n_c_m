# Data: 03/09/2024

# ============ EXERCÍCIO 3.13 ====================

# Escreva um programa que converta uma temperatura digitada em °C em °F. A fórmula para essa conversão é:
#       9 x C
# F =  ------- + 32
#         5

print()
print("="*8 + " CONVERSOR DE TEMPERATURA EM CELSIUS PARA FAHRENHEIT " + "="*8)
print()
g_celsius = float(input("Digite a temperatura em Celsius: "))
g_fahrenheit = (9 * g_celsius / 5) + 32
print(f"\nCorresponde a {g_fahrenheit}ºF")
print()
