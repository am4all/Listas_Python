# Lista 10 - Exercicio 5
#5. Identificador de Triângulos. Faça um programa que receba três valores informados pelo usuário (representando os lados de um triângulo). Primeiro, verifique se os valores formam um triângulo (a soma de dois lados deve ser sempre maior que o terceiro lado). Se formarem, classifique-o:
#Equilátero: três lados iguais.
#Isósceles: dois lados iguais.
#Escaleno: três lados diferentes.
#Se não formarem um triângulo, exiba uma mensagem de erro.

# Solicita os 3 lados
a = float(input("Digite o tamanho do primeiro lado: "))
b = float(input("Digite o tamanho do segundo lado: "))
c = float(input("Digite o tamanho do terceiro lado: "))

# Verifica se formam um triângulo 
# (soma de dois lados MENORES precisa ser MAIOR que o terceiro)
if (a + b > c) and (a + c > b) and (b + c > a):
    # Se formar, classifica o triângulo
    if a == b and b == c:
        print("Os valores formam um triângulo Equilátero.")
    elif a == b or a == c or b == c:
        print("Os valores formam um triângulo Isósceles.")
    else:
        print("Os valores formam um triângulo Escaleno.")
else:
    print("Erro: Os valores informados NÃO formam um triângulo.")
