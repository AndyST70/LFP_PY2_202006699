
from Token import constructor
from prettytable import PrettyTable
from lectorcvs import ImportarCSV
from tkinter import messagebox
import os
class AnalizadorSintactico:
    def __init__(self, tokens: list) -> None:
        self.errores = []
        self.tokens = tokens
        self.i= 0
        ruta = os.path.dirname(os.path.abspath(__file__)) + "\\archivos\\LaLigaBot-LFP.csv"
        self.csv = ImportarCSV(ruta)
    def limpieza(self):
        self.tokens = []
    def agregarError(self, entrada, pila, columna, fila):
        self.errores.append("Error sintactico: se obtuvo {} se esperaba {} columna {} fila {}".format(entrada, pila, columna, fila))
    def sacarToken(self):
        """Saca nuestro primer token"""
        try: 
            return self.tokens.pop(0)
        except: 
            return None
    #! GET
    def observarToken(self):
        '''Saca el primer token y lo mete en la pila'''
        '''GET'''
        try:
            return self.tokens[0]
        except:
            return None
    def analizar(self):
        '''S hace ref a estados'''
        return self.S()
        

    def S(self):
        return self.INICIO()
        

    def INICIO(self):
        '''Observa el primero y escoge la ruta'''
        
        vartmp: constructor = self.observarToken()
        
        if vartmp is None:
            self.agregarError("TK_result | TK_jorn | TK_temp | TK_gol | TK_tabla | TK_part | TK_top", "sin datos", 1, 1)
        elif vartmp.tipo == "TK_result":
            return self.RESULT()
        elif vartmp.tipo == "TK_jorn":
            return self.JORNA()
        elif vartmp.tipo == "TK_gol":
            return self.GOL()
        elif vartmp.tipo == "TK_tabla":
            return self.TABLA()
        elif vartmp.tipo == "TK_part":
            return self.PARTIDO()
        elif vartmp.tipo == "TK_top":
            return self.TOP()
        elif vartmp.tipo == "TK_adios":
            return self.ADIOS()
        else: 
            self.agregarError("TK_result | TK_jorn | TK_temp | TK_gol | TK_tabla | TK_part | TK_top", vartmp.tipo, 1, 1)
        
    
            
    def RESULT (self):
        '''RESULTADO equipo VS equipo TEMPORADA <YYYY-YYYY>'''
        #? se espera reservada -- TK_result
        e1 = None
        e2 = None
        año = None
        año1 = None
        token = self.sacarToken()
        if token.tipo == "TK_result":
            i =+ len(token.descripcion)
            token = self.sacarToken()
            
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("tk_cadena", "sin datos", i, 1)
                return
            #!Sacar otro toke -- Se espera cadena
            elif token.tipo == "tk_cadena":
                e1 = token.descripcion
                i =+ len(token.descripcion)
                token = self.sacarToken()
                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("TK_vs", "sin datos", i, 1)
                    return
                    
                #! Sacar otro tokens -- Se espera VS
                elif token.tipo == "TK_vs":
                    i =+ len(token.descripcion)
                    token = self.sacarToken()    
                    if token is None:
                        i =+ len(token.descripcion)
                        self.agregarError("tk_cadena", "sin datos", i, 1)
                        return
                    #! Sacar otro tokens -- Se espera cadena
                    elif token.tipo == "tk_cadena":
                        e2 = token.descripcion
                        i =+ len(token.descripcion)
                        token = self.sacarToken()    
                        if token is None:
                            i =+ len(token.descripcion)
                            self.agregarError("TK_temp", "sin datos", i, 1)

                        #! Sacar otro tokens -- Se espera Temporada
                        elif token.tipo == "TK_temp":
                            i =+ len(token.descripcion)
                            token = self.sacarToken()    
                            if token is None:
                                i =+ len(token.descripcion)
                                self.agregarError("tk_smen", "sin datos", i, 1)
                                return

                            #! Sacar otro tokens -- Se espera tk_smen
                            elif token.tipo == "tk_smen":
                                i =+ len(token.descripcion)
                                token = self.sacarToken()    
                                if token is None:
                                    i =+ len(token.descripcion)
                                    self.agregarError("tk_año", "sin datos", i, 1)
                                    return
                                #! Sacar otro tokens -- Se espera tk_año
                                elif token.tipo == "tk_año":
                                    año = token.descripcion
                                    i =+ len(token.descripcion)
                                    token = self.sacarToken()    
                                    if token is None:
                                        i =+ len(token.descripcion)
                                        self.agregarError("tk_s", "sin datos", i, 1)
                                        return
                                    #! Sacar otro tokens -- Se espera tk_año
                                    elif token.tipo == "tk_s":
                                        i =+ len(token.descripcion)
                                        token = self.sacarToken()    
                                        if token is None:
                                            i =+ len(token.descripcion)
                                            self.agregarError("tk_año", "sin datos", i, 1)
                                            return
                                        #! Sacar otro tokens -- Se espera tk_año
                                        elif token.tipo == "tk_año":
                                            año1 = token.descripcion
                                            i =+ len(token.descripcion)
                                            token = self.sacarToken()    
                                            if token is None:
                                                i =+ len(token.descripcion)
                                                self.agregarError("tk_smay", "sin datos", i, 1)
                                                return
                                            #! Sacar otro tokens -- Se espera tk_año
                                            elif token.tipo == "tk_smay":   
                                                i =+ len(token.descripcion)
                                                print ("Se ingreso correctamente")    
                                                datos_resultados = self.csv.resultado_partido(e1, e2, año, año1)
                                                print(datos_resultados)
                                                return "El resultado de este partido fue: {0} {1} - {2} {3}".format(e1, datos_resultados[0][3], e2, datos_resultados[0][4])
                                            else:
                                                i =+ len(token.descripcion)
                                                self.agregarError("token incorrecto", "falto signo mayor", i, 1)
                                        else: 
                                            i =+ len(token.descripcion)
                                            self.agregarError("token incorrecto", "Falto año: se esperaba 4 digitos", i, 1)
                                    else: 
                                        i =+ len(token.descripcion)
                                        self.agregarError("token incorrecto", "Falto guion",i, 1)
                                else: 
                                    i =+ len(token.descripcion)
                                    self.agregarError("token incorrecto", "Falto año",i, 1)
                            else: 
                                i =+ len(token.descripcion)
                                self.agregarError("token incorrecto", "Falto signo menor",i, 1)
                        else: 
                            i =+ len(token.descripcion)
                            self.agregarError("token incorrecto", "Falto TEMPORADA",i, 1)
                    else: 
                        i =+ len(token.descripcion)
                        self.agregarError("token incorrecto", "Falto cadena",i, 1)
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("token incorrecto", "Falto VS",i, 1)
            else: 
                i =+ len(token.descripcion)
                self.agregarError("token incorrecto", "Falto cadena",i, 1)
        else: 
            i =+ len(token.descripcion)
            self.agregarError("token incorrecto", "RESULTADO",i, 1)
    #* <INS>::= tkb tk_id | ε
    def INS(self):
        token = self.observarToken()
        #se esperaba una bandera | vacio 
        if token is None:
            return None

        else: 
            token = self.sacarToken()
            
            #! esperamos token tkb 
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("tkb", "Se esperaba -f", i, 1 )
                return 
            elif token.tipo == "tkb":
                
                i =+ len(token.descripcion)
                token = self.sacarToken()    
                
                #! esperamos token tk_id 
                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("tk_id", "sin datos", i,1)
                    
                elif token.tipo == "tk_id": 
                    nombre = token.descripcion
                    i =+ len(token.descripcion)
                    print("todo bien", token.descripcion)
                    return nombre
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("tkb", "Se esperaba -f", i, 1)
            else:
                # self.agregarError("tkb", "Se esperaba -f")
                return None                 
    def JORNA (self):
        '''JORNADA número TEMPORADA <YYYY-YYYY> [ -f archivo ]'''
        numero= None
        año1  = None
        año2 = None
        global nombre
        nombre = None
        #? se espera reservada -- TK_jorn
        token = self.sacarToken()
        if token.tipo == "TK_jorn":
            i =+ len(token.descripcion)
            token = self.sacarToken()
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("TK_num", "sin datos",i, 1)
                return
            
            #!Sacar otro toke -- Se espera numero
            elif token.tipo == "tk_num":
                
                numero:int = token.descripcion
                i =+ len(token.descripcion)
                token = self.sacarToken()
                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("TK_temp", "sin datos", i,1)
                    return
                #!Sacar otro toke -- Se espera TEMPORADA
                elif token.tipo == "TK_temp":
                    i =+ len(token.descripcion)
                    token = self.sacarToken()
                    if token is None:
                        i =+ len(token.descripcion)
                        self.agregarError("tk_smen", "sin datos", i,1)
                        return
                    #! Sacar otro tokens -- Se espera tk_smen
                    elif token.tipo == "tk_smen":
                        i =+ len(token.descripcion)
                        token = self.sacarToken()    
                        if token is None:
                            i =+ len(token.descripcion)
                            self.agregarError("tk_año", "sin datos", i ,1)
                            return

                        #! Sacar otro tokens -- Se espera tk_año
                        elif token.tipo == "tk_año":
                            año1 = token.descripcion
                            i =+ len(token.descripcion)
                            token = self.sacarToken()    
                            if token is None:
                                i =+ len(token.descripcion)
                                self.agregarError("tk_s", "sin datos", i ,1)
                                return

                            #! Sacar otro tokens -- Se espera guion
                            elif token.tipo == "tk_s":
                                i =+ len(token.descripcion)
                                token = self.sacarToken()    
                                if token is None:
                                    i =+ len(token.descripcion)
                                    self.agregarError("tk_año", "sin datos", i, 1)
                                    return
                                #! Sacar otro tokens -- Se espera tk_año
                                elif token.tipo == "tk_año":
                                    año2 = token.descripcion
                                    i =+ len(token.descripcion)
                                    token = self.sacarToken()    
                                    if token is None:
                                        i =+ len(token.descripcion)
                                        self.agregarError("tk_smay", "sin datos", i, 1)
                                        return

                                    #! Sacar otro tokens -- Se espera tk_año
                                    elif token.tipo == "tk_smay":   
                                        i =+ len(token.descripcion)
                                        print ("Se ingreso correctamente")
                                        # print(numero, año1, año2, nombre)

                                        encontramos_name = self.INS()
                                        if encontramos_name is None:
                                            encontramos_name = "jornada.html"
                                            i =+ len(token.descripcion)
                                            print("Se agrega por defecto: jornada.html")
