pares = 0 # INICIALIZAÇÃO
impares = 0 # INICIALIZAÇÃO
for i in range(1, 51, 1):
  if (i%2) == 0:
    pares += i
  else:
    impares += i

print(f"Soma dos pares: {pares}")
print(f"Soma dos ímpares: {impares}")