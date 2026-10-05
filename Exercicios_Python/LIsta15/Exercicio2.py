soma = 0

for i in range(1, 5):
  nota = float(input(f"Informe a {i}ª nota: "))

  soma = soma + nota

media = soma / 4

print(f"A média é: {media:.2f}")