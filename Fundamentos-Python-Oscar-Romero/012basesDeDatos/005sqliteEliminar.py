import sqlite3 as lite
import sys

conexion = lite.connect("agenda.sqlite")

cursor = conexion.cursor()
#ejecutamos una sentencia de consulta:
cursor.execute("SELECT * FROM contactos;")
#pedimos la operación en lenguaje SQl
#Esto vaciaría la tabla entera: cursor.execute("DELETE * FROM contactos;")
cursor.execute("DELETE FROM contactos WHERE identificador =2;")

conexion.commit()