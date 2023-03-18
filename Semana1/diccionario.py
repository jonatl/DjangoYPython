#Asi se hace un diccionario
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)
#asi se convierte
thisdict1 = dict(name = "John", age = 36, country = "Norway")
print(thisdict1)
#Imprimir algo especifico en un diciconario
thisdict3 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict3["model"]
print(x)
#devuelve las llaves que hay dentro del diccionario
x1 = thisdict.keys()
print(x1)


#tambien asi
y = thisdict3.get("brand")
print(y)
#devuelve las llaves que hay dentro del diccionario con el metodo keys()
y1 = thisdict.keys()
print(y1)

#Añadir un nuevo item
car2 = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
z = car2.keys()
print(z) #before the change
car2["color"] = "white"
print(z) #after the change

#para ver lo que contiene el objeto diccionario creado con el metodo Values()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
s = thisdict.values()
print(s)
#Modificar valores antes y despues
carrito = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
r = carrito.values()
print(r) #before the change
carrito["year"] = 2020
print(r) #after the change

#Metodo items() trae consigo las llaves y los valores del diccionario creado
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)
# Verificar si el la llave "model" existe en el diccionario
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Simio si está")

#Metodo para actualizar datos en el diccionario
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
#Agregamos tambien otra llave y valor
thisdictsisi = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdictsisi.update({"color": "red"})
print(thisdictsisi)

#Para eliminar una llave usamos el metodo POP() y especificamos que llave queremos quitar
#de lo contrario el metodo eliminara una llave en modo random 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#tambien se puede eliminar con el metodo "del" si no especificamos va a borrar todo pero al momento de imprimirlo
#va a retornar error porque no tiene nada
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#El metodo clear() si elimina todo pero si puedes imprimir el diccionario vacio
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

#imprime solo las llaves
thisdictllaves =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdictllaves:
  print(x)
#o tambien
for x in thisdictllaves.keys():
    print(x)

#imprime los valores
thisdictki =    {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for t in thisdictki:
  print(thisdictki[t])
#o tambien
for u in thisdictki.values():
  print(u)

#Recorrer con un loop el diccionario y traernos llaves y valores
thisdictAmbos =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdictAmbos.items():
  print(x, y)
#Crear mas de 2 diccionarios en uno
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)