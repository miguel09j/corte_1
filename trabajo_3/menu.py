

print("1. vocal o consonante")
print("2. estacionaminto")
print("3. tipo de triangulo")


opc = int(input("ingrese una opcion: "))

if opc == 1:
    l  = input("ingrese una letra: ")
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        print("la letra es una vocal ")
    else:
        print("la letra es una consonante")
elif opc == 2:
    t_m = 139
    tiempo = int(input("Ingresa el tiempo del estacionamiento: "))
    sin_iva = tiempo * t_m
    iva = sin_iva * 0.19
    total = sin_iva + iva
    total_aprox = round(total / 50) * 50
    print("Valor total a pagar: ",total_aprox) 
elif opc == 3:
    l_1 = float(input("ingrese el primer lado: "))
    l_2 = float(input("ingrese el segundo lado: "))
    l_3 = float(input("ingrese el tercer lado: "))

    if l_1 == l_2 and l_1 == l_3:
        print(" el triangulo es equilátero")
    elif l_1 == l_2 or l_1 == l_3 or l_2 == l_3:
        print("el triangulo es isoseles")
    elif l_1 != l_2 and l_1 != l_3 and l_2 != l_3:
        print("el triangulo es escaleno")


