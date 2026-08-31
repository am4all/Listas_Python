# Exercício 6 - 6 - Você já mandou uma mensagem e o corretor trocou a palavra por outra nada a ver? Vamos simular isso! 
# Faça um programa que leia uma frase completa. Em seguida, peça ao usuário para digitar uma palavra que já está na frase 
# (a palavra que será substituída) e uma palavra nova (a substituta). 
# O seu programa deve procurar a palavra antiga, trocar pela nova todas as vezes que ela aparecer e mostrar a nova frase modificada na tela.

# ENTRADA
frase_original = input("Digite a frase original: ")
palavra_antiga = input("Qual palavra você quer substituir? ")
palavra_nova = input("Qual será a nova palavra? ")

# PROCESSAMENTO
# O método replace() muda uma letra, palavra ou frase de um texto para outra e retorna uma nova string[cite: 1].
frase_MOD = frase_original.replace(palavra_antiga, palavra_nova)

# SAÍDA
print("FRASE MODIFICADA:", frase_MOD)