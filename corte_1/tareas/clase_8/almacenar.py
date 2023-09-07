

def main():

    list = []

    i = 0
    while i == 0:
        opc = input("desea ingresar otro numero  (y/n): ")
        if opc == "y":
            num = float(input("ingrese un numero: "))
            list.append(num)
            print(list)
        elif opc == "n":
            print("su lista es: ")
            print(list)
            break
        else:
            print("ingrese una opcion valida")
        



if __name__=="__main__":
    main()