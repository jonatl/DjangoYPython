import sys
while True:
    try:
        x = int(input("Mete un numero real: "))
        print("saliendo del bucle")
        break
    except ValueError:
        print("Oops!  Ese no es un numero real.  Try again...")

s=100
try:
    print(s, "Todo bien")
except:
    print("hubo un error")

try:
    print(5),
except:
    print("Algo salio mal")
else:
    print("No hubo error")

g=4
try:
    print(4.2)
except Exception as err:
    print(err)
finally:
    print("la ejecicon de la tarea ya terminó")

z=300
try:
    if z > 300:
        raise Exception("Numero muy grande")
    print("Todo salio bien")
      
#Error de sintaxis "SyntaxError: invalid syntax"
#while True print("helo")
#arreglo 

    x="ma"
    while x=="ma":
        print("HEllo")
        break
except Exception as err:
    print(err)
print(".....................................................................")

#Manejo de errores
try:
    print("Ingresa una operacion \n **Elevar \n*Mult \n+Sum \n-Res \/Div \n''Salir \n: ")
    Resul=""
    while True:
        if not Resul:
            while True:
                try:
                    Resul=input("Ingresa el numero con el que haras la operacion ")
                    if Resul.__str__()=="Salir":
                        sys.exit()
                    Resul=int(Resul)
                    break
                except ValueError:
                    print("los valores no fueron correctos: ")
        op=input("Ingresa la operacion: ")
        if op.__str__()=="Salir":
            print("Saliendo...")
            break   
        #Dentro de arreglo meter las opciones
        opciones=("Sum","Div","Res","Mul","Elev")
        while op in opciones:
                try:
                    n2=input("Ingresa el numero con el que haras la operacion junto con el otro numero")
                    if n2.lower()=="Salir":
                        break
                    n2=int(n2)
                    break
                except ValueError:
                    print("Solo puedes ingresar valores numericos")
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
            #Al momento de manejar un error se puede especificar y mostrar otro 
            try:
                Resul=Resul/n2
            except ZeroDivisionError:
                print("No se puede dividir entre 0")
        elif op.__str__()=="Elev":
            Resul=Resul**n2    
        else:
            print("No se hizo nada ya que no ingresaste correctamente la operacion")
            break
        print(f"El resultado es: {Resul}")
except Exception as err:
    print(err)