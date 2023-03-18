
print("#----------IMPRIMIR UN SALUDO-------------#")
print("Saludote")
print("************************************************")
print("#----------SUMAR DOS NUMEROS-------------#")
Primero=13
Segundo=14
Tercero=Primero+Segundo
print("La suma del numero: ",Primero," Mas el numero: ",Segundo,"es = ",Tercero)
print("************************************************")
print("#----------PORCENTAJE DE UN NUMERO-------------#")
IVA = 0.31
numero = 100
PrecioIVA=numero * IVA
print("El porcentaje del iva del numero 100 es: ", PrecioIVA)
print("El total con iva es de: ", PrecioIVA+numero)
print("************************************************")
print("#---------- DE 2 NUMEROS SABER CUAL ES MAYOR-------------#")
num1=15
num2=31
if (num2<num1):
    print("El numero: ",num1,"Es mayor que: ",num2) 
else:
    print("El numero: ",num2,"Es mayor que: ",num1) 
print("************************************************")
print("#---------- crear una variable si está entre el 1 a 10 -------------#")
va=23
if (va>=1 and va<=10):
    print("El numero: ",va,"esta entre el 1 al 10") 
else:
    print("NEEEELLL El numero: ",va," NO esta entre el 1 al 10")  
print("************************************************")

print("#---------- si está entre el 1 a 10 mostrar mensaje y si del 11 al 20 otro-------------#")
chek=15

if (chek>=1 and chek<=10):
    print("El numero: ",chek,"esta entre el 1 al 10") 
elif(chek>=11 and chek<=20):
    print("El numero: ",chek,"esta entre el 11 al 20") 
else:
    print("Nope") 
print("************************************************")

print("#---------- con while imprimir 100 veces amlover-------------#")
aux1=1
while( aux1<=100):
    print("AMLOVER")
    aux1+=1
print("Fin del bucle")

print("************************************************")

print("#---------- con FOR imprimir del 1 al 100-------------#")
aux1=1
for aux1 in range(1,101):
    print(aux1)

print("Fin del bucle con FOR")

print("************************************************")

print("#---------- imprimir caracteres de Holamundo-------------#")   
aux2=1
for aux2 in "Hola mundo":
    print(aux2)

print("************************************************")

print("#---------- mostrar los pares del 1 al 100 primera opcion------------#")  
aux3=1 
for aux3 in range(1,101):
    if ((aux3%2)==0):
        print(aux3)
print("Numeros pares con for")
print("#---------- mostrar los pares del 1 al 100 segunda opcion------------#")  
aux4=2 
for aux4 in range(2,101,2):
    print(aux4)
print("Numeros pares con for ")
print("************************************************") 
print("rango del 0 al 9")
rango=list(range(10))
print(rango)
print("************************************************") 
print("rango del 1 al 10")
rango=list(range(1,11))
print(rango)
print("************************************************") 
print("conteo regresivo del 10 al 0")
rango=list(range(10,-1,-1))
print(rango)
print("************************************************") 
print("conteo del 0 al 10 junto al 15 al 20")
rango=list(range(0,11))
rango2=list(range(15,21))
union=rango+rango2
print(union)
print("************************************************") 
print("rango dependiendo de la cadena de caracteres 'Hola mundo'")
cadena=list(range(0,len("Hola mundo")))
print(cadena)
print("************************************************") 
print("pide 2 cadenas, muestra estas 2 cadenas con un espacio pero con los 2 primeros caracteres intercambiados por ejemplo 'Hola Mundo' pasa a 'Mula Hondo'")
cadenita1=input("dame una cadena: ")
cadenita2=input("DAme otra cadena: ")
print(cadenita2[:2]+cadenita1[2:]+" "+cadenita1[:2]+cadenita2[2:]) #":2" muestra los primeros 2 caracteres, "2:" muestra los ultimos 2 caracteres.