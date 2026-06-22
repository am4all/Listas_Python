# Lista 5 - Exercício 3
#Faça um algoritmo que leia 3 notas e calcule a média ponderada das notas. Sendo que as notas têm pesos 2, 3 e 5 respectivamente.

# ENTRADA
nota1 = float(input("Digite a nota 1 (peso 2): "))
nota2 = float(input("Digite a nota 2 (peso 3): "))
nota3 = float(input("Digite a nota 3 (peso 5): "))

# PROCESSAMENTO
media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 5)) / 10 # [cite: 49]

# SAÍDA
print("A média ponderada do aluno é:", media)