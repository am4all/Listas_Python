# Lista 9 - Exercício 10
# Calculadora simp1les: Faça um algoritmo que simule uma calculadora simples, onde o usuário informará 2 números e uma operação matemática (adição, subtração, multiplicação ou divisão). Mostre o resultado da operação que o usuário escolheu.

num1 = float(input("Informe um número: "))
num2 = float(input("Informe um número: "))

op = input("Informe uma operação: \n+: Adição\n-: Subtração\n*: Multiplicação\n/: Divisão ")

if op == '+':
  print(f"Resultado da adição: {num1 + num2}")
elif op == '-':
  print(f"Resultado da subtração: {num1 - num2}")
elif op == '*':
  print(f"Resultado da multiplicação: {num1 * num2}")
elif op == '/':
  print(f"Resultado da divisão: {num1 / num2}")
else:
  print("Operação inválida!")