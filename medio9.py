lista = [1,2,3,4,5,6,7,8,9]

def pares():
    for num in lista:
        if num % 2 == 0:
            print(f"\nNumeros pares: {num}")
pares()