# Lista 8 - Exercício 1
# Um cinema tem uma regra simples para um filme específico: apenas pessoas com 16 anos ou mais podem entrar. Desenvolva um algoritmo que leia a idade de uma pessoa. Se a idade for 16 ou maior, exiba a mensagem: "Entrada permitida." Se a pessoa não tiver 16 anos, o programa deve exibir a mensagem: "Entrada NÃO permitida”.

# ENTRADA
idade = int(input("Digite a idade da pessoa: "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if idade >= 16:
    print("Entrada permitida.")
    
if idade < 16:
    print("Entrada NÃO permitida.")