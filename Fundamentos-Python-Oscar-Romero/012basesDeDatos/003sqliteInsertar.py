import sqlite3 as lite
import sys

conexion = lite.connect("agenda.sqlite")

cursor = conexion.cursor()
#ejecutamos una sentencia de consulta:
cursor.execute("SELECT * FROM contactos;")
#pedimos la operación en lenguaje SQl
cursor.execute("INSERT INTO contactos VALUES(NULL,'Jorge','2222222','jorge@gmail.com');")

conexion.commit()