#If anidados
#Puede tener sentencias if dentro de sentencias if, esto
#  se llama sentencias if anidadas.
x = 41
if x > 10:
  print("Mas de 10,")
  if x > 20:
    print("y tambien mas de 20!")
  else:
    print("pero no mas de 20.")


#Las declaraciones if no pueden estar vacías, pero 
# si por alguna razón tiene una declaración if sin 
# contenido, ingrese la declaración "pass" para evitar recibir un error.
a = 33
b = 200
if b > a:
  pass