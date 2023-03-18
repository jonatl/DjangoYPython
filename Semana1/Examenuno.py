#Como puedes hacer un reporte que te de el contrato el # de pagos acreditados, 
#el numero de pagos pendientes y calificacion de cliente.
import sys 

Contratos=[[1,"12/02/22","12/02/23",1400,12,1],
           [2,"04/05/22","04/05/23",1440,14,2],
           [3,"15/12/22","15/12/23",5120,65,2],
           [4,"01/14/22","01/14/23,",12300,78,3],
           [5,"01/14/22","30/03/23",5122,45,1],
           [6,"30/03/22","30/03/23",6835,24,1]]

Pagos=[[1,"01/01/23",1,100,"Legal",1400,"Jona"],
       [2,"04/01/23",2,300,"Pendiente",1440,"Maira"],
       [3,"12/02/23",2,500,"Activo",1440,"Maira"],
       [4,"04/01/23",3,2000,"Pagado",5120,"Naye"],
       [5,"02/02/23",3,5000,"Pagado",5120,"Naye"],
       [6,"04/02/23",4,2000,"Pagado",12300,"Oscar"],
       [7,"30/01/23",4,3000,"Pagado",12300,"Oscar"],
       [8,"28/01/23",4,5000,"Pagado",12300,"Oscar"],
       [9,"04/02/23",5,1000,"Pendiente",5122,"Brenda"],
       [10,"24/02/23",4,2000,"Pendiente",6835,"Oscar"]]

ID_CONTRATOS=[Contratos[0][0],Contratos[1][0],Contratos[2][0],Contratos[3][0],
              Contratos[4][0],Contratos[5][0]]

ID_PAGOS=[Pagos[0][0],Pagos[1][0],Pagos[2][0],Pagos[3][0],Pagos[4][0],Pagos[5][0],
              Pagos[6][0],Pagos[7][0],Pagos[8][0],Pagos[9][0]]

def AgregarPagos():
        print("Ingresar_Pagos(ID_Pagos,Fecha,ID_Contratos_Pagos,Cantidad,Estado,Valor,Provedor)")
        d1=int(input("ID_Pagos"))
        d2=int(input("Fecha"))
        d3=int(input("ID_Contratos_Pagos"))
        d4=int(input("Cantidad"))
        d5=int(input("Estado"))
        d6=int(input("Fecha"))
        d7=int(input("Valor"))
        d8=int(input("Provedor"))
        if d3 in (ID_CONTRATOS):    
            Pagos.append([d1,d2,d3,d4,d5,d6,d7,d8])
        else:
            print("No se registró pago ya que no existe el ID_CONTRATO ")
            print()
def ModificarPagos():
        opc=int("Cual contrato vas a modificar? ")     
        if opc in ID_PAGOS:
            d1=int(input("ID_Pagos"))
            d2=(input("Fecha"))
            d3=int(input("ID_Contratos_Pagos"))
            d4=int(input("Cantidad"))
            d5=(input("Estado"))
            d6=(input("Fecha"))
            d7=int(input("Valor"))
            d8=(input("Provedor"))
            Pagos[opc]=[[d1,d2,d3,d4,d5,d6,d7,d8]]
            print()
        else:
            print("No se modificó pago ya que no existe el ID_PAGO ")
            print()
def MostrarContratosPagados():
    newlist = []
    int=0
    for x in Pagos:
       if "Pagado" in x:
          int=int+1
          newlist.append(x)
    print(newlist)
    print(int," Contratos pagados")
    print()

def MostrarTodosLosPagos ():
    for x in range (len(Pagos)):
        print(x,Pagos[x])

def EliminarPagos():
    opc=int(input("Selecciona la opcion que quieres eliminar: "))
    if opc in ID_PAGOS:
        Pagos[opc]="CONTRATO CERRADO"
        print("Eliminaste el pago: ")
        print()
    else:
        print("No se puede eliminar algo que no existe")

def loop():
    try:

        while True:
            print("Acciones que puedes realizar \n 1) Agregar \n 2) Mostrar todos los pagos \n 3) Eliminar pagos \n 4) Mostrar contratos pagados\n 5) Salir")
            activ=(1,2,3,4,5)
            opmain=int(input("Selecciona la opcion: "))
            while opmain in activ:
                if opmain==1:
                    AgregarPagos() 
                    break
                elif opmain==2:
                    MostrarTodosLosPagos() 
                    break
                elif opmain==3:
                    EliminarPagos()  
                    break
                elif opmain==4:
                    MostrarContratosPagados() 
                    break
                elif opmain==5:
                    print("Saliendo")
                    sys.exit()
                
    except Exception as err:
        print(err)
        return opmain
    
loop()