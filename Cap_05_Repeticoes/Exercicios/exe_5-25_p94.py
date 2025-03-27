# Data: 27/03/2025

# ============ EXERCÍCIO 5.25 (PÁG. 94) ============

''' Escreva um programa que calcule a raiz quadrada de um número. Utilize o método de Newton para obter 
um resultado aproximado. Sendo n o número a obter a raiz quadrada, considere a base b=2. Calcule p 
usando a fórmula p=(b+(n/b))/2. Agora, calcule o quadrado de p. A cada passo, faça b=p e recalcule p 
usando a fórmula apresentada. Pare quando a diferença absoluta entre n e o quadrado de p for menor que 
0,0001. '''

n = int(input(f"\n{'=' * 10} Raiz Quadrada {'=' * 10}\n"
"Digite um número natural para obter sua raiz quadrada: ")) # 'n é o radicando' dentro do radical de índice 2
if n < 0:
    print('Digite um número positivo!')
else:
    b = 2                       # b - base
    while True:
        p = (b + (n / b) ) / 2   # p - raiz
        quadrado_de_p = p ** 2  # p ao quadrado - raiz ao quadrado, que deve ser p ^ 2 = n 
        if abs(n - quadrado_de_p) < 0.0001:     # valor absoluto da subtração, ou seja, em módulo => | valor | < 0.0001
            break
        b = p
    print(f'\nA raiz quadrada de {n} é aproximadamente: {p:8.4f}\n')
