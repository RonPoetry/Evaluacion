import sys
from os import system


usuarios=[]
asientos = [[1 , 2 , 3 , 4 , 5 , 6 ],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30],[31,32,33,34,35,36],[37,38,39,40,41,42]]


def verAsientos():
  system("cls")
  print("1. Asientos Disponibles")
  cont = 1
  for i in asientos:
      print("| ",str(i)[1:-1]," |")
      if cont == 5:
          print("|--------------------------|")
          print("|            VIP           |")
          print("|--------------------------|")
      cont += 1    
  print("")    
  input("Presione una tecla para continuar...")
  system("cls")

def comprarAsientos():
    system("cls")
    print("2. Comprar asientos")
    print("**************** Ingresar datos ****************")
    nombre=(input("ingrese el nombre del pasajero   :             \n   "))
    rut=str(input("ingrese el rut del pasajero      :             \n   "))
    telefono=int(input("ingrese el telefono del pasajero :          \n "))
    banco=str(input("ingrese el banco al que pertnece el pasajero : \n "))
    print("*"*45)

    
    eligeMal = True
    while eligeMal:
        print("****************Valor Asientos**************")
        print("1.Asiento normal 1 - 30, valor  $ 78.900  ")
        print("2.Asiento vip   31 - 42, valor  $ 240.000 ")
        print("*"*45)
        try:
            opcValorAciento=int(input("Seleccione un asiento : \n "))   

            if opcValorAciento < 1 or opcValorAciento > 42:
                print("El asiento seleccionado no es valido") 
            else:
                eligeMal = False

        except:
            print("Debe ingresar un numero valido")    
    
    existe = False
    precio = 0
    for i in asientos:
       nroAsiento = i
       if opcValorAciento in i:
        existe = True
        index = i.index(opcValorAciento)
        i[index] = 'X'
        if opcValorAciento < 30:
            precio = 78900
        else:
            precio = 240000
        if banco =="bancoduoc" or banco == "BancoDuoc" or banco == "bancoDuoc" or banco == "Bancoduoc":
            print("Aplica Descuento BancoDuoc")
            precio = (precio) - precio * 0.15 
        usuarios.append({"Nombre": nombre, "Rut": rut, "Telefono": telefono, "Banco": banco, "Asiento": opcValorAciento , "Precio": precio})
        break
       
    if existe == False:
        print("El asieno seleccionado no esta disponible")       

    for i in usuarios:
        print(i)
    print("")
    input("Presione una tecla para continuar...")    
    system("cls")

  
def anularVuelo():
    system("cls")
    print("3. Anular vuelo")
    opcAciento=int(input("Seleccione asiento del vuelo a Anular: ")) 
    elemento = {}
    for i in usuarios:
        index = i['Asiento']
        if index == opcAciento:
            elemento = i
    try:
        usuarios.remove(elemento)
    except:
        print("Elemento no existe")   
    contador = 0    
    contadorI =  0
    contadorJ =  1
    contJ =  0
    continuar = True 
    for i in asientos:
       contJ = 0
       for j in i:
           if contadorJ == opcAciento:
               contadorI = contador
               continuar = False
           if continuar == False:
              break     
           contadorJ += 1 
           contJ += 1
          
       contador += 1
       if continuar == False:
            break

    contador = 0
    for i in asientos:
       if contador == contadorI:
        i[contJ] = opcAciento
       contador = contador + 1   
       


    for i in usuarios:
        print(i)
    print("")
    input("Presione enter para continuar...")    
    system("cls")


def modificarPasajero():
    system("cls")
    print("4. Modificar Datos")
    asiento = int(input("Ingrese el asiento: "))
    rut = input("Ingrese el rut: ")
    existeUsuario = False
    for i in usuarios:
        rutUsuario = i['Rut']
        nroAsiento = i['Asiento']
        if rut == rutUsuario and asiento == nroAsiento:
            print("- Datos a Actualizar")
            print("1. Nombre Pasajero")
            print("2. Telefono Pasajero")
            op = int(input("Seleccione una opcion: "))
            if op == 1:
                i['Nombre'] = input("Ingrese un nuevo nombre: ")
            elif op == 2:
                i['Telefono'] = input("Ingrese un nuevo telefono: ")
            else:
                print("opcion invalida")        
            existeUsuario = True

    for i in usuarios:
            print(i)        
        

    if existeUsuario == False:
        print("No existen registros con los datos ingresados.")       

    input("Presione enter para continuar...")    
    system("cls")

def salir():
    print("saliendo.....")
    return False