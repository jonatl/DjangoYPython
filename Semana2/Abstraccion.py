import pymysql
class Personaje:
    def __init__(self):
        self.hay=False
        self.conexion=pymysql.connect(host='127.0.0.1',
                                                port=3306,
                                                user='admin',
                                                password='Jonatl18',
                                                db='personajes')
        self.cursor=self.conexion.cursor()
        print("Conexion exitosa a:",self.conexion.db)

class Agregarpersonaje():
    def InsertPersonaje(self):
        self.hay=True
        idinv=int(input("Dale un ID al invocador: "))
        nombre=input("Ingresa el nombre del invodador: ")
        nivel=int(input("Ingresa el nivel del invocador: "))
        vida=int(input("Ingresa la vida del invocador: "))
        resistencia=int(input("Ingresa la resistencia que tiene: "))
        fuerza=int(input("Ingresa la fuerza que tiene: "))
        daño=int(input("Ingresa el daño que hace: "))
        tipo=str(input("Ingresa el tipo de personaje si Mago o Guerrero: "))
        opzi=["S","s"]

        opcionitem=input("Deseas agregarle algun item al personaje? \n [S] para agregar item: ")
        
        sql=("INSERT INTO `invocador` (`id`, `nombre`, `nivel`, `vida`, `resistencia`, `fuerza`, `daño`, `tipo`) VALUES (%s,%s, %s, %s, %s,%s,%s,%s)")
        val=(int(idinv),str(nombre),int(nivel),int(vida),int(resistencia),int(fuerza),int(daño),str(tipo))
        try:
            self.cursor.execute(sql,val)
            self.cursor.fetchone()
            self.conexion.commit()
            print(self.cursor.rowcount,f" Invocador {nombre} registrado con ID {idinv}")
            print()
            if opcionitem in opzi:
                nombreitem=input("ingresa el item")
                cantidad=input("Cuantos le agregaras? limite 6: ")
                sqlitem=("INSERT INTO `inventario` (`id`, `cantidad`, `nombre`) VALUES (%s,%s,%s);")
                sqlval=(int(idinv),int(cantidad),str(nombreitem))
                try:
                    self.cursor.execute(sqlitem,sqlval)
                    self.cursor.fetchone()
                    self.conexion.commit()
                    print(self.cursor.rowcount ,f"item agregado al personaje {nombre} con ID: {idinv}")
                    print()
                except TypeError as err:
                    print(err)   
            else:
                print("No se le agregó item")
        except TypeError as err:
            print(err) 
            
class AgregaItem:
    def AgregarItem(self):
        if self.hay==True:
            idforaneo=input("ID del invocador que quieras agregarle item: ")
            nombreitem=input("ingresa el nombre del item: ")
            cantidad=input("Cuantos le agregaras? limite 6: ")
            sqlitem=("INSERT INTO `inventario` (`id`, `cantidad`, `nombre`) VALUES (%s, %s,%s);")
            sqlval=(int(idforaneo),int(cantidad),str(nombreitem))
            try:
                self.cursor.execute(sqlitem,sqlval)
                self.cursor.fetchone()
                self.conexion.commit()
                print(self.cursor.rowcount ,f"item agregado al personaje con ID: {idforaneo}")
                print()
            except TypeError as err:
                print(err)  
                print("no se agrego item ya que la cantidad supera lo permitido") 
        else:
            print("No hay invocador para agregar item")

class MostrarTodosLosPersonajesQueHayEnPartida:
    def MostrarPersonajes(self):
        sql=('SELECT * from invocador;')
        try:
            self.cursor.execute(sql)
            Cus=self.cursor.fetchall()
            for c in Cus:
                print(c)
                print()
        except:
            print("No se encontró ningun invocador")

class MostrarPersonajesYSuInventario:
    def MuestraInventario(self):
        sql=('SELECT * from invocador as i INNER JOIN inventario as inv on i.id=inv.id')
        try:
            self.cursor.execute(sql)
            Mos=self.cursor.fetchall()
            print("LISTA DE INVENTARIO")
            print(" ID| Nombre|Nivel| Vida| Resist| Fuerza| Daño|Tipo|can|Nombre item")
            for m in Mos:
                print("[",m,"]")
            #print("ID ",Mos[0][0]," Nombre: ",Mos[0][1])
        except:
            print("no hay invocador ")

