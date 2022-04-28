from glob import glob
from math import sin
from sre_parse import State
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
from analizadorsintactico import AnalizadorSintactico
lexico = AnalizadorLexico ()
#guardamos nuestros tokens

sintactico = AnalizadorSintactico(1)
def ventana_creacion():
    #!ttk son los componentes
    #? creamo nuestro objeto 
    ventana = tk.Tk()
    #? modificamos el tamaño de la ventana
    ventana.geometry('950x550')
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
    boton_errores = Button(ventana, text = "Reporte de errores", command=errores, width = "20", height="1", bg = "old lace" )
    boton_errores.place(x=790, y =70)
    
    boton_lperrores = Button(ventana, text = "Limpiar log de errores", command= limpiarerr, width = "20", height="1", bg = "old lace" )
    boton_lperrores.place(x=790, y =100)
    
    boton_tokens = Button(ventana, text = "Reporte de tokens", command=tokens, width = "20", height="1", bg = "old lace" )
    boton_tokens.place(x=790, y =130)
    
    boton_lptokens = Button(ventana, text = "Limpiar log de tokens", command=limpiarTok, width = "20", height="1", bg = "old lace" )
    boton_lptokens.place(x=790, y =160)
    #!==================================================================================================================
    #? Manuales de PDF 
    global boton_ManualUsuario
    boton_ManualUsuario = Button(ventana, text = "Manual de usuario", width = "20", height="1", bg = "#FFFFCC")
    boton_ManualUsuario.place(x=790, y =190)
    
    global boton_ManualTecnico
    boton_ManualTecnico = Button(ventana, text = "Manual Técnico", width = "20", height="1", bg = "#FFFFCC")
    boton_ManualTecnico.place(x=790, y =220)
    
    boton_enviar = Button(ventana, text = "enviar", width = "15", command= analizar,  height="1", bg = "#FFFFCC"  )
    boton_enviar.place(x=740, y =500)
    
    boton_reset = Button(ventana, text = "reset", width = "5", command= lmp,  height="1", bg = "#FFFFCC"  )
    boton_reset.place(x=860, y =500)
    
    global caja_texto
    caja_texto = ScrolledText(ventana, width = "85", height= "25")
    
    caja_texto.place(x=40, y = 60)
    global entry
    # Crear caja de texto.
    entry = ttk.Entry(width=110)
    # Posicionarla en la ventana.
    entry.place(x=40, y=500)

    entrada.pack()
    ventana.mainloop()
def lmp ():
    entry.delete(0, END) #?reseteamos nuestra caja
#? entradas de respuesta
def preguntas():
    txt = entry.get() + "\n"
    caja_texto.config(state="normal")
    caja_texto.tag_configure("nombre", justify="right") #! alineamos a la derecha
    caja_texto.insert(INSERT, txt)#! insertamos nuestro texto ingresado en la caja
    #? ojo a partir de aqui se hace la configuración
    caja_texto.tag_add("nombre", "1.0", "end")
    caja_texto.config(state=DISABLED)
    return txt

#? limpieza
def analizar():
   #!traemos nuestros datos para manipulación y realización de tablas 
    preguntas()
    a = entry.get() + " "#("1.0", tk.END #campo de texto o cajita
    # print(len(lexico.ListaTokens))
    #! reseteamos nuestras listas 
    lexico.Analizar(a) #? Analisis Lexico
    guardartokens = lexico.ListaTokens
    copia= guardartokens
    #TODO ANALISIS SINTACTICO
    #!===============================================================
    
    sintactico = AnalizadorSintactico(copia)
    sintactico.analizar()
    sintactico.imprimirErrores()
    sintactico.limpieza()
    
def tokens():
    lexico.imprimirTokens()
def errores():
    lexico.imprimirErrores()

def limpiarTok():
    lexico.limpiaTokens()
def limpiarerr():
    lexico.limpiarerror()

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
#!rutas dinamicas
def rutars(entrada):
    ruta_datos = uso_.path.dirname(uso_.path.abspath(__file__))+ "\\archivos\{}".format(entrada)
    webbrowser.open_new(ruta_datos)
    print(ruta_datos)

def imprimir(entrada):
    
    pass


    # #? creacion de mensajes
if __name__ == '__main__':
    ventana_creacion()
    lexico.Tabla_tokens()
    print(len(lexico.ListaErrores))

    
   
    

#! los manuales actuales son de prueba, no debe usarse por ahora