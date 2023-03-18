#. Escribe un programa de un juego de dados. 
# El juego permite jugar a dos jugadores y consiste en implementar la siguiente dinámica:

#1 Se lanza un dado, y el número que sale es el objetivo de la partida.

#2. Por orden, los dos jugadores lanzan dos dados cada uno.
# Gana la partida el jugador que la suma de los dados que ha 
# lanzado coincide con el objetivo. Podemos ganar los dos, uno o ninguno de los jugadores.

#3. El juego finaliza cuando un jugador gana 2 partidas. 
# El programa debe implementar el juego descrito y cada partida, 
# el programa pregunta si se desea continuar o parar el juego.

#El juego finaliza cuando uno de los dos jugadores gana o bien 
# cuando se indica que no se quiere jugar más. Tenga en cuenta
#  que el programa al principio pide el nombre de los dos jugadores
#  y muestra la información partida a partida indicando el número
#  de partida, el objetivo de la partida, qué dados han sacado cada
#  uno los jugadores, quien gana la partida y al final del juego 
# indica quién ha ganado el juego y cuántas partidas se han jugado.

from random import *

nameP1 =input("Inserte el nombre del jugador: ")
nameP2 ="CPU"

gameWinP1 = 0
gameWinP2 = 0

numGame = 1

continueGame = True

while (gameWinP1 < 2 and gameWinP2 < 2) and continueGame:

    print("Partida nº ", numGame)

    objectivo = randint(1,6)

    print("El objetivo es ", objectivo)

    num1P1 = randint(1,6)
    num2P1 = randint(1,6)
    sumaP1 = num1P1 + num2P1

    num1P2 = randint(1,6)
    num2P2 = randint(1,6)
    sumaP2 = num1P2 + num2P2

    print("El jugador " , nameP1, " ha sacado " , num1P1, " y ", num2P1)
    print("El jugador " , nameP2, " ha sacado " , num1P2, " y ", num2P2)

    numWinners = 0
    if sumaP1 == objectivo:
        numWinners = numWinners + 1
        gameWinP1 = gameWinP1 + 1

    if sumaP2 == objectivo:
        numWinners = numWinners + 1
        gameWinP2 = gameWinP2 + 1

    if numWinners == 2:
        print("Han ganado los dos")
    elif numWinners == 1:
        if sumaP1 == objectivo:
            print("Ha ganadio el jugador ", nameP1)
        if sumaP2 == objectivo:
            print("Ha ganadio el jugador ", nameP2)
    else:
        print("No ha ganado nadie")

    continueGame = input("¿Quieres continuar? (S/N)") == "S"

    numGame = numGame + 1

print("Juego terminado")
print("Se han jugado ", numGame," partidas")

if gameWinP1 == 2:
    print("Gana ", nameP1)
if gameWinP2 == 2:
    print("Gana ", nameP2)