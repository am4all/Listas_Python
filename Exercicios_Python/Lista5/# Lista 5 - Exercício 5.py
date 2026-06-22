# Lista 5 Exercício 5
# Escreva um algoritmo que leia o valor de uma compra feita pelo usuário, calcule e mostre o valor total da compra aplicando um desconto de 10%.  

# ENTRADA
valor_compra = float(input("Digite o valor da compra: "))

# PROCESSAMENTO
valor_final = valor_compra - (valor_compra * 0.10) 

# SAÍDA
print("O valor com desconto de 10% é:", valor_final)