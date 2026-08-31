# Revisão - Exercício 6

# ENTRADA
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura em metros (ex: 1.78): "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if (idade >= 14 and idade <= 17) or (altura > 1.75):
    print("Inscrição confirmada para a seletiva do time!")
else:
    print("Infelizmente você não atende aos requisitos deste ano.")