sim = 0
nao = 0

for i in range(1, 6):  # 5 pessoas
    resposta = input(f"Pessoa {i}, você gosta de futebol? (S/N): ").strip().upper()

    if resposta == "S":
        sim += 1
    elif resposta == "N":
        nao += 1
    else:
        print("Resposta inválida! Digite apenas S ou N.")
        # opcional: repetir a pergunta se quiser garantir resposta válida

print(f"Total de respostas 'S': {sim}")
print(f"Total de respostas 'N': {nao}")