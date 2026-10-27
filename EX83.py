print("programa para gravar 18 numero inteiros e lista-los em ordem inversa a de entrada")
print()

valores = [0]*18

for i in range(len(valores)):
    valores[i] = int(input(f"insira o {i+1} valor: "))

valores.reverse()
print(valores)