from BDVehiculo import* 
class MostrarTodo:
    def MostrarTodosLosRegistrosDeLaTablaPropiedades(self):
        sql=('SELECT*from Auto;')
        try:
            self.cursor.execute(sql)
            Cus=self.cursor.fetchall()
            for c in Cus:
                print(c)
                print()
        except:
            print("nope")

class MostrarAlgunasPropiedades:
    def MostrarPropiedadesSinTantoDato(self):
        sql=('select ID,Marca,precio from Auto;')
        try:
            self.cursor.execute(sql)
            Mos=self.cursor.fetchall()
            for m in Mos:
                print(m)
                print()
        except:
            print("no c hizo el guizo")