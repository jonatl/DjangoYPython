# Se recorre el arreglo de inicio a fin de la lista
# Cada elemento de la lista se ordena si a su izquierda tiene un elemento mayor que el actual
# Si es correcto el paso anterior, se hace el intercambio de valores
# El elemento se sigue recorriendo hacia la izquierda hasta que tenga un elemento menor que el

lista=[1,5,3,1,3,57,46,3,42,345,3]
print("Lista actual: ",lista)
for i in range(1,len(lista)):
    aux=lista[i]
    j=i-1
    while j>=0 and aux <lista[j]:
        lista[j+1]=lista[j]
        lista[j]=aux
        j-=1
print("Lista ordenada: ",lista)