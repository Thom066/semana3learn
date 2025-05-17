def contar():
    palabraUser = input("\nIngrese una palbra: ")
    letra =  input("\nCual letra quiere buscar para ver cuantas veces esta?: ")
    palab = palabraUser.count(letra)
    print(f"\nVeces respetida: {palab}")
    
contar()