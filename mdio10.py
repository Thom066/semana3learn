def palindromo():
    palabra = input("\nIngrese una palabra que se escriba igual al derecho y alrevez:")
    palab = palabra[::-1]
    
    if palabra == palab:
        print("Es un palindromo ")
        print(f"\n{palab}")
    else:
        print("no es palindromo")
    
palindromo()