
t_m = 139
tiempo = int(input("Ingresa el tiempo del estacionamiento: "))

sin_iva = tiempo * t_m
iva = sin_iva * 0.19
total = sin_iva + iva
total_aprox = round(total / 50) * 50

print("Valor total a pagar: ",total_aprox) 
