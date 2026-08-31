# Exercício 9 - Uma empresa quer validar códigos de produto com as seguintes regras:
# ● O código é uma string com exatamente 10 caracteres.
# ● Deve conter a substring "PROD" (maiúscula ou minúscula) em qualquer posição.
# ● Deve conter exatamente 3 números (0-9) em toda a string.
# ● O código não pode conter a letra "X" (maiúscula ou minúscula).
# Se o código for válido, exiba "Código válido". Caso contrário, informe o motivo da rejeição.

codigo = input("Digite o código do produto: ")

# Verificar tamanho
if len(codigo) != 10:
    print("Código inválido: deve ter 10 caracteres")
# Verificar substring PROD (case insensitive)
elif codigo.lower().find("prod") == -1:
    print("Código inválido: deve conter 'PROD'")
# Contar números na string
else:
    numeros = codigo.count("0") + codigo.count("1") + \
              codigo.count("2") + codigo.count("3") + \
              codigo.count("4") + codigo.count("5") + \
              codigo.count("6") + codigo.count("7") + \
              codigo.count("8") + codigo.count("9")
    if numeros != 3:
        print("Código inválido: deve conter exatamente 3 números")
    # Verificar se contém letra X (case insensitive)
    elif codigo.lower().find("x") != -1:
        print("Código inválido: não pode conter a letra 'X'")
    else:
        print("Código válido")