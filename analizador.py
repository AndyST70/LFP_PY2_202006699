from error import Error
from Token import constructor 
from prettytable import PrettyTable
import os
from tkinter import messagebox
class AnalizadorLexico():
    def __init__(self):
        self.ListaTokens = []
        self.ListaErrores = [] 
        self.linea = 1
        self.columna= 0
        self.lexema = "" # strings
        self.estado = 1  #
        self.i = 0 #? con este vamos recorriendo nuestras listas y guardando
        #tipo, lexema, linea y columna
    # while=?
    def agregar_token(self, caracter, tipo, linea, columna ):
        self.ListaTokens.append(constructor(caracter, linea, columna, tipo))
        self.lexema = ""
    def error_append(self, caracter, linea, columna,  tipo):
        self.ListaErrores.append(Error("caracter: ", caracter, "linea: ", linea, "columna: ", columna, "tipo", tipo))
    #!===========================================================
    #? Entrada de excepciones, simbolos, caracteres, opciones, etc
    def Estado0(self, caracter):
        '''Documentación q0'''                   
            # elif estado == 2: 
        if caracter.isalpha():#! is alpha se utiliza para el manejo de cadenas o bien para reconocer caracteres.
            self.lexema += caracter
            self.columna +=1
            self.estado = 1  # l, s, a, d

        elif caracter.isdigit():
            self.lexema += caracter
            self.columna +=1
            self.estado = 2

        elif caracter =="-":
            self.lexema += caracter
            self.columna += 1
            self.estado = 6
        elif caracter == "-":
            self.lexema += caracter
            self.columna += 1
            self.estado = 10
#! --->=============        
        elif caracter == '"':
            self.lexema += caracter

            self.columna +=1
            self.estado = 8  
