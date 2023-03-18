from abc import ABC, abstractmethod
class Personaje:
    def __init__(self,nombre):
        self.nombre=nombre
        self.nivel=0
        self.inventario=[]
        self.vida=0
    @abstractmethod
    def atacar(self,objetivo):
        pass
    @abstractmethod
    def getstatus(self):
        print(f"Nombre: {self.nombre}. Nivel: {self.nivel}")

    def subirnivel(self):
        self.nivel+=1
        print(f"Nuevo nivel: {self.nivel}")

    def ver_inventario(self):
        print(f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print(objeto)
    
class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida=1200
        self.suma=1
        self.inteligencia=95
        self.inventario=["- Grimorio nivel 1","- Poción de maná","- Objeto embrujado nivel 1","- Pocion de vida"]
        
    def getstatus(self):
        self.suma+1
        print(f"{self.nombre}. clase mago y hay {self.suma}")
        super().getstatus()
        print()

    def atacar(self, objetivo):
        objetivo.vida-=self.inteligencia*0.6
        print("Atacaste a: ",(objetivo.nombre))
        print(f"La vida actual del objetivo es de {objetivo.vida}")
        print("♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕♕")

    def saludar(self):
        print(f"Saludo de {self.nombre}")

class guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida=1500
        self.inteligencia=90
        self.fuerza=200
        self.sum=1
        self.inventario=["- Espada nivel 1","- Escudo nivel 1","- Poción de vida","- Armadura nivel 1"]
    
    def getstatus(self):
        print(f"{self.nombre}  clase guerrero y hay {self.sum}")
        return super().getstatus()
    
    def Grito(self):
        print(f"El guerrero {self.nombre} se aventó un gritote")
    
    def atacar(self, objetivo):
        print("Atacaste a: ",(objetivo.nombre))
        objetivo.vida-=self.fuerza*0.5
        print(f"La vida actual del objetivo es de {objetivo.vida}")
        print("♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛♛")



guerrero1 = guerrero("Kratos")
Mago1 = Mago("Yuno")

guerrero1.getstatus()
Mago1.getstatus()
Mago1.subirnivel()
Mago1.subirnivel()
guerrero1.Grito()
Mago1.saludar()
Mago1.ver_inventario()
guerrero1.ver_inventario()
Mago1.atacar(guerrero1)
guerrero1.atacar(Mago1)
guerrero1.atacar(Mago1)
guerrero1.atacar(Mago1)
Mago1.atacar(guerrero1)
Mago1.atacar(guerrero1)
Mago2=Mago("Erik")
Mago2.getstatus()
mago3=Mago("PEdro")
mago4=Mago("Alias")