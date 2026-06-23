# Lista 10 - Exercicio 1

#1. Classificação Eleitoral. Faça um programa que leia a idade de uma pessoa e informe a sua classe eleitoral:
#Menor que 16 anos: Não pode votar.
#Entre 16 e 17 anos ou maior que 70 anos: Voto facultativo.
#Entre 18 e 70 anos: Voto obrigatório.

idade = int(input("Digite a sua idade: "))

# Estrutura de decisão para verificar a classe eleitoral
if idade < 16:
    print("Não pode votar.")
elif (idade >= 16 and idade <= 17) or idade > 70:
    print("Voto facultativo.")
else:
    print("Voto obrigatório.")