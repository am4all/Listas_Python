# Lista 8 - Exercício 3
# Faça um algoritmo que efetue a leitura de um valor numérico inteiro referente aos códigos: 1, 2 e 3. A digitação de qualquer outro valor deverá apresentar a mensagem “Código inválido”. Se o valor estiver correto, apresentar o valor digitado por extenso. 

# ENTRADA
codigo = int(input("Digite o código numérico (1, 2 ou 3): "))

# PROCESSAMENTO
# Não há cálculos necessários antes da verificação.

# SAÍDA
if codigo == 1:
    print("Um")
    
if codigo == 2:
    print("Dois")
    
if codigo == 3:
    print("Três")
    
if codigo != 1 and codigo != 2 and codigo != 3:
    print("Código inválido")