from Semana1.funciones import *
try:
    print("1.- ","def Holo")
    print("2.- ","def SumarNumeros")
    print("3.- ","def ParONo")
    print("4.- ","def QueOnda")
    print("5.- ","def SumaCualquier_Numero")
    print("6.- ","def Dicc_Productos")
    seleccion=int(input("Selecciona que funcion quieres ejecutar: "))
    if (seleccion)==1:
        Holo()
    elif (seleccion)==2:
        print("Funcion que te pide sumar 2 numeros")
        num1=int(input("mete un numero entero pa sumarlo va?; "))
        num2=int(input("mete el otro numero para sumarlo con el primero; "))
        resultado=print(sumaNumeros(num1,num2))
        print("La suma del numero ",num1," Y el numero ",num2," Es igual a: ",resultado)
    elif (seleccion)==3:
        print("Funcion que te pide numero y dice si es par o no")
        numero=int(input("Elije un numero y yo te dijo si es par o no: ... "))
        print(f"Tu opcion fue; {numero}")
        print(ParONo(numero))
        print("-------------------------")  
    elif (seleccion)==4:
        Que_Onda("Monge","Loco")
        Que_Onda("ESte es un argumento qu ele falta otro pero se lo agrega por defecto")
    elif (seleccion)==5:
        SumarCualquier_Numero(1,4,2,643,2)  
    elif (seleccion)==6:
        Dicc_Productos(id=132,
        marca="Xiaomi",
        precio=12423,
        calidad="Precio")
    else:
        print("nope")
except Exception as err:
    print(err)