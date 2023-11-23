import tkinter as tk

def salir():
    raiz.destroy()

raiz =tk.Tk()
raiz.title("Dragons of Ages")
raiz.iconbitmap("logoOjo.ico")
raiz.geometry("960x720")
raiz.resizable(False,False)

barraMenu = tk.Menu(raiz)
raiz.config(menu=barraMenu)
juego = tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Juego",menu=juego)

juego.add_command(label="Sonido")
juego.add_command(label="Vídeo")
juego.add_command(label="Rendimiento")
juego.add_command(label="Salir",command=salir)

dificultad = tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Dificultad",menu=dificultad)

dificultad.add_command(label="Fácil")
dificultad.add_command(label="Media")
dificultad.add_command(label="Difícil")
dificultad.add_command(label="Vikingo")

soporte = tk.Menu(barraMenu,tearoff=0)
barraMenu.add_cascade(label="Soporte",menu=soporte)
soporte.add_command(label="Obtén tu cuenta en DoA")
soporte.add_command(label="Actualizaciones")
soporte.add_command(label="Preguntas frecuentes")
soporte.add_command(label="Contacta con DoA")

fondo = tk.PhotoImage(file="fondoDragon.png")
canvas = tk.Canvas(raiz, width=fondo.width(), height=fondo.height())
canvas.pack()
canvas.create_image(0,0,anchor=tk.NW, image=fondo)

usuario = tk.Label(canvas,text="Usuario",anchor="w",justify="left",width=22,font=("Verdana",10),bg="#B4B2B2")
canvas.create_window(50, 500, anchor=tk.NW, window=usuario)
usuarioEntry = tk.Entry(canvas, width=22,font=("Verdana",10),bg="#E7E9E9")
canvas.create_window(50, 525, anchor=tk.NW, window=usuarioEntry)

password = tk.Label(canvas,text="Contraseña",anchor="w",justify="left",width=22,font=("Verdana",10),bg="#B4B2B2")
canvas.create_window(50, 550, anchor=tk.NW, window=password)
passEntry = tk.Entry(canvas, show="*", width=22,font=("Verdana",10),bg="#E7E9E9")
canvas.create_window(50, 575, anchor=tk.NW, window=passEntry)

botonJugar = tk.Button(canvas,text="JUGAR",width=9,height=1,font=("Verdana",20,"bold"),bg="#F60905")
canvas.create_window(50, 600, anchor=tk.NW, window=botonJugar)

daltonismo = tk.Checkbutton (canvas,text="Habilitar modo daltonismo",width=22,font=("Verdana",10),bg="#B4B2B2")
canvas.create_window(50, 665, anchor=tk.NW, window=daltonismo)

version = tk.Label(canvas,text="Versión DoA 1.0.0 alpha",fg="white",width=22,font=("Verdana",10),bg="#141312")
canvas.create_window(700, 665, anchor=tk.NW, window=version)

raiz.mainloop()