# Lista 9 - Exercício 7
# Desenvolva um algoritmo que pergunte o salário de um cliente e o valor da parcela mensal de um financiamento desejado. Se o valor da parcela for menor ou igual a 30% do salário, exiba "Financiamento aprovado". Caso contrário, exiba "Financiamento reprovado por comprometer a renda".

# ENTRADA
salario = float(input("Digite o salário do cliente: R$ "))
valor_parcela = float(input("Digite o valor da parcela desejada: R$ "))

# PROCESSAMENTO
limite_parcela = salario * 0.30

# SAÍDA
if valor_parcela <= limite_parcela:
    print("Financiamento aprovado")
else:
    print("Financiamento reprovado por comprometer a renda")