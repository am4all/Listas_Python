for i in range(1, 5):
  print(f"Notas do {i}º aluno")
  soma = 0 #precisamos zerar a soma para não continuar somando as notas dos outros alunos
  for j in range(1, 5):
    nota = float(input(f"Informe a {j}ª nota: "))

    soma += nota

  media = soma / 4 # a média é calculada somente depois que todas as notas forem informadas

  print(f"A média é: {media:.2f}")