# Exercício 1 - Imagine que você está ajudando a calcular a conta de luz, mas precisa saber se o gasto veio do seu quarto (Residência), da loja do seu bairro (Comércio) ou de uma fábrica de eletrônicos (Indústria). Escreva um programa que pergunte a quantidade de energia consumida (em kWh) e o tipo de local: digite R para Residência, C para Comércio ou I para Indústria.Calcule o valor da conta usando a tabela abaixo. Atenção: O usuário pode acabar digitando letras minúsculas (r, c, i). Use o manipulador de texto upper() no seu código para transformar qualquer letrinha em maiúscula antes de fazer os testes de condicionais.
# Residencial (R): Até 500 kWh = R$ 0,40 | Acima de 500 kWh = R$ 0,65
# Comercial (C): Até 1000 kWh = R$ 0,55 | Acima de 1000 kWh = R$ 0,60
# Industrial (I): Até 5000 kWh = R$ 0,55 | Acima de 5000 kWh = R$ 0,60

# ENTRADA
consumo = float(input("Digite a quantidade de energia consumida (em kWh): "))
tipo_instalacao = input("Digite o tipo de local (R para Residência, C para Comércio, I para Indústria): ")

# PROCESSAMENTO
# O método upper() retorna uma string onde todos os caracteres são maiúsculos.
# Isso garante que o programa funcione mesmo se o usuário digitar 'r', 'c' ou 'i'.
tipo = tipo_instalacao.upper()

# SAÍDA
if tipo == "R":
    if consumo <= 500:
        preco = 0.40
    else:
        preco = 0.65
    print(f"Instalação Residencial. Total a pagar: R$ {consumo * preco:.2f}")

elif tipo == "C":
    if consumo <= 1000:
        preco = 0.55
    else:
        preco = 0.60
    print(f"Instalação Comercial. Total a pagar: R$ {consumo * preco:.2f}")

elif tipo == "I":
    if consumo <= 5000:
        preco = 0.55
    else:
        preco = 0.60
    print(f"Instalação Industrial. Total a pagar: R$ {consumo * preco:.2f}")

else:
    print("Erro: Tipo de instalação inválido!")