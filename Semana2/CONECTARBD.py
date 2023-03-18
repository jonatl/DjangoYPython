import pymysql
class BaseDeDatos:
    def __init__(self):
        self.conexion=pymysql.connect(host='127.0.0.1',
                                            port=3306,
                                            user='admin',
                                            password='Jonatl18',
                                            db='northwind')
        self.cursor=self.conexion.cursor()
        print("Conexion exitosa a:",self.conexion.db)

    def seleccionarCustomers(self):
        sql=('SELECT id, company, first_name, job_title,mobile_phone,city from customers')
        try:
            self.cursor.execute(sql)
            Cus=self.cursor.fetchall()
            for c in Cus:
                print(c)
                print()
        except:
            print("nope")

    def SeleccionCustomers(self,id):
        sql=('SELECT id, company, first_name, job_title,city from customers where id='+str(id))
        try:
            self.cursor.execute(sql)
            Cus=self.cursor.fetchone()
            print(Cus)
        except ValueError as err:
            print("Hubo un error al tratar de mostrar el registro \n intenta con otro ID: "+err)

    def InsertarCustomers(self):
        inID=(input("Ingresa el ID: "))
        inCompany=input("Ingresa nombre de la compañia: ")
        inNombre=input("Ingresa nombre del cliente: ")
        inTitulo=input("Ingresa el titulo de trabajo: ")
        inCity=input("Ingresa el nombre de la ciudad: ")
        inCountry=input("INgresa la region: ")
        sql=("INSERT INTO `customers` (`id`, `company`, `last_name`, `first_name`, `email_address`, `job_title`, `business_phone`, `home_phone`, `mobile_phone`, `fax_number`, `address`, `city`, `state_province`, `zip_postal_code`, `country_region`, `web_page`, `notes`, `attachments`) VALUES (%s,%s, NULL, %s, NULL,%s, NULL, NULL, NULL, NULL, NULL,%s,NULL, NULL,%s, NULL, NULL, NULL);")
        val=(str(inID),str(inCompany),str(inNombre),str(inTitulo),str(inCity),str(inCountry))
        try:
            self.cursor.execute(sql,val)
            Cus=self.cursor.fetchone()
            self.conexion.commit()
            print(self.cursor.rowcount ,"dato ingresado")
            print()
        except TypeError as err:
            print(err)

    def EliminarCustomers(self,id):
        sql=('DELETE FROM customers where id='+str(id))
        try:
            self.cursor.execute(sql)
            Cus=self.cursor.fetchone()
            self.conexion.commit()
            print(self.cursor.rowcount ,"dato eliminado")
            print()
        except ValueError as err:
            print("Hubo un error al tratar de eliminar el registro \n intenta con otro ID: "+err)

    def ModificarCustomers(self):
        inID=(input("Ingresa el ID: "))
        inCompany=input("Ingresa nombre de la compañia: ")
        inNombre=input("Ingresa nombre del cliente: ")
        inTitulo=input("Ingresa el titulo de trabajo: ")
        inCity=input("Ingresa el nombre de la ciudad: ")
        inCountry=input("INgresa la region: ")
        sql=("UPDATE `customers` SET `company` = '"+str(inCompany)+"', `last_name` = NULL, `first_name` = '"+str(inNombre)+"', `job_title` = '"+str(inTitulo)+"', `business_phone` = NULL, `fax_number` = NULL, `address` = NULL, `city` = '"+str(inCity)+"', `state_province` = NULL, `zip_postal_code` = NULL, `country_region` = '"+str(inCountry)+"' WHERE `customers`.`id` = "+str(inID)+";")
        try:
            self.cursor.execute(sql)
            self.cursor.fetchone()
            self.conexion.commit()
            print(self.cursor.rowcount ,"dato modificado")
            print()
        except TypeError as err:
            print(err)
        print()

    def Menu(self):
        continuar=True
        while(continuar):
            opcioncorrecta=False
            while (not opcioncorrecta):
                print("===== MENU PRINCIPAL ====")
                print(" 1) Mostrar si está conectada la base \n 2) Mostrar todos los registros de la tabla Customers"
                      " \n 3) Mostrar customers con poca info \n 4) Ingresar datos a customers \n 5) Eliminar \n "
                      "6) Modificar customers \n 7) Salir")
                opci=int(input("Opcion "))
                if opci < 1 or opci > 7:
                    print("No es opcion valida, intenta de nuevo...")
                elif opci==1:
                    BaseDeDatos()
                elif opci==2:
                    BaseDeDatos.seleccionarCustomers(self)
                elif opci==3:
                    sel=int(input("Selecciona el ID de quien quieres mostrar"))
                    BaseDeDatos.SeleccionCustomers(self,sel)
                elif opci==4:
                    BaseDeDatos.InsertarCustomers(self)
                elif opci==5:
                    elm=int(input("Ingresa el ID que quieres eliminar"))
                    BaseDeDatos.EliminarCustomers(self,elm) 
                elif opci==6:
                    BaseDeDatos.ModificarCustomers(self)
                elif opci==7:
                    continuar=False
                    print("Saliendo...")
                    break

                else:
                    opcioncorrecta=True                    
databas=BaseDeDatos()
databas.Menu()
#databas.seleccionarCustomers()
#databas.SeleccionCustomers(5)
#databas.InsertarCustomers()
#databas.seleccionarCustomers()
