def entrada(): 
    gen = input("Entre com seu genero (Digitar sem CAPS LOCK)")
    verifica(gen)


def verifica(gen):
    if "m" != gen != "f":
        print("Dados inválidos\nEntre com outros valores\n\n")
        entrada()
    else:
        if gen == "m":
            print("Genro Maculino seleionado")

        elif gen == "f":
            print("Genero Feminino seleionado")




entrada()