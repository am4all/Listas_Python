somaGeral = 0

for i in range(1, 6):
  print(f"Notas do {i}º aluno")
  soma = 0 #precisamos zerar a soma para não continuar somando as notas dos outros alunos
  for j in range(1, 5):
    nota = float(input(f"Informe a {j}ª nota: "))

    soma += nota

  media = soma / 4

  print(f"A média é: {media:.2f}")
  somaGeral += media # para calcular a média geral precisamos somar as médias

mediaGeral = somaGeral / 5 #depois de calcular a média de todos os alunos calculamos a média geral

print(f"A média geral é: {mediaGeral:.2f}")