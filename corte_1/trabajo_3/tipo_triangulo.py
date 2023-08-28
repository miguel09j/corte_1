
l_1 = float(input("ingrese el primer lado: "))
l_2 = float(input("ingrese el segundo lado: "))
l_3 = float(input("ingrese el tercer lado: "))

if l_1 == l_2 and l_1 == l_3:
    print(" el triangulo es equilátero")
elif l_1 == l_2 or l_1 == l_3 or l_2 == l_3:
    print("el triangulo es isoseles")
elif l_1 != l_2 and l_1 != l_3 and l_2 != l_3:
    print("el triangulo es escaleno")