#? ============================================================================================================
                                               
                                            # datos_resultados = self.csv.resultados_jornada(int(numero), int(año1), int(año2), nombre)
                                           
                                            # print(datos_resultados)
                                            # return "Generando archivo de resultados jornada {0} temporada {1} - {2}".format(int(numero), año1, año2, )
                                        else:
                                            i =+ len(token.descripcion)
                                            print("asignación: ", encontramos_name)
                                        datos_resultados = self.csv.resultados_jornada(int(numero), int(año1), int(año2), encontramos_name)                                           
                                        print(datos_resultados)
                                        return "Generando archivo de resultados jornada {0} temporada {1} - {2}".format(int(numero), año1, año2)

                                    else: 
                                        i =+ len(token.descripcion)
                                        self.agregarError("tk_smay", "Falto signo mayor", i,1)
                                else: 
                                    i =+ len(token.descripcion)
                                    self.agregarError("tk_año", "Falto año", i, 1)
                            else: 
                                i =+ len(token.descripcion)
                                self.agregarError("tk_s", "Falto guion", i,1 )
                        else: 
                            i =+ len(token.descripcion)
                            self.agregarError("tk_año", "Falto año", i, 1)
                    else: 
                        i =+ len(token.descripcion)
                        self.agregarError("tk_smen", "Falto signo <",i ,1)
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("TK_temp", "Falto TEMPORADA",i ,1)
            else: 
                i =+ len(token.descripcion)
                self.agregarError("tk_num", "Se esperaba un digito de 1 o 2  digotos maximo",i ,1)
        else: 
            i =+ len(token.descripcion)
            self.agregarError("TK_jorn", "Falto JORNADA",i ,1)                              
    def GOL (self):
        '''GOLES condición equipo TEMPORADA <YYYY-YYYY>'''
        #? se espera reservada -- TK_gol
        global entr_cond
        entr_cond = None# condicion
        equipo = None
        año1 = None
        año2 = None

        token = self.sacarToken()
        if token.tipo == "TK_gol":
            i =+ len(token.descripcion)
            condicion = self.CONDICION()
            if condicion is None:
                i =+ len(token.descripcion)
                self.agregarError("TK_local | TK_total | TK_visitante", "sin datos", i, 1)
                return
            else: 
                print("condicion es: ", condicion)
                i =+ len(token.descripcion)
                token = self.sacarToken()

                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("tk_cadena", "sin datos", i, 1)
                    return
                elif token.tipo == "tk_cadena":
                    equipo = token.descripcion
                    i =+ len(token.descripcion)
                    token = self.sacarToken()
                    
                    #!Sacar otro toke -- Se espera TEMPORADA
                    if token is None:
                        i =+ len(token.descripcion)
                        self.agregarError("TK_temp", "sin datos", i, 1)
                        return
                    elif token.tipo == "TK_temp":
                        i =+ len(token.descripcion)
                        token = self.sacarToken()
                    
                    #!Sacar otro toke -- Se espera <
                        if token is None:
                            i =+ len(token.descripcion)
                            self.agregarError("tk_smen", "sin datos", i, 1)
                            return
                        elif token.tipo == "tk_smen":
                            i =+ len(token.descripcion)
                            token = self.sacarToken()

                            #!Sacar otro toke -- Se espera año
                            if token is None:
                                i =+ len(token.descripcion)
                                self.agregarError("tk_año", "sin datos", i, 1)
                                return
                            elif token.tipo == "tk_año":
                                año1 = token.descripcion
                                i =+ len(token.descripcion)
                                token = self.sacarToken()
                                
                                
                                #!Sacar otro toke -- Se espera guion (-)
                                if token is None:
                                    i =+ len(token.descripcion)
                                    self.agregarError("tk_s", "sin datos", i,1)
                                    return
                                elif token.tipo == "tk_s":
                                    i =+ len(token.descripcion)
                                    token = self.sacarToken()
                                    #!Sacar otro toke -- Se espera año
                                    if token is None:
                                        i =+ len(token.descripcion)
                                        self.agregarError("tk_año", "sin datos", i, 1)
                                        return
                                    elif token.tipo == "tk_año":
                                        año2 = token.descripcion
                                        i =+ len(token.descripcion)
                                        token = self.sacarToken()
                                        #!Sacar otro toke -- Se espera año
                                        if token is None:
                                            i =+ len(token.descripcion)
                                            self.agregarError("tk_smay", "sin datos", i,1)
                                            return
                                        elif token.tipo == "tk_smay":
                                            i =+ len(token.descripcion)
                                            
                                            
                                            datos_resultados = self.csv.resultados_goles(condicion, equipo, int(año1), int(año2))
                                            print(datos_resultados)
                                            return "Los goles anotados por el {0} en total en la temporada  {1} {2} fueron {3}".format(equipo, año1, año2, datos_resultados)

                                        else: 
                                            i =+ len(token.descripcion)
                                            self.agregarError("tk_smay", "Falto signo mayor >", i, 1)
                                    else: 
                                        i =+ len(token.descripcion)
                                        self.agregarError("tk_año", "Falto año", i,1)
                                else:
                                    i =+ len(token.descripcion) 
                                    self.agregarError("tk_s", "Falto signo guion (-)", i,1)
                            else: 
                                i =+ len(token.descripcion)
                                self.agregarError("tk_año", "Falto año", i, 1)
                        else: 
                            i =+ len(token.descripcion)
                            self.agregarError("tk_smen", "Falto signo <",i,1)
                    else: 
                        i =+ len(token.descripcion)
                        self.agregarError("TK_temp", "Falto signo TEMPORAL",i,1)
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("tk_cadena", "Falto cadena", i,1)
        else: 
            i =+ len(token.descripcion)
            self.agregarError("TK_gol", "Falto GOLES",i,1)
    #*<CONDICION>::=tk_local | tk_visitante | tk_total
    def CONDICION(self):
        token = self.observarToken()
        if token is None:
            return None
        else:
            
            token = self.sacarToken()
            #! esperamos token LOCAL 
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("None", "Se esperaba LOCAL, VISITANTE O TOTAL", i,1 )
                return
            elif token.tipo == "TK_local" or token.tipo == "TK_visitante" or token.tipo == "TK_total":
                i =+ len(token.descripcion)
                entr_cond = token.descripcion
                print("La condicion: ", token.descripcion)
                return entr_cond
            else:
                i =+ len(token.descripcion)
                self.agregarError("condicion", "Se esperaba TOTAL | VISITANTE | LOCAL", i,1)
        
    def TABLA(self):
        '''TABLA condición equipo TEMPORADA <YYYY-YYYY>'''
        #? se espera reservada -- TK_tab
        año1 = None
        año2 = None
        global nombre
        nombre = None
        token = self.sacarToken()
        if token.tipo == "TK_tabla":
            i =+ len(token.descripcion)
            token = self.sacarToken()
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("TK_temp", "sin datos", i, 1)
                return

            #!Sacar otro toke -- Se espera  TEMPORADA   
            elif token.tipo == "TK_temp":
                i =+ len(token.descripcion)
                token = self.sacarToken()
                #!Sacar otro toke -- Se espera cadena
                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("tk_smen", "sin datos",i,1)
                    return
                 #! Sacar otro tokens -- Se espera tk_smen
                elif token.tipo == "tk_smen":
                    i =+ len(token.descripcion)
                    token = self.sacarToken()    
                    #! Sacar otro tokens -- Se espera tk_año
                    if token is None:
                        i =+ len(token.descripcion)
                        self.agregarError("tk_año", "sin datos",i ,1)
                        return
                    elif token.tipo == "tk_año":
                        año1 = token.descripcion
                        i =+ len(token.descripcion)
                        token = self.sacarToken()    
                        #! Sacar otro tokens -- Se espera guion -
                        if token is None:
                            i =+ len(token.descripcion)
                            self.agregarError("tk_s", "sin datos",i,1)
                            return
                        elif token.tipo == "tk_s":
                            i =+ len(token.descripcion)
                            token = self.sacarToken()    
                            #! Sacar otro tokens -- Se espera tk_año
                            if token is None:
                                i =+ len(token.descripcion)
                                self.agregarError("tk_año", "sin datos", i,1)
                                return
                            elif token.tipo == "tk_año":
                                año2 = token.descripcion
                                i =+ len(token.descripcion)
                                token = self.sacarToken()    
                                
                                #! Sacar otro tokens -- Se espera >
                                if token is None:
                                        i =+ len(token.descripcion)
                                        self.agregarError("tk_smay", "sin datos", i,1)
                                        return
                                #! Sacar otro tokens -- Se espera tk_año
                                elif token.tipo == "tk_smay":   
                                    i =+ len(token.descripcion)
                                    print ("Se ingreso correctamente")
                                    encontramos_name = self.INS()
                                    if encontramos_name is None:
                                        i =+ len(token.descripcion)
                                        print("Se agrega por defecto: temporada.html")
                                    else:
                                        i =+ len(token.descripcion)
                                        print("asignación: ", encontramos_name)    
                                    datos_resultados = self.csv.resultados_tabla(int(año1), int(año2), encontramos_name )
                                    print(datos_resultados)
                                    return "Generando archivo de clasificación de temporada {0} - {1} ".format(año1, año2)

                                else: 
                                    i =+ len(token.descripcion)
                                    self.agregarError("tk_smay", "Falto signo mayor",i,1)
                            else: 
                                i =+ len(token.descripcion)
                                self.agregarError("tk_año", "Falto año",i,1)
                        else: 
                            i =+ len(token.descripcion)
                            self.agregarError("tk_s", "Falto guion",i,1)
                    else: 
                        i =+ len(token.descripcion)
                        self.agregarError("tk_año", "Falto año",i,1)
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("tk_smen", "Falto signo <",i,1)
            else: 
                i =+ len(token.descripcion)
                self.agregarError("TK_temp", "Falto TEMPORADA",i,1)
        else: 
            i =+ len(token.descripcion)
            self.agregarError("TK_tabla", "Falto TABLA",i,1)                           
    def PARTIDO(self):
        '''PARTIDOS equipo TEMPORADA <YYYY-YYYY> [ -f archivo ] [ -ji número ]
            [ -jf número ]'''
        #? se espera reservada -- TK_tab
        equipo = None
        año1 = None
        año2 = None
        global nombre
        nombre = None
        global banji
        banji = None
        global banjf
        banjf = None

        token = self.sacarToken()
        if token.tipo == "TK_part":
            token = self.sacarToken()
            i =+ len(token.descripcion)
           
            #!Sacar otro toke -- Se espera  Cadena   
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("tk_cadena", "sin datos",i,1)
                return
            elif token.tipo == "tk_cadena":
                equipo = token.descripcion
                i =+ len(token.descripcion)
                token = self.sacarToken()
                
                #!Sacar otro toke -- Se espera TEMPORAL
                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("TK_temp", "sin datos",i,1)
                    return
                elif token.tipo == "TK_temp":
                    i =+ len(token.descripcion)
                    token = self.sacarToken()
                    
                    #!Sacar otro toke -- Se espera cadena
                    if token is None:
                        i =+ len(token.descripcion)
                        self.agregarError("tk_smen", "sin datos", i,1)
                        return
                    #! Sacar otro tokens -- Se espera tk_smen
                    elif token.tipo == "tk_smen":
                        i =+ len(token.descripcion)
                        token = self.sacarToken()    
                        
                        #! Sacar otro tokens -- Se espera tk_año
                        if token is None:
                            i =+ len(token.descripcion)
                            self.agregarError("tk_año", "sin datos",i,1)

                            return
                        elif token.tipo == "tk_año":
                            año1 = token.descripcion
                            i =+ len(token.descripcion)
                            token = self.sacarToken()    

                            #! Sacar otro tokens -- Se espera guion -
                            if token is None:
                                i =+ len(token.descripcion)
                                self.agregarError("tk_s", "sin datos",i,1)
                                return
                            elif token.tipo == "tk_s":
                                i =+ len(token.descripcion)
                                token = self.sacarToken()    
                                
                                #! Sacar otro tokens -- Se espera tk_año
                                if token is None:
                                    i =+ len(token.descripcion)
                                    self.agregarError("tk_año", "sin datos",i,1)
                                    return
                                elif token.tipo == "tk_año":
                                    año2 = token.descripcion
                                    i =+ len(token.descripcion)
                                    token = self.sacarToken()    
                                    
                                    #! Sacar otro tokens -- Se espera >
                                    if token is None:
                                            i =+ len(token.descripcion)
                                            self.agregarError("tk_smay", "sin datos",i,1)
                                            return
                                    elif token.tipo == "tk_smay":
                                        i =+ len(token.descripcion)
                                        print ("Se ingreso correctamente")
                                        #? se espera -f
                                        encontramos_name = self.INS()
                                        if encontramos_name is None:
                                            i =+ len(token.descripcion)
                                            print("Se agrega por defecto: partidos.html")
                                        else:
                                            i =+ len(token.descripcion)
                                            print("asignación: ", encontramos_name)
                                        #? Se espera ji
                                        encontramos_inicio = self.INS1()
                                        if encontramos_inicio is None:
                                            i =+ len(token.descripcion)
                                            print("Se agrega por defecto: entrada inicial")
                                        else:
                                            i =+ len(token.descripcion)
                                            print("asignación: ", encontramos_inicio)
                                        #? Se espera jf
                                        encontramos_final = self.INS2()
                                        if encontramos_final is None:
                                            i =+ len(token.descripcion)
                                            print("Se agrega por defecto: entrada final")
                                        else:
                                            i =+ len(token.descripcion)
                                            print("asignación: ", encontramos_final)
                                        datos_resultados = self.csv.resultado_equipo(equipo, int(año1), int(año2), encontramos_name   , encontramos_inicio, encontramos_final)
                                        print(datos_resultados)
                                        return "Generando archivo de resultados de temporada {0} - {1} del {2}".format(año1, año2, equipo)
                                        
                                    else: 
                                        i =+ len(token.descripcion)
                                        self.agregarError("tk_smay", "Falto signo mayor >", i, 1)
                                else: 
                                    i =+ len(token.descripcion)
                                    self.agregarError("tk_año", "Falto año", i,1)
                            else:
                                i =+ len(token.descripcion) 
                                self.agregarError("tk_s", "Falto signo guion (-)", i,1)
                        else: 
                            i =+ len(token.descripcion)
                            self.agregarError("tk_año", "Falto año", i, 1)
                    else: 
                        i =+ len(token.descripcion)
                        self.agregarError("tk_smen", "Falto signo <",i,1)
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("TK_temp", "Falto signo TEMPORAL",i,1)
            else: 
                i =+ len(token.descripcion)
                self.agregarError("tk_cadena", "Falto cadena", i,1)
        else: 
            i =+ len(token.descripcion)
            self.agregarError("TK_part", "Falto cadena", i,1)
    def INS1(self):
        token = self.observarToken()
        #se esperaba una bandera | vacio 
        if token is None:
            return None

        else: 
            token = self.sacarToken()
            
            #! esperamos token tkb 
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("tkb1", "Se esperaba -ji", i, 1 )
                return 
            elif token.tipo == "tkb1":
                i =+ len(token.descripcion)
                token = self.sacarToken()    
                
                #! esperamos token tk_id 
                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("tk_num", "sin datos", i,1)
                    
                elif token.tipo == "tk_num":
                    i =+ len(token.descripcion)
                    banji = token.descripcion
                    print("todo bien", token.descripcion)
                    return banji
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("tkb1", "Se esperaba -ji", i, 1)
            else:
                # self.agregarError("tkb", "Se esperaba -f")
                return None                 
    def INS2(self):
        token = self.observarToken()
        #se esperaba una bandera | vacio 
        if token is None:
            return None

        else: 
            token = self.sacarToken()
            
            #! esperamos token tkb 
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("tkb2", "Se esperaba -jf", i, 1 )
                return 
            elif token.tipo == "tkb2":
                i =+ len(token.descripcion)
                token = self.sacarToken()    
                
                #! esperamos token tk_id 
                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("tk_num", "sin datos", i,1)
                    
                elif token.tipo == "tk_num":
                    i =+ len(token.descripcion)
                    banjf = token.descripcion
                    print("todo bien", token.descripcion)
                    return banjf
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("tkb2", "Se esperaba -j2", i, 1)
            else:
                # self.agregarError("tkb", "Se esperaba -f")
                return None                 
    def TOP(self):
        '''TOP condición TEMPORADA <YYYY-YYYY> [ -n número ]'''
        #? se espera reservada -- TK_gol
        global nombre_condicion2
        nombre_condicion2 = None
        año1 = None
        año2 = None
        global bann
        bann = None
        token = self.sacarToken()
        if token.tipo == "TK_top":
            i =+ len(token.descripcion)
            condicion2 = self.CONDICION2()
            if condicion2 is None:
                i =+ len(token.descripcion)
                self.agregarError("TK_sup | TK_inf", "sin datos", i, 1)
                return
            else: 
                print("condicion es: ", condicion2)
                i =+ len(token.descripcion)
                token = self.sacarToken()
                #!Sacar otro toke -- Se espera TEMPORAL
                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("TK_temp", "sin datos",i,1)
                    return
                elif token.tipo == "TK_temp":
                    i =+ len(token.descripcion)
                    token = self.sacarToken()
                    
                    #!Sacar otro toke -- Se espera cadena
                    if token is None:
                        i =+ len(token.descripcion)
                        self.agregarError("tk_smen", "sin datos", i,1)
                        return
                    #! Sacar otro tokens -- Se espera tk_smen
                    elif token.tipo == "tk_smen":
                        i =+ len(token.descripcion)
                        token = self.sacarToken()    
                        
                        #! Sacar otro tokens -- Se espera tk_año
                        if token is None:
                            i =+ len(token.descripcion)
                            self.agregarError("tk_año", "sin datos",i,1)

                            return
                        elif token.tipo == "tk_año":
                            año1 = token.descripcion
                            i =+ len(token.descripcion)
                            token = self.sacarToken()    

                            #! Sacar otro tokens -- Se espera guion -
                            if token is None:
                                i =+ len(token.descripcion)
                                self.agregarError("tk_s", "sin datos",i,1)
                                return
                            elif token.tipo == "tk_s":
                                i =+ len(token.descripcion)
                                token = self.sacarToken()    
                                
                                #! Sacar otro tokens -- Se espera tk_año
                                if token is None:
                                    i =+ len(token.descripcion)
                                    self.agregarError("tk_año", "sin datos",i,1)
                                    return
                                elif token.tipo == "tk_año":
                                    año2 = token.descripcion
                                    i =+ len(token.descripcion)
                                    token = self.sacarToken()    
                                    
                                    #! Sacar otro tokens -- Se espera >
                                    if token is None:
                                            i =+ len(token.descripcion)
                                            self.agregarError("tk_smay", "sin datos",i,1)
                                            return
                                    elif token.tipo == "tk_smay":
                                        i =+ len(token.descripcion)
                                        print ("Se ingreso correctamente")
                                        #? se espera -f
                                        encontramos_name = self.INS3()
                                        if encontramos_name is None:
                                            i =+ len(token.descripcion)
                                            print("Se agrega por defecto: 5 equipos ")
                                        else:
                                            i =+ len(token.descripcion)
                                            print("asignación: ", encontramos_name)
                                        datos_resultados = self.csv.resultado_top(nombre_condicion2, int(año1), int(año2), int(encontramos_name))                                           
                                        print(datos_resultados)
                                        return "El top superior de la temporada {0} - {1} fue: ".format(año1 , año2)

                                    else: 
                                        i =+ len(token.descripcion)
                                        self.agregarError("tk_smay", "Falto signo mayor",i,1)
                                else: 
                                    i =+ len(token.descripcion)
                                    self.agregarError("tk_año", "Falto año",i,1)
                            else: 
                                i =+ len(token.descripcion)
                                self.agregarError("tk_s", "Falto guion",i,1)
                        else: 
                            i =+ len(token.descripcion)
                            self.agregarError("tk_año", "Falto año",i,1)
                    else: 
                        i =+ len(token.descripcion)
                        self.agregarError("tk_smen", "Falto signo <",i,1)
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("TK_temp", "Falto TEMPORADA",i,1)
        else: 
            i =+ len(token.descripcion)
            self.agregarError("TK_top", "Falto TOP",i,1)   
    def INS3(self):
        token = self.observarToken()
        #se esperaba una bandera | vacio 
        if token is None:
            return None

        else: 
            token = self.sacarToken()
            
            #! esperamos token tkb 
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("tkb3", "Se esperaba -n", i, 1 )
                return 
            elif token.tipo == "tkb3":
                i =+ len(token.descripcion)
                token = self.sacarToken()    
                
                #! esperamos token tk_id 
                if token is None:
                    i =+ len(token.descripcion)
                    self.agregarError("tk_num", "sin datos", i,1)

                    
                elif token.tipo == "tk_num":
                    bann = token.descripcion
                    i =+ len(token.descripcion)
                    print("todo bien", token.descripcion)
                    return bann
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("tkb3", "Se esperaba -n", i, 1)
            else:
                # self.agregarError("tkb", "Se esperaba -f")
                return None                 
    def CONDICION2(self):
        token = self.observarToken()
        if token is None:
            return None
        else:
            
            token = self.sacarToken()
            #! esperamos token LOCAL 
            if token is None:
                i =+ len(token.descripcion)
                self.agregarError("None", "Se esperaba SUPERIOR, INFERIOR", i,1 )
                return
            elif token.tipo == "TK_inf" or token.tipo == "TK_sup":
                nombre_condicion2 = token.descripcion
                i =+ len(token.descripcion)
                print("La condicion: ", token.descripcion)
                return nombre_condicion2
            else:
                i =+ len(token.descripcion)
                self.agregarError("condicion", "Se esperaba SUPERIOR | INFERIOR ", i,1)
    def ADIOS(self):
        '''ADIOS'''
        adios = None
        #? se espera reservada -- TK_tab
        token = self.sacarToken()
        if token.tipo == "TK_adios":
            i =+ len(token.descripcion)
            return "ADIOS"
            
        else: 
            i =+ len(token.descripcion)
            self.agregarError("TK_adios", "Falto ADIOS",i,1) 

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion"]
        for error_ in self.errores:
            x.add_row([error_])
        print(x)

    # def imprimirErrores(self):
    #     '''Imprime una tabla con los errores'''
    #     x = PrettyTable()
    #     x.field_names = ["Lexema","linea","columna", "tipo"]
    #     if len(self.errores) > 0:
    #         for error_ in self.errores:
    #             x.add_row([error_.entrada, error_.pila, error_.columna, error_.fila])     
    #         print(x)
    #     else: 
    #         messagebox.showinfo("Advertencia", "Te falta la información")
        
    #     self.Tabla_tokens(x.get_html_string(),"errores")
        
    #     return x.get_html_string()

    
    # def guardar(self, name: str, cadena: str, abrir: bool = True ):  #? es una libreria por defecto, sirve para manejo de rutas
    #     ruta = os.path.dirname(os.path.abspath(__file__))+"\\archivos"
    #     apertura= open("{}\\{}".format(ruta, name), encoding = "utf-8", mode = "w" )
    #     apertura.write(cadena)
    #     apertura.close()
    #     if abrir:
    #         os.system('start {}\\"{}"'.format(ruta, name))#? format = es para incrustar valores desde codigo a cadena
    # def busqueda(self, codigo):
    #     self.Tabla_tokens(codigo)

    # def Tabla_tokens(self, cadena, nombre_tab):
    #     print("su reporte se esta cargando")
    #     print(" cargando.....")
    #     print(" cargando ......")
    #     print("gracias por preferirnos")
    #     # repo = open("Tabla.html", "w")
    #     estilo = '''<!DOCTYPE html>
    #     <html lang="en">
    #         <head>
    #             <title>Entrada {1}</title>
    #             <meta charset="utf-8">
    #         <meta name="viewport" content="width=device-width, initial-scale=1">
    #         <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css">
    #         <script src="https://cdn.jsdelivr.net/npm/jquery@3.6.0/dist/jquery.slim.min.js"></script>
    #         <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
    #         <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/js/bootstrap.bundle.min.js"></script>
    #         </head>
    #     <body>
    #     <div class="container">
    #     <h2>Tabla {1}</h2>  
    #      <table class="table">
    #         <thead class="thead-dark">
    #          {0}
    #     </table>'''.format(cadena, nombre_tab)  #? 1: nombre_tab, 0: cadena
    #     self.guardar("{0}.html".format(nombre_tab), estilo, True)#? colocamos falso para abrir después
    