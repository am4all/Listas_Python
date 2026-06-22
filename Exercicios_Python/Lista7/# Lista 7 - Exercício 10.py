# Lista 7 - Exercício 10
# Faça um algoritmo que leia o saldo de uma conta bancária e o valor de um saque desejado. Se o valor do saque for maior que o saldo disponível, mostre a mensagem: "Saldo insuficiente para realizar a operação."

# ENTRADA
saldo = float(input("Digite o saldo da conta bancária: R$ "))
valor_saque = float(input("Digite o valor do saque desejado: R$ "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if valor_saque > saldo:
    print("Saldo insuficiente para realizar a operação.")