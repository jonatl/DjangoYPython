from BDVehiculo import*
class AgregarAuto():
    def InsertVehiculo(self):
        inID=int(input("Ingresa el ID que vas a modificar [SOLO VALORES ENTEROS]: "))
        inMarca=input("Ingresa la marca del auto: ")
        inPlaca=input("Ingresa la placa: ")
        inColor=input("Ingresa el color: ")
        inModelo=int(input("Ingresa el nombre del modelo [SOLO VALORES ENTEROS]: "))
        inKilometraje=float(input("Ingresa el kilometraje del auto [SOLO NUMEROS]: "))
        inVersion=input("Ingresa la Version del auto: ")
        inPrecio=float(input("Ingresa cuanto vale el auto [SOLO NUMEROS]: "))
        sql=("INSERT INTO `Auto` (`ID`, `Marca`, `placa`, `color`, `modelo`, `kilometraje`, `version`, `precio`) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)")
        val=(int(inID),str(inMarca),str(inPlaca),str(inColor),int(inModelo),float(inKilometraje),str(inVersion),float(inPrecio))
        try:
            self.cursor.execute(sql,val)
            self.cursor.fetchone()
            self.conexion.commit()
            print(self.cursor.rowcount ,"dato ingresado")
            print()
        except TypeError as err:
            print(err)