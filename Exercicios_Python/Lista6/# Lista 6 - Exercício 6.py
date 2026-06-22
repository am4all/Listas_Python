# Lista 6 - Exercício 6
# Desenvolva um algoritmo que leia um número de 3 algarismos. O programa isola o algarismo da casa das centenas. Identifica e imprime se esse algarismo é par ou ímpar. (Nota: A divisão inteira // 100 ajuda a isolar a centena).

# ENTRADA
numero = int(input("Digite um número de 3 algarismos (ex: 456): "))

# PROCESSAMENTO
centena = numero // 100  # Pega apenas o primeiro dígito
resto = centena % 2      # Verifica se a centena é par ou ímpar

# SAÍDA
print("O algarismo da centena é:", centena)

if resto == 0:
    print("Esse algarismo é PAR.")

if resto != 0:
    print("Esse algarismo é ÍMPAR.")