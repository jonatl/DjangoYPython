#Para añadir en tuplas primero se convierte a lista y luego de los cambios se regresa a tupla
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#Remover tupla
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#Las tuplas se nos permite extraer los valores de nuevo en variables. Esto se llama "desempacar"
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
print("¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨")
#Si el número de variables es menor que el número de valores, 
# puede agregar un * al nombre de la variable y los valores se a
# signarán a la variable como una lista:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits  #hace referencia a omitir lo que equivale a green y yellow
                                #en la lista seria igual a omitir "apple y banana" pero en
                                #*red usa un asterisco para traer todo lo que siga despues de lo
                                #que omitió... imprime de manera individual la palabra "aplle"
                                #e imprime de manera individual la palabra "banana" y lo demas
                                #lo mete en una tupla de "cherry hasta raspberry"
print(green)
print(yellow)
print(red)
#Esto es lo mismo solo que imprime el primer valor y ultimo de manera individual y lo
#demas lo mete en una tupla
print("+++++++++++++++++++++++++++++++++++++")
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#para imprimir una tupla
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#imprimir tupla
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#imprimir tupla dependiendo de su tamaño
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#Las tuplas si se pueden unir entre ellas 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)