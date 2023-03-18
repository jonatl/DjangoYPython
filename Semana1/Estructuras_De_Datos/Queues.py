

class cola:
    def __init__(self):
        self.datos=[]
    def cantidad(self):
        return len(self.datos)
    def insertar(self,dato):
        self.datos.insert(0,dato)
    def extraer(self):
        if self.cantidad():
            self.datos.pop()
        else:
            return None
    def primerdato(self):
        if self.cantidad():
            return self.datos[-1]
    def ultimo_dato(self):
        if self.cantidad():
            return self.datos[0]

num=cola()
num.insertar(2)
num.insertar(3)
num.insertar(5)
num.insertar(7)

print(num.primerdato())
print(num.ultimo_dato())
print(num.cantidad())
print()
dato=num.extraer()
print(dato)
print(num.cantidad())