import sys
from os import system
import funciones as fund



decuento=0
usuarios=[]
#usuarios=[]
opSalir=True

asientos = [[1 , 2 , 3 , 4 , 5 , 6 ],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36],[37,38,39,40,41,42]]

    


while opSalir:
    print("************** Menu ***************")
    print("1.Ver asientos disponibles      ")
    print("2.Comprar asientos              ")
    print("3.Anula vuelo                   ")
    print("4.Modificar datos del pasajero  ")
    print("5.Salir                         ")
    print("*"*45)
    try:
        opcion=int(input("Ingrese la opción que desea: "))
    except:
        print("debe igresar un numero")

    if opcion == 1 :
        fund.verAsientos ()

    if opcion== 2:
        fund.comprarAsientos()

    if opcion == 3:
        fund.anularVuelo()

    if opcion == 4:
        fund.modificarPasajero()



    if opcion == 5:
        opSalir = fund.salir()

    

        
        
