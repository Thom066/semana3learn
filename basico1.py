
def saludoPersonalizado():
    nombre = input("Digita tu nombre: ")
    mensajePersonalizado = ("Bienvenido, un placer tenerte por aca ")
    print(mensajePersonalizado+nombre)

while True:
        print("1) Saludo")
        opcion = input("Digite una opcion: ")
        if opcion == "1":
            saludoPersonalizado()
        else :
            print("Opcion invalida")
            break

