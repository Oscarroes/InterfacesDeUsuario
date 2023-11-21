'''
Programa calculadora
2023 Oscar
v0.1
'''

#Bienvenida al programa
print("Bienvenido al programa calculadora")
nombre = input("Introduce tu nombre:")
print("Hola",nombre,"te doy la bienvenida a la calculadora")
def calculadora():
    #Indicar la operacion:
    print("Elige la operación que quieres realizar" + 
          "\n1.-Suma"+
          "\n2.-Resta"+
          "\n3.-Multiplicación"+
          "\n4.-División"+"")
    operacion = int(input())
    
    if operacion == 1:
        print("La operación que has elegido es suma")
    if operacion == 2:
        print("La operación que has elegido es resta")
    if operacion == 3:
        print("La operación que has elegido es multiplicación")
    if operacion == 4:
        print("La operación que has elegido es dividión")

    #Introducir 2 números:
    numero1=int(input("Ahora introduce el primer operando:"))
    numero2=int(input("Ahora introduce el segundo operando:"))

    #Realizamos la operación:
    if operacion == 1:
        print("El resultado es:",(numero1+numero2))
        print("-----------------------------------------------")
    if operacion == 2:
        print("El resultado es:",(numero1-numero2))
        print("-----------------------------------------------")
    if operacion == 3:
        print("El resultado es:",(numero1*numero2))
        print("-----------------------------------------------")
    if operacion == 4:
        print("El resultado es:",(numero1/numero2))
        print("-----------------------------------------------")
    calculadora()

#Ejecución recursiva:
calculadora()