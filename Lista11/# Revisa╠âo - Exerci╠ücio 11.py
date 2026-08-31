# Revisão - Exercício 11

# ENTRADA
jogador_a = int(input("Digite o número do personagem do Jogador A: "))
jogador_b = int(input("Digite o número do personagem do Jogador B: "))

# PROCESSAMENTO
# Criamos uma variável auxiliar (como uma gaveta vazia) para guardar o valor 
# do Jogador A temporariamente enquanto fazemos a troca.
auxiliar = jogador_a
jogador_a = jogador_b
jogador_b = auxiliar

# SAÍDA
print("--- DEPOIS DA TROCA ---")
print(f"O Jogador A agora está com o personagem: {jogador_a}")
print(f"O Jogador B agora está com o personagem: {jogador_b}")