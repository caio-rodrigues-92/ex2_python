lista = []

for n in range(10):
    num = int(input("Entre com valores: "))
        
    lista.append(num)

const = int(input("Entre com uma constante: "))

for t in range(10):
    
    print(lista[t],"*", const, "=", lista[t] * const)
