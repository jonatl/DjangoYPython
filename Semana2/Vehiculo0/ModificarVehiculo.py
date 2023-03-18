from BDVehiculo import*
class ModificarAuto:
    def UpdateVehiculo(self):
        inID=int(input("Ingresa el ID que vas a modificar [SOLO VALORES ENTEROS]: "))
        inMarca=input("Ingresa la marca del auto: ")
        inPlaca=input("Ingresa la placa: ")
        inColor=input("Ingresa el color: ")
        inModelo=int(input("Ingresa el nombre del modelo [SOLO VALORES ENTEROS]: "))
        inKilometraje=float(input("Ingresa el kilometraje del auto [SOLO NUMEROS]: "))
        inVersion=input("Ingresa la Version del auto: ")
        inPrecio=float(input("Ingresa cuanto vale el auto [SOLO NUMEROS]: "))
        sql=("UPDATE `Auto` SET `Marca` = '"+str(inMarca)+"',`placa` = '"+str(inPlaca)+"',`color` = '"+str(inColor)+"',`modelo` = '"+str(inModelo)+"', `kilometraje` = '"+str(inKilometraje)+"', `version` = '"+str(inVersion)+"', `precio` = '"+str(inPrecio)+"' WHERE `Auto`.`ID` = "+str(inID)+";")
        print
        try:
            self.cursor.execute(sql)
            self.cursor.fetchone()
            self.conexion.commit()
            print(self.cursor.rowcount ,"dato modificado")
            print()
        except TypeError as err:
            print(err)