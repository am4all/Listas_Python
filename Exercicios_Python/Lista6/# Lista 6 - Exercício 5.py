# Lista 6 -  Exercício 5
# O programa lê um número e verifica se atende a dois critérios simultaneamente: ser divisível por 3 e por 7. Utiliza operadores lógicos para validar ambas as condições.

# ENTRADA
numero = int(input("Digite um número inteiro: "))

# PROCESSAMENTO
resto3 = numero % 3
resto7 = numero % 7

# SAÍDA
if resto3 == 0 and resto7 == 0:
    print("O número é divisível por 3 e por 7 simultaneamente.")

if resto3 != 0 or resto7 != 0:
    print("O número NÃO atende aos dois critérios simultaneamente.")