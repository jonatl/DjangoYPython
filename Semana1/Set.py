#Los Set no duplican datos que si ingresen a este y los valores True y 1 son iguales a si que si hay
#dos valores "True" y 1 omitira uno de ellos
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#Convertir una lista a Set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#Saber si esta en el SET algo
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#se pueden agrupar incluso otro tipo de datos de listas
thisset1 = {"apple", "banana", "cherry"}
mylist1 = ["kiwi", "orange"]
thisset1.update(mylist1)
print(thisset1)
#Para remover un set, si este no está ocurrirá error, si se usa el metodo POP este metodo remueve aleatorio
#cualquier dato que esté dentro del set estaria padre usarlo para una rifa e.e
thisset2 = {"apple", "banana", "cherry"}
thisset2.discard("banana")
print(thisset2)
#metodo para imprimir todo el SET
thisset3 = {"apple", "banana", "cherry"}
for x in thisset3:
  print(x)
#Metodo para unir 2 sets dentro de uno
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#Metodo para unir 2 sets dentro de otro set, estos al unirse si hay datos duplicados se quedará solo con uno
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#Metodo que elimina los duplicados incluso de 2 sets al unirlos
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
#Mismo metodo pero este no los elimina si no que si no están presentes en los 2 Sets no los imprime
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
#agregar una nueva palabra con su valor
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
print(car)
