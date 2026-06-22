# Lista 9 - Exercício 11

# ENTRADA
frequencia = float(input("Digite a frequência do aluno (0 a 100): "))
nota = float(input("Digite a nota do aluno (0.0 a 10.0): "))

# PROCESSAMENTO
situacao = ""

# Validação básica de limites (opcional, mas recomendada para evitar erros)
if frequencia < 0 or frequencia > 100 or nota < 0.0 or nota > 10.0:
    situacao = "Erro: Valores de frequência ou nota fora do limite permitido."
    
# Condição 1: Frequência abaixo de 75% (Reprovado direto)
elif frequencia < 75:
    situacao = "REPROVADO"
# Condições para quem tem frequência igual ou superior a 75%
elif frequencia >= 75 and nota < 3.0:
    situacao = "REPROVADO"
elif frequencia >= 75 and nota >= 3.0 and nota < 7.0:
    situacao = "EXAME"
elif frequencia >= 75 and nota >= 7.0 and nota <= 10.0:
    situacao = "APROVADO"
else:
    situacao = "Situação indefinida."

# SAÍDA
print(f"Situação do aluno: {situacao}")





# Solução 2
freq = float(input("Digite a frequência (%): "))
nota = float(input("Digite a nota (0.0 a 10.0): "))

# Verificação da situação
if freq <= 75:
    situacao = "Reprovado"
elif freq > 75 and freq <= 100:
    if nota <= 3.0:
        situacao = "Reprovado"
    elif nota < 7.0:
        situacao = "Exame"
    else:  # nota entre 7.0 e 10.0
        situacao = "Aprovado"
else:
    situacao = "Frequência inválida"

print("Situação do aluno:", situacao)