# Exercício 4 - Sabe quando alguém tem mania de falar a mesma palavra toda hora, tipo "literalmente", "tipo" ou "mano"?
# Vamos criar um rastreador para isso!
# Faça um programa que leia uma frase inteira e depois pergunte qual palavra você quer investigar. 
# O programa deve contar e mostrar na tela quantas vezes essa palavra específica apareceu no meio da frase.

# ENTRADA
frase = input("Digite a frase completa: ")
giria = input("Qual gíria ou palavra você quer rastrear? ")

# PROCESSAMENTO
# O método count() retorna o número de vezes que um valor aparece em uma string.
quantidade = frase.count(giria)

# SAÍDA
if quantidade > 0:
    print(f"A palavra '{giria}' apareceu {quantidade} vezes na frase.")
else:
    print(f"A palavra '{giria}' não foi encontrada na frase.")