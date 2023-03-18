print("************************************************") 
print("Pedirà una cadena y dependiendo el tamaño saber si es palindromo o no")
while True:
    print("Si quieres jugar presiona la letra 'S' si no la letra 'N'")
    key_press=input("Elijo la opcion: ... ")[0].upper()
    print(f"Tu opcion fue; {key_press}")
    if key_press=="S":
        cadena=input("Dame una cadena de caracteres y te dire si es palindromo o nel:  ")
        cadena_invertida=cadena[::-1] #El primer " : " significa inicio y el segundo " : " final y el "-1" incremento o decremento, dependiendo del numero indica si se lee de principio a final o viceversa
        if (cadena==cadena_invertida):
            print("-------------------------------------------------") 
            print("Es palindromo la palabra: ",cadena)
            print("-------------------------------------------------") 
        else:
            print("-------------------------------------------------") 
            print("NO es palindromo la palabra: ",cadena)
            print("-------------------------------------------------")  
    elif key_press=="N":
        print("Saliendo")
        print("************************************************") 
        break
    else:
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Solo admitimos letra 'S' o 'N' ")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")