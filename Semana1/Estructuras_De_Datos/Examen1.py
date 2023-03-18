#cada renglon es un cliente con sus datos
#Arreglo multidimencional de n a m
#decalaramos el arreglo con 5 clientes con sus datos
#imprmir clientes
#ingresar o modificar otro cliente 

Contratos=[[1,2,3,4,5,6],                                                    #ID contrato
       ["12/02/22","04/05/22","15/12/22","01/14/22,","30/03/22","14/12/22"], #Fecha inicio
       ["12/02/23","04/05/23","15/12/23","01/14/23,","30/03/23","14/12/23"], #Fecha final
       [1400,1440,5120,12300,5122,6835],                                     #Valor
       [12,14,12,65,78,45],                                                  #Comision
       [1,2,2,1,3,1,1]]                                                        #Pagos
def Ingresar_Contratos(ID_Contratos,FechaInicio,FechaFinal,Valor,Comision,Pagos):
    print(f"Bienvenido {ID_Contratos} {FechaInicio} {FechaFinal} {Valor} {Comision} {Pagos}")

Pagos=[[1,2,3,4,5,6,7,8,9],
       ["01/01/23","04/01/23","02/02/23","11/01/23","02/02/23","03/02/23","16/02/23","19/03/23","14/03/23"],
       [10,20,20,30,30,40,50,50,50,60],
       [100,102,150,140,200,500,120,521,400],
       ["Legal","Activo","En proceso","Activo","En proceso","Activo","Activo","Cerrado"],
       [1400,1440,1440,5120,12300,12300,12300,5122,6835],
       ["Jona","Emmanuel","Emmauel","Angel","Angel","Sofia","MAira","MAira","MAira","Miguel"]]

def Ingresar_Pagos(ID_Pagos,Fecha,ID_Contratos_Pagos,Cantidad,Estado,Valor,Provedor):
    print(f"Bienvenido {ID_Pagos} {Fecha} {ID_Contratos_Pagos} {Cantidad} {Estado} {Valor} {Provedor}")

def Imprimir_Pagos():
    for i in range (len(Pagos)):
        for j in range(len(Pagos[i])):
            print (Pagos[i][j])
def Imprimir_Pagos2():
    print(Pagos[0])
Imprimir_Pagos2()
print("........................")
Imprimir_Pagos2()
#for i in range(len(Pagos)) : 
 #   for j in range(len(Pagos[i])) : 
  #      print(Pagos[i][j], end=" ")
   # print() 