#! --->=============
        elif caracter == "<":
            self.lexema += caracter
            self.columna += 1
            self.estado = 10

        elif caracter == ">":
            self.lexema += caracter
            self.columna += 1
            self.estado = 10
        

        elif caracter == "\t":
            self.columna +=1

        elif caracter == " ":
            self.columna += 1

        elif caracter == '\n':
            self.linea += 1
            self.columna = 1

        elif caracter == "$":
            pass
        
        elif caracter == '\r':
            pass

        else:
            self.lexema += caracter
              #! nos dara un error
            self.ListaErrores.append(Error(self.lexema, 
            self.linea,
            self.columna,
            "Error Caracter desconocido"
            )) 
    
    #!===========================================================
    #? Estados para ingreso de cadenas, indicadores y reservadas, excepciones de cadenas
    #* Verificado completo
    def Estado1(self, caracter :str):
        '''Estado s1'''

        if caracter.isalpha(): # tipo
            self.lexema += caracter 
            self.columna +=1
            self.estado = 1

        elif caracter.isdigit(): #tipo2
            self.lexema +=caracter
            self.columna += 1    
            self.estado = 1
            
        elif caracter == "_": #tipo_2a
            self.estado = 1
            self.lexema +=caracter
            self.columna += 1    
        
        else:
         #!===================================================
                #? Asignamos nuestras palabras reservadas
                #? formulario, tipo, valor, fondo, nombre
                #? valores, evento
            if self.lexema == "RESULTADO":
                self.agregar_token(self.lexema, "TK_result", self.linea, self.columna)
            elif self.lexema == "VS":
                self.agregar_token(self.lexema, "TK_vs", self.linea, self.columna)
            elif self.lexema == "TEMPORADA":
                self.agregar_token(self.lexema, "TK_temp", self.linea, self.columna)
            elif self.lexema == "JORNADA":
                self.agregar_token(self.lexema, "TK_jorn", self.linea, self.columna)
            elif self.lexema == "GOLES":
                self.agregar_token(self.lexema, "TK_gol", self.linea, self.columna)
            elif self.lexema == "LOCAL":
                self.agregar_token(self.lexema, "TK_local", self.linea, self.columna)
            elif self.lexema == "VISITANTE":
                self.agregar_token(self.lexema, "TK_visitante", self.linea, self.columna)
            elif self.lexema == "TOTAL":
                self.agregar_token(self.lexema, "TK_total", self.linea, self.columna)
            elif self.lexema == "PARTIDOS":
                self.agregar_token(self.lexema, "TK_part", self.linea, self.columna)
            elif self.lexema == "TABLA":
                self.agregar_token(self.lexema, "TK_tabla", self.linea, self.columna)
            elif self.lexema == "TOP":
                self.agregar_token(self.lexema, "TK_top", self.linea, self.columna)
            elif self.lexema == "SUPERIOR":
                self.agregar_token(self.lexema, "TK_sup", self.linea, self.columna)
            elif self.lexema == "INFERIOR":
                self.agregar_token(self.lexema, "TK_inf", self.linea, self.columna)
            elif self.lexema == "ADIOS":
                self.agregar_token(self.lexema, "TK_adios", self.linea, self.columna)
        #!======================================================
            # elif self.lexema == "Nombre" or self.lexema =="Ingrese Nombre" or self.lexema == "Guatemala" or self.lexema == "El salvador" or self.lexema ==" Honduras":
            #     self.agregar_token(self.lexema, "Cadena, seguida de letras minusculas/numeros/espacios ", self.linea, self.columna)
            #     self.estado = 0
            #     self.i -= 1
            elif self.lexema == "archivo" :
                self.agregar_token(self.lexema, "tk_id", self.linea, self.columna)
        #!======================================================
                #?Asignamos nuestras palabras idetinficadores
                #?etiqueta, texto, grupo-radio, grupo-option, boton, EVENTO
            self.estado = 0
            self.i -= 1
    
    #!===========================================================
    #? Estados de digitos enteros
    def Estado2(self, caracter :str):
    #!===========================================================    
        '''Estado s2'''
        if caracter.isdigit():
            self.lexema +=caracter
            self.columna += 1
            self.estado = 3
        else:
            self.agregar_token(self.lexema, "tk_num", self.linea, self.columna)
            self.estado = 0
            self.i -= 1
    
    #!===========================================================
    #? Estados de digitos enteros
    def Estado3 (self, caracter : str):
    #!===========================================================    
        '''Estado s3'''
        if caracter.isdigit():
            self.lexema +=caracter
            self.columna += 1
            self.estado = 4
        else: 
            self.agregar_token(self.lexema, "tk_num", self.linea, self.columna)
            self.estado = 0
            self.i -= 1
    
    #!===========================================================
    #? Estados de digitos enteros
    def Estado4 (self, caracter : str):
    #!===========================================================    
        '''Estado s4'''
        if caracter.isdigit():
            self.lexema +=caracter
            self.columna += 1
            self.estado = 5
        else: 
            self.lexema += caracter
              #! nos dara un error
            self.ListaErrores.append(Error(self.lexema, 
            self.linea,
            self.columna,
            "Error Caracter desconocido"
            )) 

    #!===========================================================
    #? Estados de digitos enteros
    def Estado5 (self, caracter : str):
    #!===========================================================   
        '''Estado s5'''
        if caracter.isdigit():
            self.lexema +=caracter
            self.columna += 1
            self.estado = 5
        else:
            self.agregar_token(self.lexema, "tk_año", self.linea, self.columna)
            self.estado = 0
            self.i -= 1
    #!=========================================================== 
    def Estado6 (self, caracter : str):
    #!===========================================================   
        '''Estado s6'''
        if self.lexema == "jf" or self.lexema == "ji" or self.lexema == "f" or self.lexema == "n":
            self.lexema +=caracter
            self.columna += 1
            self.estado = 7
        # elif caracter.isalpha(): # tipo
        #     self.lexema += caracter 
        #     self.columna +=1
        #     self.estado = 6
        else:
            if self.lexema == "-jf":
                self.agregar_token(self.lexema, "tkb", self.linea, self.columna)
            elif self.lexema == "-ji":
                self.agregar_token(self.lexema, "tkb1", self.linea, self.columna)
            self.estado = 0
            self.columna += 1
            self.i -= 1 
    #!=========================================================== 
    def Estado7 (self, caracter : str):
        '''Estado s7'''
    #!=========================================================== 
        if caracter == "-jf" or caracter == "-ji" or caracter == "-f" or caracter == "-n":
        # if self.lexema in ['-jf', '-ji', '-f', '-n']:   
            self.lexema +=caracter
            self.columna += 1
        else:
            if self.lexema == "-jf":
                self.agregar_token(self.lexema, "tkb", self.linea, self.columna)
            elif self.lexema == "-ji":
                self.agregar_token(self.lexema, "tkb1", self.linea, self.columna)
            elif self.lexema == "-f":
                self.agregar_token(self.lexema, "tkb2", self.linea, self.columna)
            elif self.lexema == "-n":
                self.agregar_token(self.lexema, "tkb3", self.linea, self.columna)
            self.columna+=1
            self.estado = 0
            self.i -= 1        
    #!===========================================================
    #? Estado para creación de cadenas
     #!===========================================================
    #? Estado para creación de cadenas
    def Estado8(self, caracter : str):
        if caracter != "\"": 
            # caracter.isalpha() or caracter == "-" or caracter == " ": #"S-S S5 
            self.lexema += caracter
            self.columna +=1
            self.estado = 8
        else: 
            caracter == "\""
            self.estado = 9
            self.lexema +=caracter
            self.columna += 1     
   
    def Estado9(self, caracter: str):         
        self.agregar_token(self.lexema, "tk_cadena", self.linea, self.columna)
        self.estado = 0
        self.i -= 1
    #!===========================================================
    #? Estado para creación de simbolos
    def Estado10 (self, caracter : str):
        '''estado q4'''
        if caracter == "[" or caracter == "]" or caracter == "<" or caracter == ">" or caracter == "-" : 
            self.lexema += caracter
            self.columna +=1
            self.estado = 10        
        else:
            if self.lexema == "<":
                self.agregar_token(self.lexema, "tk_smen", self.linea, self.columna)
            elif self.lexema == ">":
                self.agregar_token(self.lexema, "tj_smay", self.linea, self.columna)
            elif self.lexema == "-":
                self.agregar_token(self.lexema, "tk_s", self.linea, self.columna)
            self.estado = 0
            self.columna += 1
            self.i -= 1    
  
    #!===========================================================
    #? Estados para creación de decimales

    def Analizar(self, caracter):
        self.linea = 1
        self.columna= 0
        self.lexema = "" # strings
        self.estado = 1  #
        self.i = 0

        while self.i < len(caracter):
            if self.estado == 0:
                self.Estado0(caracter[self.i])
            elif self.estado == 1:
                self.Estado1(caracter[self.i])
            elif self.estado == 2:
                self.Estado2(caracter[self.i])
            elif self.estado == 3:
                self.Estado3(caracter[self.i])
            elif self.estado == 4:
                self.Estado4(caracter[self.i])
            elif self.estado == 5:
                self.Estado5(caracter[self.i])
            elif self.estado == 6:
                self.Estado6(caracter[self.i])
            elif self.estado == 7:
                self.Estado7(caracter[self.i])
            elif self.estado == 8:
                self.Estado8(caracter[self.i])
            elif self.estado == 9:
                self.Estado9(caracter[self.i])
            elif self.estado == 10:
                self.Estado10(caracter[self.i])
            self.i += 1

    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna","tipo"]
        if len(self.ListaTokens) >0:
            for token in self.ListaTokens:
                x.add_row([token.descripcion, token.linea, token.columna,token.tipo])
            print(x)
        else: 
            messagebox.showinfo("Advertencia", "Te falta la información")
        
        self.Tabla_tokens(x.get_html_string(),"tokens")
        return x.get_html_string()

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna", "tipo"]
        if len(self.ListaErrores) > 0:
            for error_ in self.ListaErrores:
                x.add_row([error_.descripcion, error_.linea, error_.columna, error_.tipo])     
            print(x)
        else: 
            messagebox.showinfo("Advertencia", "Te falta la información")
        
        self.Tabla_tokens(x.get_html_string(),"errores")
        
        return x.get_html_string()


    
    
    def limpiaTokens(self):
        self.ListaTokens = []
    def limpiarerror(self):
        self.ListaErrores = []     


    def guardar(self, name: str, cadena: str, abrir: bool = True ):  #? es una libreria por defecto, sirve para manejo de rutas
        ruta = os.path.dirname(os.path.abspath(__file__))+"\\archivos"
        apertura= open("{}\\{}".format(ruta, name), encoding = "utf-8", mode = "w" )
        apertura.write(cadena)
        apertura.close()
        if abrir:
            os.system('start {}\\"{}"'.format(ruta, name))#? format = es para incrustar valores desde codigo a cadena
    def busqueda(self, codigo ):
        self.Analizar(codigo)
        self.Tabla_tokens(codigo)

    def Tabla_tokens(self, cadena, nombre_tab):
        print("su reporte se esta cargando")
        print(" cargando.....")
        print(" cargando ......")
        print("gracias por preferirnos")
        # repo = open("Tabla.html", "w")
        estilo = '''<!DOCTYPE html>
        <html lang="en">
            <head>
                <title>Tabla {1}</title>
                <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
            <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
            </head>
        <body>
        <div class="container">
        <h2>Tabla {1}</h2>  
         <table class="table">
            <thead class="thead-dark">
             {0}
        </table>'''.format(cadena, nombre_tab)  #? 1: nombre_tab, 0: cadena
        self.guardar("{0}.html".format(nombre_tab), estilo, True)#? colocamos falso para abrir después
    

