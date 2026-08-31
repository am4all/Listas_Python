# Exercício 2 - Você está programando o visor de um "liquidificador smart" que só aceita fazer vitaminas destas frutas: 
# banana, maçã, melancia, morango ou laranja. Faça um programa que peça para o usuário digitar o nome de uma fruta. 
# Se for uma das frutas permitidas, mostre o nome dela confirmando o pedido. Caso contrário, exiba: "Erro: Fruta desconhecida!".
# Detalhe importante: O usuário pode digitar de qualquer jeito, tipo "Maçã", "MAÇÃ" ou "maçã". 
# Use o manipulador de string .lower() para transformar tudo em minúsculo antes de verificar, 
# garantindo que o programa não dê erro por causa de letras maiúsculas.

# ENTRADA
fruta_digitada = input("Digite o nome da fruta para a sua vitamina: ")

# PROCESSAMENTO
# O método lower() retorna uma string onde todos os caracteres são minúsculos
# Assim, "MAÇÃ", "Maçã" ou "maçã" serão lidos da mesma forma.
fruta = fruta_digitada.lower()

# SAÍDA
if fruta == "banana" or fruta == "maçã" or fruta == "melancia" or fruta == "morango" or fruta == "laranja":
    print(f"Pedido confirmado! Preparando vitamina de {fruta}.")
else:
    print("Erro: Fruta desconhecida!")