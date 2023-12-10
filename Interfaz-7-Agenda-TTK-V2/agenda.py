import tkinter as tk
from tkinter import Frame, ttk
from tkinter import messagebox

#FUNCION SALIR
def salir():
    raiz.destroy()

#FUNCION AGREGAR
contadorID = 0
def agregar():
    global contadorID
    nombre = nombreVar.get()
    apellidos = apellidosVar.get()
    telefono = telefonoVar.get()
    email = emailVar.get()

    IDcontacto = contadorID
    contadorID +=1
    
    arbol.insert('','end',iid=IDcontacto,text=IDcontacto,values=(nombre,apellidos,telefono,email))
    messagebox.showinfo("Agregar", "Contacto agregado")
    limpiarCampos()

#FUNCION MODIFICAR
def modificar():
    seleccionado = arbol.focus()
    IDcontacto = arbol.selection()[0]
    valorID = arbol.item(IDcontacto)
    valorIID = valorID['text']

    nombre = nombreModVar.get()
    apellidos = apellidosModVar.get()
    telefono = telefonoModVar.get()
    email = emailModVar.get()

    comprobacion = messagebox.askquestion("Modificar", "¿Estás seguro que quieres modificar?")
    if comprobacion == "yes":
        arbol.item(seleccionado,text=valorIID, values=(nombre,apellidos,telefono,email))
        messagebox.showinfo("Modificar", "Contacto modificado")
        limpiarCampos()
    
#FUNCION ELIMINAR  
def eliminar():
    seleccionado = arbol.focus()
    IDcontacto = arbol.selection()[0]
    valorID = arbol.item(IDcontacto)
    valorIID = valorID['text']
    comprobacion = messagebox.askquestion("Eliminar", "¿Estás seguro que quieres eliminar?")
    if comprobacion == "yes":
        arbol.delete(valorIID) 
        messagebox.showinfo("Eliminar", "Contacto eliminado")

#LIMPIAR CAMPOS EN LAS VENTANAS
def limpiarCampos():
    nombreVar.set('')
    apellidosVar.set('')
    telefonoVar.set('')
    emailVar.set('')
    nombreModVar.set('')
    apellidosModVar.set('')
    telefonoModVar.set('')
    emailModVar.set('')
    idModVar.set('')

