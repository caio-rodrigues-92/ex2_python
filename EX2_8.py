lista = []

for n in range(10):
    num = int(input("Entre com valores: "))
        
    lista.append(num)

reverso = sorted(lista, reverse=True)
print(reverso)