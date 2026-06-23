# Lista 10 - Exercicio 6
# 6. Ano Bissexto. Crie um algoritmo que peça para o usuário digitar um ano (ex: 2024). O programa deve verificar se o ano é bissexto ou não. Regra: Um ano é bissexto se for divisível por 4, mas não por 100. A exceção a essa regra são os anos divisíveis por 400, que também são bissextos.

# Solicita o ano
ano = int(input("Digite um ano (ex: 2024): "))

# Regra: Divisível por 4 E não por 100, OU divisível por 400
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")