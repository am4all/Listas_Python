# Lista 6 - Exercício 1
# Desenvolva um algoritmo que solicite ao usuário dois números inteiros e realize a soma. O resultado só deve ser exibido se for maior que 10. Caso contrário, não mostra nada.

# ENTRADA
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

# PROCESSAMENTO
soma = num1 + num2

# SAÍDA
if soma > 10:
    print("A soma dos valores é:", soma)