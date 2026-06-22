# Lista 6 - Exercício 4
# O algoritmo recebe um número inteiro e usa o operador de resto (%) para verificar se é múltiplo de 3. Deve exibir se é ou não é múltiplo

# ENTRADA
numero = int(input("Digite um número inteiro: "))

# PROCESSAMENTO
resto = numero % 3

# SAÍDA
if resto == 0:
    print("É múltiplo de 3")

if resto != 0:
    print("Não é múltiplo de 3")