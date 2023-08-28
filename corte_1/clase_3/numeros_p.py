n = int(input("ingrese la cantidad de numeros primos que desea: "))
x = 1
num = 2
print("1")

while x < n:
    for i in range(2,num+1):
        primo = num%i
        if (primo == 0 and num == i):
            print(num)
            num+=1
            x+=1
        elif (primo==0 and num!=i):
            num+=1
            break
