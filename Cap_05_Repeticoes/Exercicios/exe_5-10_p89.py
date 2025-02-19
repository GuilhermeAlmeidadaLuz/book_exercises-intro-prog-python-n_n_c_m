# Data: 18/02/2025

# ============ EXERCÍCIO 5.10 (PÁG. 89) ============

# Correção de Teste de Múltipla Escolha

# pontos = 0
# questao = 1
# while questao <= 3:
#     resposta = input(f"Resposta da questão {questao}: ")
#     if questao == 1 and resposta == "b":
#         pontos = pontos + 1
#     if questao == 2 and resposta == "a":
#         pontos = pontos + 1
#     if questao == 3 and resposta == "d":
#         pontos = pontos + 1
#     questao = questao + 1
# print(f"O aluno fez {pontos} ponto(s)")


'''(Exercício 5.10) Modifique o programa anterior para que aceite respostas com letras maiúsculas e minúsculas em todas as 
questões.'''

pontos = 0
questao = 1
while questao <= 3:
    resposta = input(f"Resposta da questão {questao}: ")
    if questao == 1 and (resposta == "B" or resposta == "b"):
        pontos = pontos + 1
    if questao == 2 and (resposta == "A" or resposta == "a"):
        pontos = pontos + 1
    if questao == 3 and (resposta == "D" or resposta == "d"):
        pontos = pontos + 1
    questao = questao + 1
print(f"O aluno fez {pontos} ponto(s)")
