# Lista 8 - Exercício 5
# Faça um algoritmo que leia de dois valores numéricos e efetue a adição. Caso o valor somado seja maior ou igual a 10, o resultado apresentado deve ser apresentado somando mais 5. Caso o valor somado não seja maior ou igual a 10, o resultado apresentado deverá ser subtraído de 7.  

# ENTRADA
valor1 = float(input("Digite o primeiro valor numérico: "))
valor2 = float(input("Digite o segundo valor numérico: "))

# PROCESSAMENTO
soma = valor1 + valor2

# SAÍDA
if soma >= 10:
    resultado = soma + 5
    print(f"O valor somado foi >= 10. O resultado final ajustado (+5) é: {resultado}")

if soma < 10:
    resultado = soma - 7
    print(f"O valor somado foi < 10. O resultado final ajustado (-7) é: {resultado}")