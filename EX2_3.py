def entrada():
    num = int(input("Entre com valor para ver sua tabuada"))
    verifica(num)

def verifica(num):
    if num < 0:
        print("Valor inválido\nEntre com um valor positivo")
        entrada()

    else:        
        #for n in range(10):
        #    n = n+1
        #    print(num, "x", n, "=", n*num )

        contador = 0
        while (contador > 11):
            
            print(contador, " x ", num, " = ",contador*num )

            contador = contador  + 1
            print()
        print("FIM!!")

entrada()