# Exercício 5 - Ninguém gosta de tomar spoiler da série favorita no grupo do WhatsApp! 
# Crie um programa de segurança: ele deve pedir para o usuário colar uma mensagem (frase) 
# e depois digitar a "palavra proibida" (por exemplo: "morre" ou "final"). 
# O algoritmo deve apenas verificar e avisar: exiba "ALERTA: A palavra proibida está na mensagem!" 
# se ela existir na frase, ou "Tudo limpo, pode ler tranquilo!" se ela não aparecer.

# ENTRADA
mensagem = input("Cole a mensagem do grupo aqui: ")
palavra_proibida = input("Digite a palavra proibida (spoiler): ")

# PROCESSAMENTO
# O método find() retorna a primeira ocorrência de um valor específico na string.
# Caso não encontre o valor será retornado -1.
posicao = mensagem.find(palavra_proibida)

# SAÍDA
if posicao > -1:
    print("ALERTA: A palavra proibida está na mensagem! Cuidado com o spoiler.")
else:
    print("Tudo limpo, pode ler tranquilo!")