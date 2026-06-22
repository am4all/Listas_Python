# Lista 8 - Exercício 4
# Faça um algoritmo que efetue leitura de um valor numérico inteiro que não seja negativo. Qualquer outro valor deverá apresentar a mensagem “Valor inválido”. Se o valor estiver correto, apresentar a mensagem “Valor válido”, colocar junto a mensagem o valor fornecido. Atentar para o uso do operador lógico NOT.

# ENTRADA
valor = int(input("Digite um valor numérico inteiro não negativo: "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
# Uso do operador lógico NOT para verificar se não é negativo
if not (valor < 0):
    print(f"Valor válido. O valor fornecido foi: {valor}")

if valor < 0:
    print("Valor inválido")