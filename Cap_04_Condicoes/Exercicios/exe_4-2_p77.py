# Data: 06/09/2024

# ============ EXERCÍCIO 4.2 (PÁG 77) ============

# Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, 
# exiba uma mensagem dizendo que o usuário foi multado. 
# Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

print()
vel = float(input("Qual a velocidade do carro (km/h): "))
if vel > 80:
    print("\nVocê foi multado!\n")
    multa = (vel - 80) * 5
    print(f'Deve pagar R${multa:.2f}\n')
if vel <= 80:
    print("\nVocê está detro da velocidade permitida\n")