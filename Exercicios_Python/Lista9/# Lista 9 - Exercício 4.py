# Lista 9 - Exercício 5
# Escreva um algoritmo que leia o valor total de uma compra no e-commerce. Se o valor for maior ou igual a R$ 250,00, exiba "Parabéns! Você ganhou Frete Grátis". Caso contrário, exiba "O valor do frete fixo é de R$ 25,00".

# ENTRADA
valor_compra = float(input("Digite o valor total da compra: R$ "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if valor_compra >= 250.00:
    print("Parabéns! Você ganhou Frete Grátis")
else:
    print("O valor do frete fixo é de R$ 25,00")