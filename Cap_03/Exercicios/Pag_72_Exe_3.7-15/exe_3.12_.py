# Data: 03/09/2024

# ============ EXERCÍCIO 3.12 ====================

# Escreva um programa que calcule o tempo de uma viagem de carro. 
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

print()
print(f'========== Tempo de Viagem ==========')
print()
distancia = float(input('Digite a distância a ser percorrida (Km): '))
vel_media = float(input('Digite a velocidade média esperada para a viagem (Km/h): '))
tempo = distancia / vel_media
tempo_hora = tempo//1 # ou int(tempo) ou int (tempo/1)
# tempo_min = (tempo - tempo_hora) * 60
tempo_min = ((tempo % 1) * 3600) // 60
tempo_seg = ((tempo % 1) * 3600) % 60
print()
print('O tempo de viagem percorrendo uma distância total de %.2f Km a uma velocidade de %.2f Km/h é:' % (distancia, vel_media))
print(f'{tempo_hora:02.0f} h {tempo_min:02.0f} min')
print(f'{tempo_hora:02.0f} h {tempo_min:02.0f} min {tempo_seg:02.0f} s')
print()
# ========== FIM ==========================================================================

print("Alternativa:\n")
tempo_s = int(tempo * 3600)  # convertemos de horas para segundos
horas = int(tempo_s / 3600)  # parte inteira

tempo_s_restante = int(tempo_s % 3600)  # o resto

minutos = int(tempo_s_restante / 60)
segundos = int(tempo_s_restante % 60)
print("%05d:%02d:%02d" % (horas, minutos, segundos))