import pymysql
import sys
from AgregarVehiculo import *
from EliminarVehiculo import *
from ModificarVehiculo import *
from MostrarVehiculo import*
class Vehiculo:
    def __init__(self):
        self.conexion=pymysql.connect(host='127.0.0.1',
                                                port=3306,
                                                user='admin',
                                                password='Jonatl18',
                                                db='Vehiculo')
        self.cursor=self.conexion.cursor()
        print("Conexion exitosa a:",self.conexion.db)

class Mennu(Vehiculo):
    def Menu(self):
        continuar=True
        while(continuar):
            opcioncorrecta=False
            while opcioncorrecta!=True:
                print("===== MENU PRINCIPAL ====")
                print(" 1) Mostrar si está conectada la base \n 2) Mostrar todos los registros de la tabla Auto"
                      " \n 3) Mostrar Auto con poca info \n 4) Insertar auto \n 5) Eliminar \n 6) Modificar auto \n "
                      "7) Salir")
                opci=int(input("Opcion "))
                if opci < 1 or opci > 7:
                    print("No es opcion valida, intenta de nuevo...")
                elif opci==1:
                    Vehiculo()
                elif opci==2:
                    MostrarTodo.MostrarTodosLosRegistrosDeLaTablaPropiedades(self)
                elif opci==3:
                    MostrarAlgunasPropiedades.MostrarPropiedadesSinTantoDato(self)
                elif opci==4:
                    AgregarAuto.InsertVehiculo(self)
                elif opci==5:    
                    elim=input("Ingresa el ID del auto que quieras eliminar: ")
                    EliminarAuto.DeleteVehiculo(self,elim) 
                elif opci==6:
                    ModificarAuto.UpdateVehiculo(self)            
                elif opci==7:
                    continuar=False
                    print("Saliendo...")
                    sys.exit()
                else:
                    opcioncorrecta=True
databas=Mennu()
databas.Menu()