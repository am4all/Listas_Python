# Revisão - Exercício 3


# ENTRADA
saldo = int(input("Digite o seu saldo de moedas no jogo: "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if saldo < 500:
    print("Saldo insuficiente para comprar skins.")     
elif saldo >= 500 and saldo <= 999:
    print("Você pode comprar uma Skin Comum.")
elif saldo >= 1000 and saldo <= 1999:
    print("Você pode comprar uma Skin Épica.")
    
# elif 500 <= saldo <= 999:
#    print("Você pode comprar uma Skin Comum.")
# elif 1000 <= saldo <= 1999:
#    print("Você pode comprar uma Skin Épica.")

else:
    print("Você pode comprar uma Skin Lendária!")