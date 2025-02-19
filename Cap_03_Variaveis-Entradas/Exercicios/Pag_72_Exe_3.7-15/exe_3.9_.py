# Data: 30/08/2024

# ============== Exercício 3.9 =============

# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
# Calcule o total em segundos

def total_seconds(dias, horas, minutos, segundos):
    hours_24 = 24
    minutes_60 = 60
    seconds_60 = 60

    days_at_sec = dias * hours_24 * minutes_60 * seconds_60
    hours_at_sec = horas * minutes_60 * seconds_60
    minutes_at_sec = minutos * seconds_60

    qtd_sec = days_at_sec + hours_at_sec + minutes_at_sec + segundos
    return qtd_sec

if __name__=="__main__":
    print()
    print('==== Conversor para segundos ===========')
    dias = int(input("Digite quantos dias: "))
    horas = int(input('Digite quantas horas: '))
    minutos = int(input('Digite quantos minutos: '))
    segundos = int(input('Digite quantos segundos: '))
    print()
    print(f'O total em segundos é {total_seconds(dias, horas, minutos, segundos)}s')
    print()