# Lê um número inteiro positivo N do usuário
n = int(input("Digite um número inteiro positivo (N): "))

print(f"Números naturais de 0 até {n} em ordem crescente:")
for i in range(0, n + 1):
    print(i, end=" ") # para ficar em linha ocm espaço adequado.
print()