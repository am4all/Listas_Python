# Revisão - Exercício 7

# ENTRADA
bateria = float(input("Digite o nível atual da bateria (apenas o número): "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if bateria > 20:
    print("Bateria ok. Pode continuar usando as redes sociais.")
elif bateria >= 5 and bateria <= 20:
    print("Aviso: Bateria fraca! Conecte o carregador.")
else:
    print("Bateria crítica. O celular vai desligar em instantes.")