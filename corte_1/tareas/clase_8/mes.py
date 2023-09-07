def main():
    dias = {
        "enero": 31,
        "febrero": 28,
        "marzo": 31,
        "abril": 30,
        "mayo": 31,
        "junio": 30,
        "julio": 31,
        "agosto": 31,
        "septiembre": 30,
        "octubre": 31,
        "noviembre": 30,
        "diciembre": 31,
    }

    f_mes = {
        "enero": 2,
        "febrero": 2,
        "marzo":7,
        "abril": 6,
        "mayo": 1,
        "junio":2,
        "julio":2,
        "agosto":2,
        "septiembre":0,
        "noviembre":2,
        "diciembre": 2,
    }

   
    mes = input("Ingrese el nombre de un mes: ").lower()

    if mes == "enero":
        print("los dias del mes son:",dias["enero"])
        print("los festivos del mes son",f_mes["enero"])
    elif mes == "febrero":
        print("los dias del mes son:",dias["febrero"])
        print("los festivos del mes son",f_mes["febrero"])
    elif mes == "marzo":
        print("los dias del mes son:",dias["marzo"])
        print("los festivos del mes son",f_mes["marzo"])
    elif mes == "abril":
        print("los dias del mes son:",dias["abril"])
        print("los festivos del mes son",f_mes["abril"])
    elif mes == "mayo":
        print("los dias del mes son:",dias["mayo"])
        print("los festivos del mes son",f_mes["mayo"])
    elif mes == "junio":
        print("los dias del mes son:",dias["junio"])
        print("los festivos del mes son",f_mes["junio"])
    elif mes == "agosto":
        print("los dias del mes son:",dias["agosto"])
        print("los festivos del mes son",f_mes["agosto"])
    elif mes == "septiembre":
        print("los dias del mes son:",dias["septiembre"])
        print("los festivos del mes son",f_mes["septiembre"])
    elif mes == "octubre":
        print("los dias del mes son:",dias["octubre"])
        print("los festivos del mes son",f_mes["octubre"])
    elif mes == "noviembre":
        print("los dias del mes son:",dias["noviembre"])
        print("los festivos del mes son",f_mes["noviembre"])
    elif mes == "diciembre":
        print("los dias del mes son:",dias["diciembre"])
        print("los festivos del mes son",f_mes["diciembre"])

    


if __name__ == "__main__":
    main()