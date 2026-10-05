# Inicializa os contadores para cada faixa etária
faixa1 = 0  # Até 15 anos
faixa2 = 0  # De 16 a 30 anos
faixa3 = 0  # De 31 a 45 anos
faixa4 = 0  # De 46 a 60 anos
faixa5 = 0  # Acima de 61 anos

print("--- Pesquisa de Faixa Etária ---")

# Laço para receber a idade de 15 pessoas (de 1 a 15)
for i in range(1, 3):
  idade = int(input(f"Digite a idade da {i}ª pessoa: "))

  # Verifica em qual faixa etária a idade se encaixa
  if idade <= 15:
    faixa1 += 1
  elif idade <= 30:
    faixa2 += 1
  elif idade <= 45:
    faixa3 += 1
  elif idade <= 60:
    faixa4 += 1
  else:
    faixa5 += 1

# Exibe o resultado final após a leitura das 15 idades
print("\n=== Resultado da Quantidade por Faixa Etária ===")
print(f"Até 15 anos: {faixa1} pessoa(s)")
print(f"De 16 a 30 anos: {faixa2} pessoa(s)")
print(f"De 31 a 45 anos: {faixa3} pessoa(s)")
print(f"De 46 a 60 anos: {faixa4} pessoa(s)")
print(f"Acima de 61 anos: {faixa5} pessoa(s)")