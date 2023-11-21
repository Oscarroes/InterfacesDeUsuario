#Son Listas pero inmutables, no se pueden modificar despues de su creación
agenda = ("Juan","Angel","Pepe")
print("La longitud de la tupla es de:",len(agenda))
print(agenda[2])

#Convertir la tupla en una lista:
lista=list(agenda)
print(lista)
print(agenda)