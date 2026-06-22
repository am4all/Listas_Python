# Lista 5 - Exercício 8
# Uma peça produzida por uma impressa em 3D tem seu custo calculado pelo peso do filamento gasto. Escreva um algoritmo que leia o peso da peça (em gramas) e o valor do quilo do filamento. Calcule e mostre o custo apenas do material utilizado na peça.
# RESUMO: Leia o peso da peça (em gramas) e o valor do quilo do filamento para calcular o custo apenas do material utilizado.

# ENTRADA
peso_gramas = float(input("Digite o peso da peça em gramas: "))
valor_quilo = float(input("Digite o valor do quilo do filamento: "))

# PROCESSAMENTO
custo_peca = (peso_gramas / 1000) * valor_quilo

# SAÍDA
print("O custo de material da peça 3D é:", custo_peca)