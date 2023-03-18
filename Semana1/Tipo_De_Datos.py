#Variables                                      #Tipo de dato
x = "Hello World"	                            #str	
x = 20	                                        #int	
x = 20.5	                                    #float	
x = 1j	                                        #complex	
x = ["apple", "banana", "cherry"]	            #list	
x = ("apple", "banana", "cherry")	            #tuple	
x = range(6)	                                #range	
x = {"name" : "John", "age" : 36}	            #dict	
x = {"apple", "banana", "cherry"}	            #set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	                                    #bool	
x = b"Hello"	                                #bytes	
x = bytearray(5)	                            #bytearray	
x = memoryview(bytes(5))	                    #memoryview	
x = None

#Tipo de datos especificados                            #Tipo de dato
uno = str("Hello World")	                                #str
print(uno," Es tipo de dato: ",type(uno))	
print()
dos = int(20)	                                            #int
print(dos," Es tipo de dato: ",type(dos))
print()	
tres = float(20.5)	                                        #float
print(tres," Es tipo de dato: ",type(tres))
print()	
cuatro = complex(1j)	                                    #complex
print(cuatro," Es tipo de dato: ",type(cuatro))	
print()

print(".................................")
cinco = list(("apple", "banana", "cherry"))	                #list
#Metoodo para agregar
cinco.append("orange")
#Se cambio en la posicion 1 y se agrego otra palara (ESTE METODO DE INGRESAR MANUAL SE USA EN LISTAS)
cinco[0]="Cambio de manzana a pera"
#Para imprimir solo una posicion en las listas se usa el metodo
print("Se imprime de la lista la posicion 0",cinco[0])
#Agregar en la posicion 2
cinco.insert(1,"Limones")
#Metodo para eliminar
cinco.remove("banana")
#Indexación negativa para imprimir el último elemento de la lista.
print(cinco[-1])
print(cinco," Es tipo de dato: ",type(cinco))
#Imprimir desde el segundo elemento hasta el cuarto
print(cinco[1:4]) 
#Utilice la sintaxis correcta para imprimir el número de elementos de la lista.
print(len(cinco))
#Traer elementos de la lista hasta un rango de 3
print(cinco[:4])
#Traer elementos de la lista desde un rango de 2
print(cinco[2:])
print("..........................")
print()	



seis = tuple(("apple", "banana", "cherry"))	                #tuple [Estos elementos no se modifican] 
                                                        #Pero hay una solución. Puede convertir la tupla 
                                                        # en una lista, cambiar la lista y volver a 
                                                        # convertir la lista en una tupla.
print(seis," Es tipo de dato: ",type(seis))	
siete = range(6)	                                        #range	
print()
print(siete," Es tipo de dato: ",type(siete))
print()
ocho = dict ({"name" : "John", "age" : 36})	                #dict
print(ocho," Es tipo de dato: ",type(ocho))	
print()
nueve = set({"apple", "banana", "cherry"})	                #set
print(nueve," Es tipo de dato: ",type(nueve))	
print()
diez = frozenset({"apple", "banana", "cherry"})	            #frozenset	
print(diez," Es tipo de dato: ",type(diez))
print()
once = bool(5)	                                            #bool	
print(once," Es tipo de dato: ",type(once))
print()
doce = b"Hello"	                                            #bytes
print(doce," Es tipo de dato: ",type(doce))	
print()
trece = bytearray(5)	                                    #bytearray	
print(trece," Es tipo de dato: ",type(trece))
print()
catorce = memoryview(bytes(5))	                            #memoryview	
print(catorce," Es tipo de dato: ",type(catorce))
print()
quince = None
print(quince," Es tipo de dato: ",type(quince))
print("..........................................")
xx = 1    # int
y = 2.8  # float
z = 1j   # complex

a = float(xx)
b = int(y)
c = complex(xx)
print("#convert '1' from int to float:")
print(a)
print("#convert '2.8' from float to int:")
print(b)
print("#convert '1' from int to complex:")
print(c)
print("#TIPO DE DATOS:")
print(type(a))
print(type(b))
print(type(c))

#La lista es una colección ordenada y modificable. Permite miembros duplicados.
#Tuple es una colección ordenada e inmutable. Permite miembros duplicados.
#Conjunto es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
#El diccionario es una colección ordenada** y modificable. No hay miembros duplicados.