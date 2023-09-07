import math

def mod_vector(x1, y1, x2, y2):
    x = x2 - x1
    y = y2 - y1
    mod = math.sqrt(x**2 + y**2)
    return mod, x, y

def main():
    print("Cordenadas de inicio del vector:")
    x1 = float(input("Coordenada x: "))
    y1 = float(input("Coordenada y: "))
    
    print("cordenadas finales del vector:")
    x2 = float(input("Coordenada x: "))
    y2 = float(input("Coordenada y: "))
    
    mod, comp_x, comp_y = mod_vector(x1, y1, x2, y2)
    
    print("Resultados:")
    print("Módulo del vector:", mod)
    print("Componente x:", comp_x)
    print("Componente y:", comp_y)

if __name__ == "__main__":
    main()