# Lista 5 - Exercício 7
# Para o protótipo do aplicativo PetCare, precisamos calcular a alimentação de um cão. Escreva um algoritmo que leia o peso de um cachorro (em kg) e calcule a quantidade diária de ração recomendada, sabendo que a recomendação média é de 15 gramas de ração para cada quilo do animal. Mostre o resultado em gramas.
# ENTRADA
peso_cachorro = float(input("Digite o peso do cachorro (kg): "))

# PROCESSAMENTO
qtd_racao = peso_cachorro * 15 

# SAÍDA
print("A quantidade diária de ração é (gramas):", qtd_racao)