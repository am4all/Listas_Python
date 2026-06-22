#Lista 5 -  Exercício 2
#Faça um algoritmo que leia o valor de uma compra e o desconto a ser aplicado, calculando o total.  
# compra 200 aplica 10% ... vai pagar 180
# ENTRADA
valorcompra = float(input("Digite o valor da compra: "))
desconto = float(input("Digite a porcentagem de desconto: "))

# PROCESSAMENTO
valortotal = valorcompra * (1 - (desconto / 100))
#valortotal = valorcompra - (valorcompra * 0.10) 
#valortotal = valorcompra *0.10

# SAÍDA
print("O valor total com desconto é:", valortotal)