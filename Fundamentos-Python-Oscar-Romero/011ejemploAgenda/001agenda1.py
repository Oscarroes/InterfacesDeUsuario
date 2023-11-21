#Programa Agenda1:

agenda = [["nombre","telefono","email"]]
archivo = open("agenda1.txt",'a')
archivo.close()
#Cargamos los registros que tenemos guardados en el archivo txt:
archivo = open("agenda1.txt",'r')
for i in range(1,10):
    nuevalinea =archivo.read().split(",")
    agenda.append(nuevalinea)

#Imprimimos el estado previo de la agenda:
print(agenda)

def miAgenda():
    #Menu inicial:
    print("Escoge una opción:")
    print("1.- Introduce un nuevo registro")
    print("2.- Lista los registros")

    opcion = int(input())
    if opcion == 1:
        nombre = input("Introduce el nuevo nombre en la agenda: ")
        telefono = input("Introduce el nuevo telefono: ")
        correo = input("Introduce el nuevo correo: ")
        print("-------------------------------")
        #Metemos la info en la lista:
        agenda.append([nombre,telefono,correo])
        #sacamos la lista por pantalla:
        print(agenda)
        #Guardamos la info en archivo:
        archivo = open("agenda1.txt",'a')
        cadena = nombre + "," + telefono + "," + correo + "\n"
        archivo.write(str(cadena))
        archivo.close()
    elif opcion == 2:
        for i in range(1,len(agenda)):
            print(agenda[i])

    #Ejecución recursiva:
    miAgenda()

miAgenda()