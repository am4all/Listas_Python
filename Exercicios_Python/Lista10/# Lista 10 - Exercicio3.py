# Lista 10 - Exercicio 3
#3. Bilheteria do Cinema. Um cinema tem o ingresso no valor de R$ 30,00. Faça um programa que pergunte a idade do cliente e se ele é estudante (S/N). O programa deve calcular o valor a ser pago considerando que:
#Estudantes ou pessoas com 60 anos ou mais têm direito a meia-entrada (50% de desconto).
#Demais pessoas pagam o valor inteiro.

valor_ingresso = 30.00

# Solicita a idade e se é estudante
idade = int(input("Digite a sua idade: "))
estudante = input("Você é estudante? (S/N): ").upper()

# Verifica se tem direito à meia-entrada
if idade >= 60 or estudante == "S":
    valor_pagar = valor_ingresso / 2
    print(f"Você tem direito a meia-entrada! O valor a pagar é R$ {valor_pagar:.2f}")
else:
    valor_pagar = valor_ingresso
    print(f"Ingresso inteiro. O valor a pagar é R$ {valor_pagar:.2f}")