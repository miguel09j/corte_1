
n = int(input("Ingrese un número: "))

print("Los divisores positivos de {n} son:")
for divisor in range(1, n + 1):
    if n % divisor == 0:
        print(divisor)