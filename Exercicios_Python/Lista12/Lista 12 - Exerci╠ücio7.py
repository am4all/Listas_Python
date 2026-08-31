# Exercício 7 - 7 - Uma empresa de segurança precisa desenvolver um pequeno sistema para controlar o acesso noturno de funcionários a um prédio. 
# As regras de acesso são as seguintes:
# A entrada só é permitida após as 18 horas (hora >= 18).
# Apenas os funcionários com cargo de confiança (código de acesso entre 1000 e 1999) podem entrar sozinhos.
# Funcionários com cargo não autorizado (código de acesso acima de 2000) não têm permissão de entrada.
# Funcionários com código entre 2000 e 2999 só podem entrar acompanhados por um supervisor (variável booleana: tem_supervisor = True).
# Qualquer tentativa de acesso fora do horário ou sem os critérios acima deve ser negada.

# ENTRADA
hora = int(input("Digite a hora atual (ex: 17, 18, 20): "))
codigo = int(input("Digite o número do seu crachá de acesso: "))
supervisor = input("Está acompanhado por um supervisor? (sim/nao): ")

# PROCESSAMENTO
resp_supervisor = supervisor.lower()

# SAÍDA
if hora < 18:
    print("Acesso negado! Os portões do Corujão só abrem às 18h.")
    
elif codigo >= 1000 and codigo <= 1999:
    print("Acesso autorizado!")
    
elif codigo >= 2000 and codigo <= 2999:
    # Um IF dentro do outro (condicional aninhada) para testar a segunda regra deste crachá
    if resp_supervisor == "sim":
        print("Acesso autorizado com supervisor!")
    else:
        print("Acesso negado! O supervisor precisa estar presnete para liberar o acesso.")
        
elif codigo > 2999:
    print("Acesso negado! Código de crachá não reconhecido.")
    
else:
    print("Acesso negado!")