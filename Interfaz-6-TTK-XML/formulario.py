from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk


raiz = tk.Tk()

archivo = open("interfaz.xml","r")

contenido = archivo.read()
xml = BeautifulSoup(contenido,"xml")

for campo in xml.find_all("campo"):

    tipo = campo.get("tipo")
    texto = campo.get("texto")
    
    if tipo == "entrada":
        ttk.Entry(raiz).pack(padx=5,pady=5)
    elif tipo == "etiqueta":
        ttk.Label(raiz,text=texto).pack(padx=5,pady=5)
    elif tipo == "boton":
        ttk.Button(raiz,text=texto,width=20).pack(padx=10,pady=10)
    elif tipo == "check":
        ttk.Checkbutton(raiz,text=texto).pack(padx=10,pady=10)
    elif tipo == "combo":
        valores = campo.get("valores").split(',')
        ttk.Combobox(raiz,values=valores).pack(padx=10,pady=10)
    elif tipo == "spinbox":
        ttk.Spinbox(raiz,from_=0,to=10).pack(padx=10,pady=10)
    elif tipo == "titulo":
        fuente = ("Arial",16,"bold")
        ttk.Label(raiz,text=texto,font=fuente).pack(padx=20,pady=20)

raiz.mainloop()