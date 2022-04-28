from lib2to3.pgen2 import token
from pickle import NONE
from tokenize import Token
from Token import constructor
from prettytable import PrettyTable

class AnalizadorSintactico:
    def __init__(self, tokens: list) -> None:
        self.errores = []
        self.tokens = tokens
        self.i= 0
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
        self.S()

    def S(self):
        self.INICIO()

    def INICIO(self):
        '''Observa el primero y escoge la ruta'''
        
        vartmp: constructor = self.observarToken()
        
        if vartmp is None:
            self.agregarError("TK_result | TK_jorn | TK_temp | TK_gol | TK_tabla | TK_part | TK_top", "sin datos")
        elif vartmp.tipo == "TK_result":
            self.RESULT()
        elif vartmp.tipo == "TK_jorn":
            self.JORNA()
        elif vartmp.tipo == "TK_gol":
            self.GOL()
        elif vartmp.tipo == "TK_tabla":
            self.TABLA()
        elif vartmp.tipo == "TK_part":
            self.PARTIDO()
        elif vartmp.tipo == "TK_top":
            self.TOP()
        elif vartmp.tipo == "TK_adios":
            self.ADIOS()
        else: 
            self.agregarError("TK_result | TK_jorn | TK_temp | TK_gol | TK_tabla | TK_part | TK_top", vartmp.tipo)
        
    
            
    def RESULT (self):
        '''RESULTADO equipo VS equipo TEMPORADA <YYYY-YYYY>'''
        #? se espera reservada -- TK_result
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
                                            i =+ len(token.descripcion)
                                            token = self.sacarToken()    
                                            if token is None:
                                                i =+ len(token.descripcion)
                                                self.agregarError("tk_smay", "sin datos", i, 1)
                                                return
                                            #! Sacar otro tokens -- Se espera tk_año
                                            elif token.tipo == "tk_smay":   
                                                i =+ len(token.descripcion)
                                                print ("correcto manito wuu")    
                                                
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
                    i =+ len(token.descripcion)
                    print("todo bien", token.descripcion)
                    return token.descripcion
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
        name = None
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
                                    i =+ len(token.descripcion)
                                    token = self.sacarToken()    
                                    if token is None:
                                        i =+ len(token.descripcion)
                                        self.agregarError("tk_smay", "sin datos", i, 1)
                                        return

                                    #! Sacar otro tokens -- Se espera tk_año
                                    elif token.tipo == "tk_smay":   
                                        i =+ len(token.descripcion)
                                        print ("correcto manito wuu")
                                        encontramos_name = self.INS()
                                        if encontramos_name is None:
                                            i =+ len(token.descripcion)
                                            print("Se agrega por defecto: jornada.html")
                                        else:
                                            i =+ len(token.descripcion)
                                            print("asignación: ", encontramos_name)
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
                                        i =+ len(token.descripcion)
                                        token = self.sacarToken()
                                        #!Sacar otro toke -- Se espera año
                                        if token is None:
                                            i =+ len(token.descripcion)
                                            self.agregarError("tk_smay", "sin datos", i,1)
                                            return
                                        elif token.tipo == "tk_smay":
                                            i =+ len(token.descripcion)
                                            token = self.sacarToken()
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
                print("La condicion: ", token.descripcion)
                return token.descripcion
            else:
                i =+ len(token.descripcion)
                self.agregarError("condicion", "Se esperaba TOTAL | VISITANTE | LOCAL", i,1)
                
    def TABLA(self):
        '''TABLA condición equipo TEMPORADA <YYYY-YYYY>'''
        #? se espera reservada -- TK_tab
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
                                    print ("correcto manito wuu")
                                    encontramos_name = self.INS()
                                    if encontramos_name is None:
                                        i =+ len(token.descripcion)
                                        print("Se agrega por defecto: temporada.html")
                                    else:
                                        i =+ len(token.descripcion)
                                        print("asignación: ", encontramos_name)    
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
                                    i =+ len(token.descripcion)
                                    token = self.sacarToken()    
                                    
                                    #! Sacar otro tokens -- Se espera >
                                    if token is None:
                                            i =+ len(token.descripcion)
                                            self.agregarError("tk_smay", "sin datos",i,1)
                                            return
                                    elif token.tipo == "tk_smay":
                                        i =+ len(token.descripcion)
                                        print ("correcto manito wuu")
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
                    print("todo bien", token.descripcion)
                    return token.descripcion
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
                    print("todo bien", token.descripcion)
                    return token.descripcion
                else: 
                    i =+ len(token.descripcion)
                    self.agregarError("tkb2", "Se esperaba -j2", i, 1)
            else:
                # self.agregarError("tkb", "Se esperaba -f")
                return None                 
    def TOP(self):
        '''TOP condición TEMPORADA <YYYY-YYYY> [ -n número ]'''
        #? se espera reservada -- TK_gol
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
                                    i =+ len(token.descripcion)
                                    token = self.sacarToken()    
                                    
                                    #! Sacar otro tokens -- Se espera >
                                    if token is None:
                                            i =+ len(token.descripcion)
                                            self.agregarError("tk_smay", "sin datos",i,1)
                                            return
                                    elif token.tipo == "tk_smay":
                                        i =+ len(token.descripcion)
                                        print ("correcto manito wuu")
                                        #? se espera -f
                                        encontramos_name = self.INS3()
                                        if encontramos_name is None:
                                            i =+ len(token.descripcion)
                                            print("Se agrega por defecto: 5 equipos ")
                                        else:
                                            i =+ len(token.descripcion)
                                            print("asignación: ", encontramos_name)
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
                    i =+ len(token.descripcion)
                    print("todo bien", token.descripcion)
                    return token.descripcion
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
                i =+ len(token.descripcion)
                print("La condicion: ", token.descripcion)
                return token.descripcion
            else:
                i =+ len(token.descripcion)
                self.agregarError("condicion", "Se esperaba SUPERIOR | INFERIOR ", i,1)
    def ADIOS(self):
        '''ADIOS'''
        #? se espera reservada -- TK_tab
        token = self.sacarToken()
        if token.tipo == "TK_adios":
            token = self.sacarToken()
            i =+ len(token.descripcion)
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
    