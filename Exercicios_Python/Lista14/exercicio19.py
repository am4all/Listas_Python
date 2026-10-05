anoAtual = int(input("Digite o ano atual: "))

for i in range(0, 2, 1):
  nome = input(f"Digite o nome da {i+1}ª pessoa: ")
  anoNascimento = int(input(f"Digite o ano de nascimento da {i+1}ª pessoa: "))

  idade = anoAtual - anoNascimento

  print(f"{nome} tem {idade} ano(s)")
  if idade >= 18:
    print("É maior de idade")
  else:
    print("É maior de idade")
