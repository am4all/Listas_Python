# Lista 10 - Exercicio 4
#4. Radar de Trânsito. Escreva um programa que leia a velocidade de um carro. O limite da via é de 80 km/h: 
#Se a velocidade for menor ou igual a 80 km/h, imprima "Velocidade permitida. Boa viagem!".
#Se a velocidade for entre 81 e 100 km/h, imprima "Aviso: Você está acima do limite de velocidade!".
#Se a velocidade for maior que 100 km/h, imprima "Multado! Você excedeu muito o limite de velocidade.".



velocidade = float(input("Digite a velocidade do carro em km/h: "))

# Estrutura de decisão
if velocidade <= 80:
    print("Velocidade permitida. Boa viagem!")
elif 81 <= velocidade <= 100:
    print("Aviso: Você está acima do limite de velocidade!")
else:
    print("Multado! Você excedeu muito o limite de velocidade.")