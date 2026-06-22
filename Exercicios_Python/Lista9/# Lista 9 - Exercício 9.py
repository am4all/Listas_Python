# Lista 9 - Exercício 9
# Escreva um programa que pergunte o valor de um produto e se o usuário é assinante premium do aplicativo ("S" para sim ou "N" para não). Se for assinante, aplique um desconto de 20% e mostre o valor final. Caso contrário, mostre o valor original dizendo "Assine o premium para ter descontos!".

# ENTRADA
valor_produto = float(input("Digite o valor do produto: R$ "))
assinante = input("Você é assinante premium? (S=Sim / N=Não): ").upper()

# PROCESSAMENTO
valor_com_desconto = valor_produto - (valor_produto * 0.20)

# SAÍDA
# Validação: Se a resposta for diferente de S *E* diferente de N, é inválido.
if assinante != "S" and assinante != "N":
    print("Condição inválida! Digite:(S=Sim / N=Não)")
else:
    # Se passou pela validação, entra na lógica de desconto
    if assinante == "S":
        print(f"Desconto aplicado! O valor final do produto é: R$ {valor_com_desconto:.2f}")
    else:
        print(f"O valor do produto é: R$ {valor_produto:.2f}.")
        print("Assine o premium para ter descontos!")
        
        
        

# Lista 9 - Exercício 10
# Escreva um programa que pergunte o valor de um produto e se o usuário é assinante premium do aplicativo ("S" para sim ou "N" para não). Se for assinante, aplique um desconto de 20% e mostre o valor final. Caso contrário, mostre o valor original dizendo "Assine o premium para ter descontos!".

# ENTRADA
#valor_produto = float(input("Digite o valor do produto: R$ "))
#assinante = input("Você é assinante premium? (S=Sim / N=Não): ").upper()

# PROCESSAMENTO
#valor_com_desconto = valor_produto - (valor_produto * 0.20)

# SAÍDA
# Validação: Se a resposta for diferente de S *E* diferente de N, é inválido.
#if assinante != "S" and assinante != "N":
#    print("Condição inválida! Digite:(S=Sim / N=Não)")
# else:
    # Se passou pela validação, entra na lógica de desconto
    # if assinante == "S":
       # print(f"Desconto aplicado! O valor final do produto é: R$ {valor_com_desconto:.2f}")
    #else:
       # print(f"O valor do produto é: R$ {valor_produto:.2f}.")
       # print("Assine o premium para ter descontos!")