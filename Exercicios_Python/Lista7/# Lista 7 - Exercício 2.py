# Lista 7 - Exercício 2
# Crie um algoritmo que peça a idade de uma pessoa. Se a idade for maior ou igual a 18 anos, mostre a mensagem "Acesso permitido".

# ENTRADA
idade = int(input("Digite a sua idade: "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if idade >= 18:
    print("Acesso permitido")
    
if idade < 18:
    print("Acesso não permitido")