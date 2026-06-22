# Lista 8 - Exercício 2
# Faça um algoritmo que aceite valores numéricos inteiros entre 0 e 9. Se o valor estiver dentro da faixa, o programa deverá apresentar a mensagem “Valor válido”. Caso o valor esteja fora da faixa apresentada a mensagem deverá ser “Valor inválido". É obrigatório o uso do operador lógico E é em seguida o operador OU.

# ENTRADA
valor = int(input("Digite um valor numérico inteiro: "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
# Verificação com o operador E (AND)
if valor >= 0 and valor <= 9:
    print("Valor válido")

# Verificação com o operador OU (OR)
if valor < 0 or valor > 9:
    print("Valor inválido")