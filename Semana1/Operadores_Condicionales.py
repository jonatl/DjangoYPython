#   Operadores aritmeticos
#  Operador Nombre         ejemplo
#     +	    suma	        x + y	
#     - 	resta	        x - y	
#     *	    Multiplicacion	x * y	
#     /	    Division	    x / y	
#     %	    Modulus	        x % y	
#     **	Exponentiation	x ** y	
#     //	Floor division	x // y


#   Asignando Operadores aritmeticos
#Los operadores de asignación se utilizan para asignar valores a las variables.
#  Operador     Ejemplo         lo mismo
#    =	        x = 5	         x = 5	
#   +=	        x += 3	        x = x + 3	
#   -=	        x -= 3	        x = x - 3	
#   *=	        x *= 3	        x = x * 3	
#   /=	        x /= 3	        x = x / 3	
#   %=	        x %= 3	        x = x % 3	
#   //=	x       //= 3	        x = x // 3	
#   **=	x       **= 3	        x = x ** 3	
#   &=	        x &= 3	        x = x & 3	
#   |=	        x |= 3	        x = x | 3	
#   ^=	        x ^= 3	        x = x ^ 3	
#   >>=	x       >>= 3	        x = x >> 3	
#   <<=	x       <<= 3	        x = x << 3
segundos = 125
minutos = segundos // 60
segundos_sobrantes = segundos % 60  # Residuo de dividir entre 60
print("Minutos: {}, segundos: {}".format(minutos, segundos_sobrantes))
#   Operadores de comparacion
#Los operadores de comparación se utilizan para comparar dos valores:
#  Operador     Nombre          Ejemplo
#    ==	    Igual	                x == y	
#    !=	    No es igual	            x != y	
#    >	    Mayor que	            x > y	
#    3<	    Menor que	            x < y	
#    >=	    mayor que or igual que	x >= y	
#    <=	    Menor que or igual que	x <= y


#                           Operadores logicos
#Los operadores lógicos se utilizan para combinar sentencias condicionales:

#Operador           Descripcion                                                     Ejemplo
# and 	Devuelve True si ambas afirmaciones son verdaderas	                     x < 5 and  x < 10	
# or	Devuelve True si una de las afirmaciones es verdadera	                 x < 5 or x < 4	
# not	Invierte el resultado, devuelve Falso si el resultado es verdadero no   (x < 5 and x < 10)

#                           Operadores de identidad
#Los operadores de identidad se utilizan para comparar los objetos, no si son 
# iguales, sino si en realidad son el mismo objeto, con la misma ubicación de memoria:

#Operador           Descripcion                                             Ejemplo
#   is 	    Devuelve True si ambas variables son el mismo objeto             x is y	
# is not    Devuelve True si ambas variables no son el mismo objeto	        x is not y

#                           Operadores de membresía
#Los operadores de membresía se utilizan para probar si una secuencia se presenta en un objeto:
#Operador           Descripcion                                             Ejemplo
#   in 	    Devuelve True si una secuencia con el valor                     x in y	
#           especificado está presente en el objeto                        
# not in    Devuelve True si una secuencia con el valor                     x not in y
#           especificado no está presente en el objeto	        


#                               Operadores bit a bit
#Los operadores bit a bit se utilizan para comparar números (binarios):
#Operador   Nombre                  Descripcion                                                 Ejemplo
# & 	    AND	                    Establece cada bit en 1 si ambos bits son 1	                x & y	
# |         OR	                    Establece cada bit en 1 si uno de los dos bits es 1	        x | y	
# ^	        XOR	                    Establece cada bit en 1 si solo uno de los dos bits es 1    x ^ y	
# ~	        NOT	                    Invierte todos los bits	~x	
# <<	    Zero fill left shift	Desplace a la izquierda empujando ceros desde la derecha    x << 2	
#                                   y deje que los bits más a la izquierda caigan	
# >>	    Signed right shift	    Sdesplace a la derecha empujando copias del bit más a la    x >> 2
#                                   izquierda desde la izquierda, y deje que los bits más 
#                                   a la derecha caigan	
