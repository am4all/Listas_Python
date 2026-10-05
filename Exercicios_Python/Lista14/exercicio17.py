# num1 = 5
# num2 =3

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))

soma = 0 # INICIALIZAÇÃO

for i in range(0, num2, 1): # O FOR VAI REPETIR O BLOCO DE CÓDIGO NUM2 VEZES (3).
  soma += num1 # ITERAÇÃO 1 = SOMA = 0 + 5 = 5
               # ITAREÇÃO 2 = SOMA = 5 + 5 = 10
               # ITERAÇÃO 3 = SOMA = 10 + 5 = 15

print(f"O resultado da soma é: {soma}")