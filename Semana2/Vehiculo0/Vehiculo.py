#Clase
class Vehiculo:
    #Self nos brinda acceso a los metodos y atributos de la clase
    #la clase main se crea con la siguiente sintaxis para que las sub clases puedan heredarlos
    def __init__(self,marca,placa,color,modelo,kilometraje,version,precio):
        self.marca=marca
        self.placa=placa
        self.color=color
        self.modelo=modelo
        self.kilometraje=kilometraje
        self.version=version
        self.precio=precio

    def mostrar(self):
        print("Marca: {}".format(self.marca)," Placa: {}".format(self.placa)," Color: {}".format(self.color)," Modelo: {}".format(self.modelo)," Kilometraje: {} km/h".format(self.kilometraje)," Version: {}".format(self.version)," Precio: ${}".format(self.precio))    

    def modificar_marca(self,cambio_marca):
        self.marca=cambio_marca
        print("Se cambio la marca a: {}".format(cambio_marca))
    
    def modificar_placa(self,cambio_placa):
        self.placa=cambio_placa
        print("Se modifico la placa a: {}".format(cambio_placa))

    def modificar_color(self, cambiar_color):
        self.color=cambiar_color
        print("Se cambio por el color: {}".format(cambiar_color))

    def modificar_modelo(self,cambio_modelo):
        self.modelo=cambio_modelo
        print("Cambiamos el modelo al: {}".format(cambio_modelo))
        
    def modificarkilometraje(self,nuevo_kilometraje):
        kilometraje=self.kilometraje+nuevo_kilometraje
        print("el nuevo kilometraje es de: {}".format(kilometraje))

    def modificar_version(self,cambiar_version):
        self.version=cambiar_version
        print("Se modifico la version por la version: {}".format(cambiar_version)) 
         
    def modificar_precio(self,cambiar_precio):
        self.precio=cambiar_precio
        print("Se cambio el precio que tenia a: {}".format(cambiar_precio))     

#Agregar objetos=Instanciarlos
camionetaJona=Vehiculo('JAC','AKS-1322','Rojo',2020,10,'LTE',14929)
camionetaJona.mostrar()
camionetaJona.modificar_marca('TOYOTA')
camionetaJona.modificar_placa('ZZZ-GGIZI')
camionetaJona.modificar_color('ELCOLORDETUSOJOS')
camionetaJona.modificar_modelo(2023)
camionetaJona.modificarkilometraje(20)
camionetaJona.modificar_version('BIGHORN')
camionetaJona.modificar_precio(300000)
print("..................")
#Creacion de subclases
class buses(Vehiculo):
    def sillas(self,numerodesillas):
        print("El numero de sillas es: {}".format(numerodesillas))
#Instanciar objetos de la subclase
FloresBorja=buses('MERCEDES','AMLOVER','Blanco con franja roja',1999,130121,'RUTABORJAS',2000)
FloresBorja.mostrar()
FloresBorja.modificarkilometraje(8001)
FloresBorja.sillas(52)
#Subclase 2
class Hibridos(Vehiculo):
    def BolsasDeAire(self,numerodebolsasdeaire):
        print("Numero de bolsas de aire que tiene: {}".format(numerodebolsasdeaire))
Uber=Hibridos('PIRUS','LOV-Is-War','Celeste',2022,41200,'LTE',230000)
Uber.mostrar()
Uber.BolsasDeAire(6)
#..........................................................................
class Motos(Vehiculo):
    def Cilindros(self,numcilindros):
        print("Numeros de cilindros: {}".format(numcilindros))
Motingo=Motos('ITALIKA','K34D-1241','NEGRO Y ROJO',2023,0,'MAX',30000)
Motingo.mostrar()
Motingo.modificar_color('Naranja')

#Decoreitors