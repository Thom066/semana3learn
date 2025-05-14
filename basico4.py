def edades():
    while True:
        try:
            edadSolicitada=int(input("Digite una edad: "))
            if edadSolicitada >= 18:
                    print("Es mayor de edad")
                    break
            elif edadSolicitada>0 and  edadSolicitada<18:
                    print("Es menor de edad")
                    break
            else: 
                    print("No valido")
        except ValueError:
            print("Digite bien la edad como un entero")
        
edades()