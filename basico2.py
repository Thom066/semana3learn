def sumaNumeros():
    numero1=int(input("Digita un numero: "))
    numero2=int(input("Digita otro numero: "))
    resultado = numero1 + numero2
    print("El resultado es: ",resultado)


while True:
    opcion=input("Digite 1 para sumar: ")
    if opcion =="1":
        sumaNumeros()
    else:
        print("Opcion invalida, Marca solo 1")

