#Usando el metodo "in" sabremos si un elemento esta o no en la lista
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Cambiar el segundo item de la lista
thislist1 = ["apple", "banana", "cherry"]
thislist1[1] = "blackcurrant"
print(thislist1)

#Para cambiar el valor de los elementos dentro de un rango 
# específico, defina una lista con los nuevos 
# valores y consulte el rango de números de índice donde 
# desea insertar los nuevos valores:
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist3[1:3] = ["Ajoenpolvo", "Pimienta negra re100 molida"]
print(thislist3)

#Insertar un item en un lugar especifico
thislist4 = ["apple", "banana", "cherry"]
thislist4.insert(2, "watermelon")
print(thislist4)

#Para añadir un iterm usamos el metodo append()
thislist5 = ["apple", "banana", "cherry"]
thislist5.append("orange")
print(thislist5)
#Para añadir un iterm desde una posicion en especifico
thislist6 = ["apple", "banana", "cherry"]
thislist6.insert(1, "orange")
print(thislist6)
#Para unir 2 listas se usa el metodo extend()
thislist7 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist7.extend(tropical)
print(thislist)
#REmover item especifico
thislist8 = ["apple", "banana", "cherry"]
thislist8.remove("banana")
print(thislist8)
#Metodo pop remover item especifico
thislist9 = ["apple", "banana", "cherry"]
thislist9.pop(1)
print(thislist9)
#Si no especifica el índice, el método pop() elimina el último elemento.
thislist10 = ["apple", "banana", "cherry"]
thislist10.pop()
print(thislist10)
#La palabra clave "del" también elimina el índice especificado:
thislist11 = ["apple", "banana", "cherry"]
del thislist11[0]
print(thislist11)
#Eliminar una lista completa
thislist12 = ["apple", "banana", "cherry"]
del thislist12
#El método clear() vacía la lista. La lista aún permanece, pero no tiene contenido.
thislist13 = ["apple", "banana", "cherry"]
thislist13.clear()
print(thislist13)
#Imprimir una lista con el metodo for
thislistL = ["apple", "banana", "cherry"]
for x in thislistL:
  print(x)
#También puede recorrer los elementos de la lista consultando su número de índice.
#Utilice las funciones range() y len() para crear un iterable adecuado.
thislistA = ["apple", "banana", "cherry"]
for i in range(len(thislistA)):
  print(thislistA[i])
#Puede recorrer los elementos de la lista mediante un bucle while.
#Use la función len() para determinar la longitud de la lista, luego comience en 0 y recorra los elementos de la lista consultando sus índices.
#Recuerde aumentar el índice en 1 después de cada iteración.  
thislistB = ["apple", "banana", "cherry"]
i = 0
while i < len(thislistB):
  print(thislistB[i])
  i = i + 1

#Imprimir con for y sintaxis resumida
thislistC = ["apple", "banana", "cherry"]
[print(x) for x in thislistC]
#Basado en una lista de frutas, desea una nueva lista que contenga 
# solo las frutas con la letra "a" en el nombre.
#Sin comprensión de lista, tendrá que escribir una declaración 
# for con una prueba condicional dentro:
fruitsE = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruitsE:
  if "a" in x:
    newlist.append(x)
    #Tambien se puede crear una nueva lista con esta sintaxis
    #  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    #newlist = [x for x in fruits if "a" in x]
    #print(newlist)

print("De la lista de frutas: ",fruitsE," se hizo esta nueva \nlista que solo contiene palabras con la letra a")
print(newlist)
print("Esta lista imprime todo excepto la palabra 'apple' de la lista: \n",fruitsE)
newlist1 = [x for x in fruitsE if x != "apple"]
print(newlist1)

#Para imprimir una lista del 0 al 10 se puede usar la siguiente sintaxis
newlistN = [x for x in range(10)]
print(newlistN)

#Para ordenar una lista por Metodo "sort()" por abecedario asc INFLUYEN LAS MAYUSCULAS ordenando primero las mayusculas y luego las minusculas
thislistO = ["orange", "mango", "perita","kiwi", "pineapple", "banana","uvas","arandano"]
thislistO.sort()
print(thislistO)
#Ordenar una lista numerica
thislistN = [100, 50, 65, 82, 23,532,12,1]
thislistN.sort()
print(thislistN)
#ORdenar lista dsc con el metodo reverse=true
thislist = ["orange", "mango", "perita","kiwi", "pineapple", "banana","uvas","arandano"]
thislist.sort(reverse = True)
print(thislist)
#Ordenar una lista numerica dsc
thislistN = [100, 50, 65, 82, 23,532,12,1]
thislistN.sort(reverse=True)
print(thislistN)

#Ordene la lista según lo cerca que esté el número de 50:
def myfunc(n):
  return abs(n - 50)

thislistApro = [51, 50, 1, 821, 23]
thislistApro.sort(key = myfunc)
print(thislistApro)
#Ordenar lista incluso si hay mayusculas o minusculas
thislistJunt = ["banana", "Orange", "Kiwi", "cherry"]
thislistJunt.sort(key = str.lower)
print(thislistJunt)

#Imprimir de manera desc la lista
thislistRev = ["banana", "Orange", "Kiwi", "cherry"]
thislistRev.reverse()
print(thislistRev)

#Copiar una lista
thislistCOP = ["perros", "banana", "cereal","mondongo"]
mylist = thislistCOP.copy()
print(mylist)
#otro metodo para copiar una lista
thislistCOP = ["perros", "banana", "cereal","mondongo","mondongo"]
mylist = list(thislistCOP)
print(mylist)
#Unir 2 cadenas con el metodo extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3,6,7,1]
list1.extend(list2)
print(list1)
#Metodo para agregar en la lista10 lo que hay dentro de la lista20
list10 = ["a", "b" , "c"]
list20 = [1, 2, 3]
for x in list20:
  list10.append(x)
print(list10)