# Revisão - Exercício 10

# ENTRADA
palavra = input("Digite a palavra Brasil: ")

# PROCESSAMENTO
# Não há cálculos necessários. As comparações diretas ocorrem na saída.

# SAÍDA
if palavra == "brasil":
    print("Você digitou tudo em minúsculo! (Bateu a preguiça no teclado?)")
elif palavra == "BRASIL":
    print("Você digitou tudo em maiúsculo! (Não precisa gritar!)")
elif palavra == "Brasil":
    print("Você digitou só com a primeira maiúscula! (Gramática perfeita, parabéns!)")
else:
    print("Você escreveu de um jeito misturado ou não reconhecido!")