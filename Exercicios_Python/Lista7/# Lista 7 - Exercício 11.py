# Lista 7 - Exercício 11
# Faça um algoritmo que leia o ano de nascimento de uma pessoa e o ano atual. Calcule a idade e, se ela for maior ou igual a 16 anos, mostre a mensagem: "Você já possui idade para votar."

# ENTRADA
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# PROCESSAMENTO
idade = ano_atual - ano_nascimento

# SAÍDA
if idade >= 16:
    print("Você já possui idade para votar.")