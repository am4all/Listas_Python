# Lista 6 - Exercício 2
# O programa recebe dois números reais e calcula a soma. Se o resultado for superior a 20, subtrai 5 unidades do total. Se for igual ou menor que 20, o valor original é mantid.

# ENTRADA
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

# PROCESSAMENTO
soma = n1 + n2

if soma > 20:
    soma = soma - 5

# SAÍDA
print("O resultado final é:", soma)