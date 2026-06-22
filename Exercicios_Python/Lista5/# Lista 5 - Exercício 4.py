# Lista 5 Exercíco 4
# Escreva um algoritmo que leia 3 itens de supermercado, nome, quantidade e valor unitário. Calcule o valor total de cada item, o valor total da compra. Por fim mostre na tela, os itens comprados com a quantidade, valor unitário e valor total de cada item e o valor total da compra.
# ENTRADA
print("Item 1")
nome1 = input("Digite o nome: ")
qtd1 = int(input("Digite a quantidade: "))
valor_unit1 = float(input("Digite o valor unitário: "))

print("\nItem 2")
nome2 = input("Digite o nome: ")
qtd2 = int(input("Digite a quantidade: "))
valor_unit2 = float(input("Digite o valor unitário: "))

print("\nItem 3")
nome3 = input("Digite o nome: ")
qtd3 = int(input("Digite a quantidade: "))
valor_unit3 = float(input("Digite o valor unitário: "))

# PROCESSAMENTO
total1 = qtd1 * valor_unit1 
total2 = qtd2 * valor_unit2 
total3 = qtd3 * valor_unit3 
total_compra = total1 + total2 + total3 

# SAÍDA
print("\nResumo da Compra:")
print(f"{nome1} | Quantidade: {qtd1} | Valor Unitário: {valor_unit1} | Total do item: {total1}")
print(f"{nome2} | Quantidade: {qtd2} | Valor Unitário: {valor_unit2} | Total do item: {total2}")
print(f"{nome3} | Quantidade: {qtd3} | Valor Unitário: {valor_unit3} | Total do item: {total3}")
print("Valor total da compra:", total_compra)
