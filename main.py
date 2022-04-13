from glob import glob
import tkinter as tk
from tkinter import ttk
import os as uso_
from tkinter import filedialog, Tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from tkinter.filedialog import askopenfile
import sys
from turtle import width
from analizador import AnalizadorLexico
import webbrowser
lexico = AnalizadorLexico ()
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
    #? creacion de boton de reportes
    global boton_errores
    boton_errores = Button(ventana, text = "Reporte de errores", width = "20", height="1", bg = "old lace" )
    boton_errores.place(x=490, y =70)
    
    boton_lperrores = Button(ventana, text = "Limpiar log de errores", width = "20", height="1", bg = "old lace" )
    boton_lperrores.place(x=490, y =100)
    
    boton_tokens = Button(ventana, text = "Reporte de tokens", width = "20", height="1", bg = "old lace" )
    boton_tokens.place(x=490, y =130)
    
    boton_lptokens = Button(ventana, text = "Limpiar log de tokens", width = "20", height="1", bg = "old lace" )
    boton_lptokens.place(x=490, y =160)
    #!==================================================================================================================
    #? Manuales de PDF 
    global boton_ManualUsuario
    boton_ManualUsuario = Button(ventana, text = "Manual de usuario", command = enter_entrada,   width = "20", height="1", bg = "#FFFFCC")
    boton_ManualUsuario.place(x=490, y =190)
    
    global boton_ManualTecnico
    boton_ManualTecnico = Button(ventana, text = "Manual Técnico",command = enter_entrada, width = "20", height="1", bg = "#FFFFCC")
    boton_ManualTecnico.place(x=490, y =220)
    
    
    boton_enviar = Button(ventana, text = "enviar", width = "15", height="1", bg = "#FFFFCC"  )
    boton_enviar.place(x=490, y =500)
    
    global caja_texto
    caja_texto = ScrolledText(ventana, width = "50", height= "25")
    caja_texto.place(x=40, y = 60)

    # Crear caja de texto.
    entry = ttk.Entry(width=70)
    # Posicionarla en la ventana.
    entry.place(x=40, y=500)

    entrada.pack()
    ventana.mainloop()
def analizar():
   #!traemos nuestros datos para manipulación y realización de tablas 
   a = caja_texto.get("1.0", tk.END)
   lexico.iniciar() #! reseteamos nuestras listas 
   lexico.Analizar(a) #? iniciamos nuestros tokens y la formulación de estos
def salir():
    sys.exit()
def abrir():
    Tk().withdraw()
    archivo = filedialog.askopenfile(
        title = "Seleccionar un archivo",
        initialdir = "./",
        filetypes = [
            #Definimos los tipo de archivo
            ("archivos .form", "*.form"),
            ("todos los archivos",  "*.*")
        ]
    )
    #si no se seleccióno ningun archivo
    if archivo is None:
        print('No se selecciono ningun archivo\n')
        return None
    else:
        archivo_2 = open(archivo.name, "r", encoding = "utf-8")
        #Leer el texto
        texto = archivo_2.read()
        archivo_2.close()
        caja_texto.delete("1.0", "end")
        caja_texto.insert(INSERT, texto)
        return texto #retorna nuestro texto
def rutars(entrada):
    ruta_datos = uso_.path.dirname(uso_.path.abspath(__file__))+ "\\archivos\{}".format(entrada)
    webbrowser.open_new(ruta_datos)
    
    print(ruta_datos)


def enter_entrada():
    #!==================================================
    if boton_ManualTecnico.get() == "Reporte de Tokens":
        boton_ManualTecnico.set("")
        if lexico.ListaTokens != None:
           lexico.imprimirTokens()
        else: 
            print("No tenemos información")

    elif combo.get() == "Reporte de errores":
        combo.set("")
        if lexico.ListaErrores != None:
            lexico.imprimirErrores()
        else: 
            print("No tenemos información")
    elif boton_ManualUsuario.get() == "Manual Usuario":
        boton_ManualUsuario.set("")
        rutars("Manual Usuario.pdf")

    elif boton_ManualTecnico.get() == "Manual Tecnico":
        boton_ManualTecnico.set("")
        rutars("Manual Tecnico.pdf")
                    
    # #? creacion de mensajes
if __name__ == '__main__':
    ventana_creacion()
    lexico.Tabla_tokens()
    print(len(lexico.ListaTokens))
    print(len(lexico.ListaErrores))


#! los manuales actuales son de prueba, no debe usarse por ahora