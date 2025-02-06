lista = []
soma = 0


for n in range(10):
    num = int(input("Entre com valores: "))
        
    lista.append(num)
    soma = soma + num
        

maximo = max(lista)
minimo = min(lista)

print(maximo)
print(minimo)
print(soma/10)
