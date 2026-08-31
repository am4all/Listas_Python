# Exercício 3 - 3 - Às vezes você escreve aquela bio perfeita ou um tweet gigante e precisa saber se vai caber. 
# Faça um programa que peça para o usuário digitar uma frase e mostre na tela exatamente quantos caracteres
# (letras, espaços e pontuações) essa frase tem.

# ENTRADA
frase = input("Digite a sua bio ou tweet: ")

# PROCESSAMENTO
# A função len() retorna o número de caracteres em uma string.
tamanho = len(frase)

# SAÍDA
print(f"A sua frase possui {tamanho} caracteres no total.")