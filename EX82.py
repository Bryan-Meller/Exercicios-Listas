print("programa que solicita 11 valores e os apresenta na tela")
print()

valores = [0]*11

for i in range(len(valores)):
    valores[i] = float(input(f"insira o {i+1} valor: "))


for i in range(len(valores)):
    print("----------------")
    print(valores[i])
print("----------------")

