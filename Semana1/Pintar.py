lado=int(input("da tamaño del cuadrado: "))
for fila in range(lado):
    for columna in range(lado):
        if fila==0 or fila==lado -1 or columna==0 or columna==lado-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
print()
print("-------------------------------------------------")
altura=int(input("da tamaño de escalera: "))
for fila in range(altura):
    for columna in range(fila+1):
        print("* ", end="")
    print()
print("-------------------------------------------------")
alturanum=int(input("da tamaño de la escalera numerica: "))
for fila in range(1, alturanum+1):
    for columnanum in range(1, fila +1):
        print(columnanum, end="")
    print()

print("-------------------------------------------------")

altura2=int(input("da tamaño de piramide: "))
asterisco=1

for espacios in range(altura2,0,-1):

    for e in range(espacios):
        print("-", end="")

    for a in range(asterisco):
        print("* " ,end="")

    print()
    asterisco+=1
