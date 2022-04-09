class constructor: 
    '''Clase token'''
    def __init__(self, descripcion : str, linea, columna : int, tipo) -> None:

        self.descripcion = descripcion #?lexema
        self.linea = linea
        self.columna = columna
        self.tipo = tipo
    def imprimir_data(self):
        print(self.descripcion, self.linea, self.columna, self.tipo)



    def get_Descripción_Token (self):
        return self.descripcion
    def get_linea_Token(self):
        return self.linea
    def get_columna_Token(self):
        return self.columna
    def get_tipo_Token (self):
        return self.tipo
        