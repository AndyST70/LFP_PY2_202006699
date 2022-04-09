import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, Tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from tkinter.filedialog import askopenfile
from turtle import width
def ventana_creacion():
    #!ttk son los componentes
    #? creamo nuestro objeto 
    ventana = tk.Tk()
    #? modificamos el tamaño de la ventana
    ventana.geometry('650x550')
    #? titulo de la ventana
    ventana.title("Interfaz Gráfica")
    #? configuramos nuestro icono de nuestra app
    ventana.iconbitmap("icono.ico")
    ventana.resizable(0,0) #? evitamos que cambie de tamaño
    ventana.config(background= "#FF9933")



    #========================================================
    entrada = Label(text = "La Liga Bot",  font = ("Cambria", 14), bg= "#FFFFFF", width = "500", height = "2")
    #!           Label
    ventana.rowconfigure(0, weight=1)
    #TODO=================================================================
    #! configuración de nuestro chat
    boton_enviar = Button(ventana, text = "Reporte de errores", width = "20", height="1", bg = "old lace" )
    boton_enviar.place(x=490, y =70)
    
    boton_enviar = Button(ventana, text = "Limpiar log de errores", width = "20", height="1", bg = "old lace" )
    boton_enviar.place(x=490, y =100)
    
    boton_enviar = Button(ventana, text = "Reporte de tokens", width = "20", height="1", bg = "old lace" )
    boton_enviar.place(x=490, y =130)
    
    boton_enviar = Button(ventana, text = "Limpiar log de tokens", width = "20", height="1", bg = "old lace" )
    boton_enviar.place(x=490, y =160)
    
    boton_enviar = Button(ventana, text = "Manual de usuario", width = "20", height="1", bg = "#FFFFCC")
    boton_enviar.place(x=490, y =190)
    
    boton_enviar = Button(ventana, text = "Manual Técnico", width = "20", height="1", bg = "#FFFFCC")
    boton_enviar.place(x=490, y =220)
    
    
    boton_enviar = Button(ventana, text = "enviar", width = "15", height="1", bg = "#FFFFCC"  )
    boton_enviar.place(x=490, y =500)
    

    caja_texto = ScrolledText(ventana, width = "50", height= "25")
    caja_texto.place(x=40, y = 60)

    # Crear caja de texto.
    entry = ttk.Entry(width=70)
    # Posicionarla en la ventana.
    entry.place(x=40, y=500)

    entrada.pack()
    ventana.mainloop()


if __name__ == '__main__':
    ventana_creacion()