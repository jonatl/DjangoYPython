from BDVehiculo import*
class EliminarAuto:
    def DeleteVehiculo(self,ID):
            sql=("DELETE from Auto where id="+str(ID))
            try:
                self.cursor.execute(sql)
                Cus=self.cursor.fetchone()
                self.conexion.commit()
                print(self.cursor.rowcount ,"dato eliminado")
                print()

            except ValueError as err:
                print("Hubo un error al tratar de eliminar el registro \n intenta con otro ID: "+err)
