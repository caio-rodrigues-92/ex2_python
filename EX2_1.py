def Entrada():
    num1 = int(input("Entre com um valor"))
    num2 = int(input("Entre com o segundo valor"))
    Verifica(num1,num2)

def Verifica(num1,num2):
    if num1 > num2:
        print("\nEntre de novo com os valores")
        Entrada()
    else:
        print("Segundo numero é maior")

Entrada()