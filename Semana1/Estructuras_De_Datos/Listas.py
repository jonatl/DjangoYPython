lista=[1,3,2,5,3,1]
print(lista)


for x in range (len(lista)):
    print(lista[x])

#Sintaxis para recorrer una lista con su indice
for x in range (len(lista)):
    print("Index[%d]=>%d"% (x,lista[x]))

#Agregar un numero a la lista
lista=lista + [4]
print(lista)
#Retornar un valor especifico de la lista
print("Index[%d]=>%d"% (3,lista[3]))
#Retorna un valor de atras hacia adelante
print("Index[%d]=>%d"% (5,lista[-0]))
#Imprime datos en un rango especifico
print(lista[::3])
print(lista[:3])

#Listas sencillas
#Listas ordenadas
