
#HAcer una funciion con un arreglo y sumar todos los valores
def Sumar(*Numeros):
    try:
        Resu=0
        for sum in Numeros:
            Resu=Resu+sum
        print(Resu)
    except TypeError:
        print("No se puede sumar"+TypeError)
Sumar(1,3,2,4,77)