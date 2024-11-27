# Data: 04/10/2024

# ============ EXERCÍCIO 4.5 (PÁG 80) ============

# Execute o Programa 4.4 e experimente alguns valores. Verifique se os resultados foram os mesmos do 
# Programa 4.2.

# Programa 4.4 - Carro novo ou velho, dependendo da idade com else
idade = int(input("Digite a idade de seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
else:
    print("Seu carro é velho")

# Programa 4.2 - Carro novo ou velho, dependendo da idade
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
if idade > 3:
    print("Seu carro é velho")