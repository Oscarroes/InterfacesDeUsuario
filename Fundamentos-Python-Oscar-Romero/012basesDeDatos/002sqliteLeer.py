import sqlite3 as lite
import sys

conexion = lite.connect("agenda.sqlite")

cursor = conexion.cursor()
#ejecutamos una sentencia de consulta:
cursor.execute("SELECT * FROM contactos;")
#esta vez le pedimos a datos que nos traiga todo
datos = cursor.fetchall()
#el \t inserta una tabulación
for i in datos:
    print("nombre:",i[1],"\t telefono:",i[2],"\t email:",i[3])

