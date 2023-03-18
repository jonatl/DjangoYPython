print("************************************************") 
print("Adivinar un numero del 1 al 100, este mismo juego nos dirà si es mayor o menor este numero como pista")
from random import *
def generar_numero_aleatorio(minimo,maximo):
    try:
        if minimo > maximo:
            aux=minimo
            minimo=maximo
            maximo=aux
            
        return randint(minimo,maximo)
    except TypeError:
        print("Escribe otro numero")
        return -1
numero_buscado=generar_numero_aleatorio(1,100)
encontrado=False
intentos=0
while not encontrado:
    numero_usuario=int(input("Introduce un numero del 1 al 100:  "))   
    if numero_usuario> numero_buscado:
        print("El numero aleatorio es menor")
        intentos=intentos+1
    elif numero_usuario< numero_buscado:
        print("El numero aleatorio es mayor")
        intentos=intentos+1
    else:
        encontrado=True
        print("Felicidades <3 el numero aleatorio era: ",numero_usuario,"Y solo te equivocaste: ",intentos," Veces")