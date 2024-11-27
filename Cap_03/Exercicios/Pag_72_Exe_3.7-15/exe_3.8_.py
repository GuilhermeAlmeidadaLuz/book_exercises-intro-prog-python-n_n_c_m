# Data: 30/08/2024

# ============== Exercício 3.8 =============

# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros

# 1 cm == 10 mm ----------- 1 mm = 0,1 cm = 0,01 m

def Convert_m_in_mm(meters):
    milimeters = meters * 100
    return milimeters


if __name__ == "__main__":
    print()
    print("======== Conversor de metros para milimetros ========")
    print()
    val = float(input('Digite uma medida em metros: '))
    print(f'O valor digitado "{val}m" corresponde a "{Convert_m_in_mm(val)}mm"')
    print()