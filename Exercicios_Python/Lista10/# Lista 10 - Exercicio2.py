# Lista 10 - Exercicio 2 
#2. Calculadora de IMC (Índice de Massa Corporal). Crie um algoritmo que solicite o peso (em kg) e a altura (em metros) do usuário, calcule o IMC (peso / (altura * altura)) e mostre a classificação:
#IMC abaixo de 18,5: Abaixo do peso
#IMC entre 18,5 e 24,9: Peso normal
#IMC entre 25,0 e 29,9: Sobrepeso
#IMC de 30,0 ou mais: 

# Solicita peso e altura
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros, ex: 1.75): "))

# Calcula o IMC
imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")

# Estrutura de decisão para a classificação
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc <= 24.9:
    print("Classificação: Peso normal")
elif 25.0 <= imc <= 29.9:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
