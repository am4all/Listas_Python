# Lista 9 - Exercício 9
# Faça um algoritmo que leia a temperatura atual da sua cidade em graus Celsius. Se a temperatura for menor que 20 graus, exiba "Está frio, leve um casaco!". Caso contrário, exiba "O clima está agradável, não precisa de casaco".

# ENTRADA
temperatura = float(input("Digite a temperatura atual (em °C): "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if temperatura < 20:
    print("Está frio, leve um casaco!")
else:
    print("O clima está agradável, não precisa de casaco")