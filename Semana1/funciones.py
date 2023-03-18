def Holo():
  print("Hello desde clase funciones hasta llamado de funciones")
def sumaNumeros(num1,num2):
    return num1+num2
def ParONo(numero):
    return(numero%2==0)
def Que_Onda(nombre, apellido="Feliz"):
  print("Que ondas")
  print(f"Bienvenido {nombre} {apellido}")
def SumarCualquier_Numero(*Numeros):
  Resultao=0
  for Numero in Numeros:
    Resultao=Resultao+Numero
  print(Resultao)
def Dicc_Productos(**datos):
  print(datos)