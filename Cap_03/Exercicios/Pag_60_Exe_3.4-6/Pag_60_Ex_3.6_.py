# Guilherme Almeida da Luz

# Exercício 3.6 - Escreva uma expressão que será utilizada para decidir se um aluno foi
# ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores que 7.
# Considere que o aluno cursa apenas três matérias, e que a nota de cada uma está armazenada
# nas seguintes variáveis: matéria1, matéria2 e matéria3.

print()
matéria1 = float(input("Nota da Matéria 1: "))
matéria2 = float(input("Nota da Matéria 2: "))
matéria3 = float(input("Nota da Matéria 3: "))

aprovado = matéria1 > 7 and matéria2 > 7 and matéria3 > 7
print("Aprovado? --> ", aprovado)
print()