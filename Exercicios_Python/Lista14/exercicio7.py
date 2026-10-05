contador = 0
for i in range(2):
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()
    if sexo == "M" and idade > 21:
        contador += 1
print("Quantidade de homens com mais de 21 anos:", contador)