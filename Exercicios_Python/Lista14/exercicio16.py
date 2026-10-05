num = int(input("Digete um númeor para imprimir sua tabuada: "))

for i in range(0, 11, 1):
  res = num * i
  print(f"3 x {i} = {res}")