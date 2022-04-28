import pandas as pd
from pandas import DataFrame

class ImportarCSV:
    ruta: str = None
    datos: DataFrame = None
    def __init__(self, ruta: str):
        self.ruta = ruta
        self.datos = pd.read_csv(self.ruta, header = [0], encoding='utf8')
        
    def resultado_partido(self, e1: str, e2: str, año: int, año1: int):
        datos = pd.DataFrame(self.datos, columns = ['Temporada', 'Equipo1', 'Equipo2', 'Goles1', 'Goles2'])
        return datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año, año1)) & (datos['Equipo1'] == e1) & (datos['Equipo2'] == e2)].values
    