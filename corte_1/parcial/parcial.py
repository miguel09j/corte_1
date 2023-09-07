import random as r

A = 10
J = 10
Q = 10
K = 10
cartas_n = "23456789"

def main():
    aleatorio()
    rapartir()


def aleatorio():
    i = 0
    x = 0
    while i != 2:
        x = r.choice(cartas_n)
        i = i+1
        print(f"sus cartas iniciales son: {x}")
    print(f"el conteo de sus cartas es: {x}")


def rapartir():
    n = 0
    while n < 21:
        opc = input("desea pedir otra carta (y/n) o (exit): ")
        n = 0
        i = 0
        x_n = 0
        if opc == "y":
                while i != 1:
                    x_n = r.choice(cartas_n)
                    print(f"su nueva carta es: {x_n}")
                    i = i+1
                    conteo = x_n
                    print(f"su conteo va: {conteo}")
        elif opc == "n":
            print("fin de la apuesta")
            break
        elif opc == "exit":
            print("gracias por jugar")
            break
        else: 
            print("ingrese una opcion valida")



if __name__=="__main__":
    main()