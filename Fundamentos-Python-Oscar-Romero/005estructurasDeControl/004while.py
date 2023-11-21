numero = 1
while numero <10:
    numero +=1
    print("Hola")

#Ejemplo algo más complicado:
edad=int(input("Introduce tu edad: "))
while edad<0 or edad>120:
	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
	edad=int(input("Introduce tu edad: "))

print("Tu edad es de: ",str(edad)," años.")