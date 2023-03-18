
def funcion_decoradora(funcion_parametro):
    #la siguiente funcion es la que se retorna
   
    def funcion_interior():
        #Acciones adifionales que decoran
        sumar=0
        funcion_parametro()
        total=sumar
        total=sumar+1
        print(total)
        #Acciones adifionales que decora
    return funcion_interior

def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)

@funcion_decoradora
def suma():
    print(13+123)
@funcion_decoradora
def resta():
    print(13-3)
suma()
resta()