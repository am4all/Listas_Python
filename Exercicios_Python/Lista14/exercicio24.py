# Lê um número inteiro positivo N do usuário
n = int(input("Digite um número inteiro positivo (N): "))

print(f"Números naturais de {n} até 0 em ordem decrescente:")
for i in range(n, -1, -1):
    print(i, end=" ")
print()