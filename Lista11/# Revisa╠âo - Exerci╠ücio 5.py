# Revisão - Exercício 5

# ENTRADA
trabalhos = input("Você terminou todos os trabalhos escolares? (S/N): ")
quarto = input("Você arrumou o seu quarto? (S/N): ")

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if (trabalhos == "S" or trabalhos == "s") and (quarto == "S" or quarto == "s"):
    print("Liberado! Bom passeio no shopping.")
else:
    print("Fim de semana cancelado. Vá terminar suas obrigações!")