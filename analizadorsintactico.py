from lib2to3.pgen2 import token
from tokenize import Token
from Token import constructor
from prettytable import PrettyTable

class AnalizadorSintactico:
    def __init__(self, tokens: list) -> None:
        self.errores = []
        self.tokens = tokens
        
    def agregarError(self, entrada, pila):
        self.errores.append("Error sintactico: se obtuvo {} se esperaba {}".format(entrada, pila))
    def sacarToken(self):
        """Saca nuestro primer token"""
        try: 
            return self.tokens.pop(0)
        except: 
            return None
    def observarToken(self):
        '''Saca el primer token y lo mete en la pila'''
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
            token = self.sacarToken()
            
            if token is None:
                self.agregarError("TK_result", "sin datos")
                return
            #!Sacar otro toke -- Se espera cadena
            elif token.tipo == "tk_cadena":
                token = self.sacarToken()
                if token is None:
                    self.agregarError("tk_cadena", "sin datos")
                    
                #! Sacar otro tokens -- Se espera VS
                elif token.tipo == "TK_vs":
                    token = self.sacarToken()    
                    if token is None:
                        self.agregarError("TK_vs", "sin datos")

                    #! Sacar otro tokens -- Se espera cadena
                    elif token.tipo == "tk_cadena":
                        token = self.sacarToken()    
                        if token is None:
                                    self.agregarError("tk_cadena", "sin datos")

                        #! Sacar otro tokens -- Se espera Temporada
                        elif token.tipo == "TK_temp":
                            token = self.sacarToken()    
                            if token is None:
                                self.agregarError("TK_temp", "sin datos")


                            #! Sacar otro tokens -- Se espera tk_smen
                            elif token.tipo == "tk_smen":
                                token = self.sacarToken()    
                                if token is None:
                                    self.agregarError("tk_smen", "sin datos")

                                #! Sacar otro tokens -- Se espera tk_año
                                elif token.tipo == "tk_año":
                                    token = self.sacarToken()    
                                    if token is None:
                                        self.agregarError("tk_año", "sin datos")

                                    #! Sacar otro tokens -- Se espera tk_año
                                    elif token.tipo == "tk_s":
                                        token = self.sacarToken()    
                                        if token is None:
                                            self.agregarError("tk_s", "sin datos")
                                        #! Sacar otro tokens -- Se espera tk_año
                                        elif token.tipo == "tk_año":
                                            token = self.sacarToken()    
                                            if token is None:
                                                self.agregarError("tk_año", "sin datos")

                                            #! Sacar otro tokens -- Se espera tk_año
                                            elif token.tipo == "tk_smay":   
                                                print ("correcto manito wuu")    
                                            
                                            else:
                                                self.agregarError("token incorrecto", "falto signo mayor")
                                        else: 
                                            self.agregarError("token incorrecto", "Falto año")
                                    else: 
                                        self.agregarError("token incorrecto", "Falto guion")
                                else: 
                                    self.agregarError("token incorrecto", "Falto año")
                            else: 
                                self.agregarError("token incorrecto", "Falto signo menor")
                        else: 
                            self.agregarError("token incorrecto", "Falto TEMPORADA")
                    else: 
                        self.agregarError("token incorrecto", "Falto cadena")
                else: 
                    self.agregarError("token incorrecto", "Falto VS")
            else: 
                self.agregarError("token incorrecto", "Falto cadena")
        else: 
            self.agregarError("token incorrecto", "RESULTADO")

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion"]
        for error_ in self.errores:
            x.add_row([error_])
        print(x)