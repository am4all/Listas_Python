# Lista 7 - Exercício 5
# Faça um algoritmo que leia a quantidade de produtos no estoque. 
# Se a quantidade for menor que 10 unidades, exiba a mensagem "Atenção: Necessário repor estoque".

# ENTRADA
quantidade_estoque = int(input("Digite a quantidade de produtos no estoque: "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if quantidade_estoque < 10:
    print("Atenção: Necessário repor estoque")
if quantidade_estoque > 10:
    print(" Não é Necessário repor estoque")