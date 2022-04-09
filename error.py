class Error: 
    "Clase Errores"
    def __init__(self, descripcion:str, linea, columna, tipo):

        self.descripcion = descripcion #? lexema
        self.linea = linea
        self.tipo = tipo
        self.columna = columna
    def imprimir_error(self):
        print(self.descripcion, self.linea, self.columna)