# Lista 6 - Exercício 8
# Manutenção de Máquina

# ENTRADA
total_produzido = int(input("Digite o total de peças produzidas: "))
total_defeitos = int(input("Digite o total de peças com defeito: "))

# PROCESSAMENTO
limite_defeitos = total_produzido * 0.10

# SAÍDA
if total_defeitos > limite_defeitos:
    print("Precisa de Manutenção")

if total_defeitos <= limite_defeitos:
    print("Normal")