# Lista 9 - Exercício 12

# ENTRADA
idade = int(input("Digite a idade do nadador: "))

# PROCESSAMENTO
categoria = ""

if idade < 5:
    categoria = "Idade inferior à mínima exigida (sem categoria)"
elif idade >= 5 and idade <= 7:
    categoria = "Infantil A"
elif idade >= 8 and idade <= 10:
    categoria = "Infantil B"
elif idade >= 11 and idade <= 13:
    categoria = "Juvenil A"
elif idade >= 14 and idade <= 17:
    categoria = "Juvenil B"
elif idade >= 18:
    categoria = "Sênior"

# SAÍDA
print(f"A categoria do nadador é: {categoria}")