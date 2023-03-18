try:
    print("Ingresa una operacion \n **Elevar \n*Mult \n+Sum \n-Res \/Div \n''Salir \n: ")
    Resul=""
    while True:
        if not Resul:
            Resul=input("Ingresa el numero con el que haras la operacion ")
            if Resul.lower()=="Salir":
                break
            Resul=int(Resul)
        op=input("Ingresa la operacion: ")
        if op.__str__()=="Salir":
            print("Saliendo...")
            break
        n2=input("Ingresa el siguiente numero: ")
        if n2.__str__()=="Salir":
            print("Saliendo...")
            break
        n2=int(n2)
        if op.__str__()=="Sum":
            Resul=Resul+n2
        elif op.__str__()=="Res":
            Resul=Resul-n2
        elif op.__str__()=="Mul":
            Resul=Resul*n2
        elif op.__str__()=="Div":
            Resul=Resul/n2
        elif op.__str__()=="Elev":
            Resul=Resul**n2    
        else:
            print("No se hizo nada")
            break
        print(f"El resultado es: {Resul}")
except Exception as err:
    print(err)