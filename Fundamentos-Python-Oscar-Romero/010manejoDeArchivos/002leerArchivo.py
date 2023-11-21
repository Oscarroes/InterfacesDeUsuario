archivo = open("miArchivo.txt",'r')

#Nos va a leer una línea y deja el cursor al final de la línea
print(archivo.readline())
#Si la vuelves a llamar leerá la siguiente
print(archivo.readline())

#.read() lee todo el archivo
print(archivo.read())
#Leer de la primera línea a la 10
for i in range(0,10):
    print(archivo.readline())