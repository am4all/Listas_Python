# Lista 6 - Exercício 3
# O algoritmo recebe um número único. Se o número for positivo, calcula e imprime o seu triplo. Se for negativo, calcula e imprime o seu quadrado.  

# ENTRADA
numero = float(input("Digite um número: "))

# PROCESSAMENTO E SAÍDA
if numero > 0:
    resultado = numero * 3
    print("O número é positivo. O triplo é:", resultado)

if numero < 0:
    resultado = numero ** 2
    print("O número é negativo. O quadrado é:", resultado)