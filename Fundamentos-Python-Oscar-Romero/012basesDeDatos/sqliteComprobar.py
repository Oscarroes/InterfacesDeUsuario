#Importamos las librerias de sqlite3 para la base datos
#Importamos sys para usar funcines para conectar con el sistema
import sqlite3 as lite
import sys

#Conectamos con una base de datos llamada agenda, si no existe nos la crea
conexion = lite.connect("agenda.sqlite")

#Establezco un cursor para saber en qué punto de la base de datos voy a trabajar
cursor = conexion.cursor()

#Le pedimos algo a la base de datos en lenguaje SQL
cursor.execute("SELECT SQLITE_VERSION()")
#la variable datos contiene lo que me devuelve la base de datos
datos = cursor.fetchone()
print("La version de SQLite es:",datos)
