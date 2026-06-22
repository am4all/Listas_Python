# Lista 9 - Exercício 8
# Crie um programa que leia o saldo de uma conta e pergunte o valor que o usuário deseja sacar. Se o valor do saque for menor ou igual ao saldo, subtraia o valor e mostre "Saque realizado com sucesso. Novo saldo: [valor]". Caso contrário, mostre "Operação cancelada: Saldo insuficiente".

# ENTRADA
saldo = float(input("Digite o saldo atual da conta: R$ "))
valor_saque = float(input("Digite o valor que deseja sacar: R$ "))

# PROCESSAMENTO
# O processamento do novo saldo ocorrerá dentro do bloco condicional, 
# pois só deve ser calculado se houver saldo suficiente.

# SAÍDA
if valor_saque <= saldo:
    novo_saldo = saldo - valor_saque
    print(f"Saque realizado com sucesso. Novo saldo: R$ {novo_saldo:.2f}")
else:
    print("Operação cancelada: Saldo insuficiente")