#VENTANAS EMERGENTES
def abrirVentana(event):
    # Definir las variables como globales, para poder usarlas fuera de la función
    global nombreVar, apellidosVar, telefonoVar, emailVar, idModVar, nombreModVar, apellidosModVar, telefonoModVar, emailModVar
    if opciones.get() == 'Nuevo Contacto':

        ventanaAgregar = tk.Toplevel(raiz)
        ventanaAgregar.config(bg="#21925D")
        ventanaAgregar.title("Agregar nuevo contacto")
        ventanaAgregar.geometry("450x400")

        nombreVar = tk.StringVar()
        apellidosVar = tk.StringVar()
        telefonoVar = tk.StringVar()
        emailVar = tk.StringVar()
        nombreModVar = tk.StringVar()
        apellidosModVar = tk.StringVar()
        telefonoModVar = tk.StringVar()
        emailModVar = tk.StringVar()
        idModVar = tk.StringVar()

        headLabel = ttk.Label(ventanaAgregar,text="Introduce los datos",font=("Arial",12,"bold"),background="#21925D")
        nombreLabel = ttk.Label(ventanaAgregar,text="Introduce el nombre:",anchor='w',width=25,background="#21925D")
        nombreEntry = ttk.Entry(ventanaAgregar,textvariable=nombreVar)
        apellidosLabel = ttk.Label(ventanaAgregar,text="Introduce los apellidos:",anchor='w',width=25,background="#21925D")
        apellidosEntry = ttk.Entry(ventanaAgregar,textvariable=apellidosVar)
        telefonoLabel = ttk.Label(ventanaAgregar,text="Introduce el telefono:",anchor='w',width=25,background="#21925D")
        telefonoEntry = ttk.Entry(ventanaAgregar,textvariable=telefonoVar)
        emailLabel = ttk.Label(ventanaAgregar,text="Introduce el correo:",anchor='w',width=25,background="#21925D")
        emailEntry = ttk.Entry(ventanaAgregar,textvariable=emailVar)
        botonAgregar = ttk.Button(ventanaAgregar,text="Agregar Contacto", command=agregar)

        headLabel.grid(row=0,column=0,columnspan=2,padx=30,pady=30)
        nombreLabel.grid(row=1,column=0,padx=30,pady=10)
        nombreEntry.grid(row=1,column=1,padx=30,pady=10)
        apellidosLabel.grid(row=2,column=0,padx=30,pady=10)
        apellidosEntry.grid(row=2,column=1,padx=30,pady=10)
        telefonoLabel.grid(row=3,column=0,padx=30,pady=10)
        telefonoEntry.grid(row=3,column=1,padx=30,pady=10)
        emailLabel.grid(row=4,column=0,padx=30,pady=10)
        emailEntry.grid(row=4,column=1,padx=30,pady=10)
        botonAgregar.grid(row=5,column=0,columnspan=2,padx=30,pady=30)


    elif opciones.get() == 'Editar Contacto':
        ventanaModificar = tk.Toplevel(raiz)
        ventanaModificar.config(bg="#E7B312")
        ventanaModificar.title("Modificar un contacto")
        ventanaModificar.geometry("500x450")

        headModLabel2 = ttk.Label(ventanaModificar,text="Selecciona el contacto e introduce los datos modificados",font=("Arial",12,"bold"),background="#E7B312")

        nombreModLabel = ttk.Label(ventanaModificar,text="Introduce el nombre:",anchor='w',width=25,background="#E7B312")
        nombreModEntry = ttk.Entry(ventanaModificar,textvariable=nombreModVar)
        apellidosModLabel = ttk.Label(ventanaModificar,text="Introduce los apellidos:",anchor='w',width=25,background="#E7B312")
        apellidosModEntry = ttk.Entry(ventanaModificar,textvariable=apellidosModVar)
        telefonoModLabel = ttk.Label(ventanaModificar,text="Introduce el telefono:",anchor='w',width=25,background="#E7B312")
        telefonoModEntry = ttk.Entry(ventanaModificar,textvariable=telefonoModVar)
        emailModLabel = ttk.Label(ventanaModificar,text="Introduce el correo:",anchor='w',width=25,background="#E7B312")
        emailModEntry = ttk.Entry(ventanaModificar,textvariable=emailModVar)
        botonModificar = ttk.Button(ventanaModificar,text="Modificar Contacto",command=modificar)

        headModLabel2.grid(row=0,column=0,columnspan=2,padx=30,pady=30)
        nombreModLabel.grid(row=1,column=0,padx=30,pady=10)
        nombreModEntry.grid(row=1,column=1,padx=30,pady=10)
        apellidosModLabel.grid(row=2,column=0,padx=30,pady=10)
        apellidosModEntry.grid(row=2,column=1,padx=30,pady=10)
        telefonoModLabel.grid(row=3,column=0,padx=30,pady=10)
        telefonoModEntry.grid(row=3,column=1,padx=30,pady=10)
        emailModLabel.grid(row=4,column=0,padx=30,pady=10)
        emailModEntry.grid(row=4,column=1,padx=30,pady=10)
        botonModificar.grid(row=5,column=0,columnspan=2,padx=30,pady=30)

    elif opciones.get() == 'Eliminar Contacto':
        
        ventanaEliminar = tk.Toplevel(raiz)
        ventanaEliminar.config(bg="#F6381D")
        ventanaEliminar.title("Eliminar un contacto")
        ventanaEliminar.geometry("450x250")
    
        headDelLabel1 = ttk.Label(ventanaEliminar,text="Selecciona el contacto a elminar",background="#F6381D",font=("Arial",12,"bold"))
        BotonEliminar = ttk.Button(ventanaEliminar,text="Eliminar Contacto",command=eliminar, style="Red.TButton")
        headDelLabel1.pack(padx=30,pady=30)
        BotonEliminar.pack(padx=30,pady=30)

#CREAR LA RAIZ
raiz = tk.Tk()
raiz.title("Agenda")
raiz.geometry("900x550")
raiz.config(bg="#219092")

#ESTILOS
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure('TButton',foreground='navy',font=("Arial",10,"bold"))
estilo.configure("Red.TButton", foreground="red",font=("Arial",10,"bold"))
estilo.configure('TLabel',background='#219092',font=("Arial",10,"bold"))

#CREAR LOS FRAMES
frameAgenda = Frame(raiz, width=800, height=400)
frameAgenda.pack(padx=5,pady=5)
frameAcciones = Frame(raiz, width=800, height=100)
frameAcciones.pack(padx=5,pady=5)
frameAcciones.configure(bg='#219092')

#CREAR EL ARBOL DE DATOS EN EL FRAME AGENDA
arbol=ttk.Treeview(frameAgenda,columns=('nombre','apellidos','telefono','email'),height=20)
arbol.heading("#0",text="ID")
arbol.heading("nombre",text="Nombre")
arbol.heading("apellidos",text="Apellidos")
arbol.heading("telefono",text="Telefono")
arbol.heading("email",text="Correo electronico")
arbol.column("#0",width=40)
arbol.pack(padx=10,pady=10)

#CREAR EL GRID EN EL FRAME ACCIONES
etiqueta1 = ttk.Label(frameAcciones,text="Elige una opción: ")
opciones = ttk.Combobox(frameAcciones, values=['Nuevo Contacto','Editar Contacto','Eliminar Contacto'], width=30)
botonSalir = ttk.Button(frameAcciones,text="Salir", command=salir, style="Red.TButton")

etiqueta1.grid(row=0,column=0,padx=80,pady=20)
opciones.grid(row=0,column=1,padx=80,pady=20)
botonSalir.grid(row=0,column=2,padx=80,pady=20)

opciones.bind("<<ComboboxSelected>>", abrirVentana)

raiz.mainloop()