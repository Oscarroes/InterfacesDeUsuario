import sqlite3 as lite
import sys

conexion = lite.connect("agenda.sqlite")

cursor = conexion.cursor()
#ejecutamos una sentencia de consulta:
cursor.execute("SELECT * FROM contactos;")
#pedimos la operación en lenguaje SQl
cursor.execute("UPDATE contactos SET telefono = '634567' WHERE identificador = 1;")

conexion.commit()