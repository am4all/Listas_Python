num = int(input("Digite o 1º número: "))

maior = menor = num
# MAIOR = NUM  --- O QUE FAZ ISSO SER VALIDO/INVALIDO?
# MENOR = NUM
# COMO AINDA NÃO TEMOS NUMERO PARA COMPARAR O QUE FOI DIGITADO É O MAIOR
# COMO AINDA NÃO TEMOS NUMERO PARA COMPARAR O QUE FOI DIGITADO É O MENOR


for i in range(2, 6, 1):
  num = int(input(f"Digite o {i}º número: "))# QUAL MOTIVO DO FOR ESTAR AQUI?
  if num > maior: # SE O NUMERO DIGITADO FOR MAIOR QUE O ATUAL ATUALIZAMOS A VAR MAIOR
    maior = num

  if num < menor: # SE O NUMERO DIGITADO FOR MENOR QUE O ATUAL ATUALIZAMOS A VAR MENOR

    menor = num

print(f"O maior número é: {maior}")

print(f"O menor número é: {menor}")