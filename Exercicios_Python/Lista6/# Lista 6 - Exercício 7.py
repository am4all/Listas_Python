# Lista 6 - Exercício 7
# Tabela de preços de fotocópias

# ENTRADA
copias = int(input("Digite a quantidade de cópias desejadas: "))

# PROCESSAMENTO
if copias <= 100:
    valor_total = copias * 0.25

if copias > 100:
    valor_total = copias * 0.20

# SAÍDA
print(f"O valor total da fatura é: R$ {valor_total:.2f}")