class ComenzarDeCero:
    def BorrarTodosLosDatos(self):
        sql=('DELETE FROM `inventario`;')
        sql2=('DELETE FROM `invocador`;')
        try:
            self.cursor.execute(sql)
            self.cursor.fetchone()
            self.conexion.commit()
            print(self.cursor.rowcount ,"datos eliminado de las tablas")
            print()
        except ValueError as err:
            print("Hubo un error al tratar de eliminar el registro "+err)
        try:
            self.cursor.execute(sql2)
            self.cursor.fetchone()
            self.conexion.commit()
            print(self.cursor.rowcount ,"datos eliminado de la tabla invocadores")
            print()
        except ValueError as err:
            print("Hubo un error al tratar de eliminar el registro "+err)

class Contador():
    def SumaMagos(self):
        sqlcont=("SELECT COUNT(id) AS Numero_De_Magos FROM invocador WHERE `tipo` LIKE 'Mago'")
        try:
            self.cursor.execute(sqlcont)
            Cont=self.cursor.fetchone()
            for c in Cont:
                print(f"hay: {c} Magos")
        except ValueError as err:
            print("Hay 0 magos "+err)

class ContadorGuerreros():
    def SumGuereros(self):
        sqlcont=("SELECT COUNT(id) AS Numero_De_Magos FROM invocador WHERE `tipo` LIKE 'Guerrero'")
        try:
            self.cursor.execute(sqlcont)
            Cont=self.cursor.fetchone()
            for c in Cont:
                print(f"hay: {c} Guerreros")
        except ValueError as err:
            print("Hay 0 Guerreros "+err)

class uno_vs_un():
    def pelea(self):
        if self.hay==True:
            p1=int(input("Selecciona el peleador con su ID"))
            p2=int(input("Selecciona el contrincande con su ID"))
            print(p1," Vs ",p2)
            sql=(f"select * FROM `invocador` where id={str(p1)};")
            sql2=(f"select * FROM `invocador` where id={str(p2)};")
            try:
                self.cursor.execute(sql)
                player1=self.cursor.fetchone()
                print(f"Seleccionaste: {player1} ")
            except ValueError as err:
                print("nope")
            try:
                self.cursor.execute(sql2)
                player2=self.cursor.fetchone()
                print(f"Seleccionaste: {player2} ")
            except ValueError as err:
                print("nope")
            fight=(player1," Vs ",player2)
            print(fight)
        else:
            print("No hay peleadores suficientes")

class game(Personaje):
    def Menu(self):
        continuar=True
        while(continuar):
            opcioncorrecta=False
            while opcioncorrecta!=True:
                print("===== MENU PRINCIPAL ====")
                print(" 1) Mostrar si está conectada la base \n 2) Mostrar todos los  invocadores ingresados"
                      " \n 3) Mostrar inventario de los personajes \n 4) Insertar invocador \n 5) Agregar Item"
                       " \n 6) Contador guerreros \n 7) Contador Magos \n 8) PELEEEAAAAAAA \n 9) Reanudar")
                opci=int(input("Opcion "))
                if opci < 1 or opci > 9:
                    print("No es opcion valida, intenta de nuevo...")
                elif opci==1:
                    Personaje()
                elif opci==2:
                    MostrarTodosLosPersonajesQueHayEnPartida.MostrarPersonajes(self)
                elif opci==3:
                    MostrarPersonajesYSuInventario.MuestraInventario(self)
                elif opci==4:
                    Agregarpersonaje.InsertPersonaje(self)
                elif opci==5:    
                    AgregaItem.AgregarItem(self)
                elif opci==6:
                    ContadorGuerreros.SumGuereros(self)
                elif opci==7:
                    Contador.SumaMagos(self)
                elif opci==8:
                    uno_vs_un.pelea(self)
                elif opci==9:
                    ComenzarDeCero.BorrarTodosLosDatos(self)
                    continuar=False
                    print("Saliendo...")
                    break
                else:
                    opcioncorrecta=True
databas=game()
databas.Menu()