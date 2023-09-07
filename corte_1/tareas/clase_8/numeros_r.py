import random as r

def main():
    
    lista = []
    for _ in range(15):
        numero = r.randint(1, 100)  
        lista.append(numero)
        
    print("numeros ordenados ")
    for numero in lista:
        print(numero)


if __name__ == "__main__":
    main()