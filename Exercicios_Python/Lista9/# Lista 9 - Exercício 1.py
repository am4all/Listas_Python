# Lista 9 - Exercício 1
# Crie um algoritmo que leia um número inteiro digitado pelo usuário. Se o número for divisível por 2 (resto da divisão igual a zero), exiba a mensagem "O número é par". Caso contrário, exiba "O número é ímpar".

# ENTRADA
numero = int(input("Digite um número inteiro: "))

# PROCESSAMENTO
resto = numero % 2

# SAÍDA
if resto == 0:
    print("O número é par")
else:
    print("O número é ímpar")