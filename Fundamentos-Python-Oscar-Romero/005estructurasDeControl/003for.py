print("Ejemplo básico")
for i in range(5):
	print(i)

print("Ejemplo básico 2")
for i in range(1,10):
	print("Esta es la línea",i)
print("Ya estás fuera del bucle")

	
#------------------------------------------------------
#Ejemplo más complejo, recorrer un srting
valido=False

email1=input("Introduce tu email: ")

for i in range(len(email1)):
	if email1[i]=="@":
		valido=True

if valido==True:
	print("El email es correcto")

else:
	print("El email es incorrecto")