# Lista 7 - Exercício 3
# Faça um algoritmo que leia o valor de uma compra. Se o valor for superior a R$ 200,00, aplique um desconto de R$ 20,00 no total e mostre o novo valor.

# ENTRADA
valor_compra = float(input("Digite o valor total da compra: R$ "))

# PROCESSAMENTO
valor_com_desconto = valor_compra - 20.00

# SAÍDA
if valor_compra > 200.00:
    print(f"Desconto aplicado! O novo valor da compra é: R$ {valor_com_desconto:.2f}")
    
if valor_compra < 200.00:
    print(f"Desconto não aplicado.")