# Revisão - Exercício 9 

# ENTRADA
p1 = int(input("Digite a 1ª pontuação: "))
p2 = int(input("Digite a 2ª pontuação: "))
p3 = int(input("Digite a 3ª pontuação: "))

# PROCESSAMENTO
# Testando as 6 ordens possíveis de pontuação
if p1 > p2 and p2 > p3:
    maior = p1
    intermediario = p2
    menor = p3
    
elif p1 > p3 and p3 > p2:
    maior = p1
    intermediario = p3
    menor = p2
    
elif p2 > p1 and p1 > p3:
    maior = p2
    intermediario = p1
    menor = p3
    
elif p2 > p3 and p3 > p1:
    maior = p2
    intermediario = p3
    menor = p1
    
elif p3 > p1 and p1 > p2:
    maior = p3
    intermediario = p1
    menor = p2
    
else:
    # Se não foi nenhuma das anteriores, só sobrou uma possibilidade:
    maior = p3
    intermediario = p2
    menor = p1

# SAÍDA
print("--- PÓDIO ---")
print(f"1º Lugar (Maior): {maior}")
print(f"2º Lugar (Intermediário): {intermediario}")
print(f"3º Lugar (Menor): {menor}")