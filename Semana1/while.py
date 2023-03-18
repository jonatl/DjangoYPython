# imprimir un numero hasta que se cumpla la funcion
i = 1
while i < 6:
  print(i)
  i += 1
# Los comandos break pueden romper el ciclo incluso cuando este se cumpla
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#Con la instrucción continuar podemos detener la iteración actual y continuar con la siguiente:
i = 0
while i < 6:
  i += 1
  if i == 3: #aqui omite el numero 3 y continua con el bucle hasta llegar al 6
    continue
  print(i)
#Con la declaración "else" podemos ejecutar un bloque de 
# código una vez cuando la condición ya no sea verdadera:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i ya no es menos que 6")