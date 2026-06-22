# Lista 7 - Exercício 9
# Crie um algoritmo que leia o salário de um funcionário e o tempo de serviço em anos. Se o tempo de serviço for superior a 5 anos, adicione R$ 500,00 ao salário e mostre o valor atualizado.

# ENTRADA
salario = float(input("Digite o salário do funcionário: R$ "))
tempo_servico = int(input("Digite o tempo de serviço (em anos): "))

# PROCESSAMENTO
novo_salario = salario + 500.00

# SAÍDA
if tempo_servico > 5:
    print(f"Bônus aplicado! O salário atualizado é: R$ {novo_salario:.2f}")