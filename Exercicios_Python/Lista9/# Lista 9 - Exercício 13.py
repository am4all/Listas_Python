# Lista 9 - Exercício 13


# preços por litro
preco_alcool = 1.90
preco_gasolina = 2.70

# entrada de dados
litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A - álcool, G - gasolina): ").upper()

# cálculo do preço e desconto
if tipo == "A":
    preco = preco_alcool
    if litros <= 25:
        desconto = 0.02
    else:
        desconto = 0.04
elif tipo == "G":
    preco = preco_gasolina
    if litros <= 25:
        desconto = 0.03
    else:
        desconto = 0.05
else:
    print("Tipo de combustível inválido.")
    exit()

# valor total com desconto
valor_bruto = litros * preco
valor_final = valor_bruto * (1 - desconto)

print(f"Valor a ser pago: R$ {valor_final:.2f}")
