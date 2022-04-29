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
        print(datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año, año1)) & (datos['Equipo1'] == e1) & (datos['Equipo2'] == e2)].values)
        return datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año, año1)) & (datos['Equipo1'] == e1) & (datos['Equipo2'] == e2)].values

    def resultados_jornada(self, numero: int, año1: int, año2: int, nombre: str):
        datos = pd.DataFrame(self.datos, columns = ['Temporada', 'Jornada', 'Equipo1', 'Equipo2', 'Goles1', 'Goles2'])
        a1 =  datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Jornada'] == numero)].values
        salida = open(nombre, 'w')
        #!================================================================
        html = '''<p>Tabla de JORNADA</p>
                <p>&nbsp;</p>
                <p>&nbsp;</p>
                <p>&nbsp;</p>
                <p>&nbsp;</p>
                <table style="border-collapse: collapse; width: 100%;" border="1">
                <tbody>
                <tr>
                <td style="width: 14.2857%;">Temporada</td>
                <td style="width: 14.2857%;">Jornada</td>
                <td style="width: 14.2857%;">Equipo 1</td>
                <td style="width: 14.2857%;">Equipo 2</td>
                <td style="width: 14.2857%;">Goles 1</td>
                <td style="width: 14.2857%;">Goles 2</td>
                </tr>
                                </tbody>
                </table>
                '''
        entradas = ""
        for i in range (len(a1)): 
        
            entradas +='''
                <table style="border-collapse: collapse; width: 100%;" border="1">
                <tbody>
                <tr>
                <td style="width: 20%;"> {}</td>
                <td style="width: 20%;"> {}</td>
                <td style="width: 20%;"> {}</td>
                <td style="width: 20%;"> {}</td>
                <td style="width: 20%;"> {}</td>
                </tr>
                </tbody>
                </table>'''.format(i [0], i[1], i[2],  i[3],i[4], i[5], i[6])
        

        suma = html + entradas
        s
        #!==============================================================
        
    def resultados_goles(self, condicion: str, equipo: str, año1: int, año2: int):
        datos = pd.DataFrame(self.datos, columns = ['Temporada', 'Equipo1', 'Equipo2', 'Goles1', 'Goles2'])
        
        if condicion == 'LOCAL':
            return datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo1'] == equipo)].groupby('Equipo1')['Goles1'].sum().head().values
        elif condicion == 'VISITANTE':
            return datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo2'] == equipo)].groupby('Equipo2')['Goles2'].sum().head().values
        elif condicion == 'TOTAL':
            local = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo1'] == equipo)].groupby('Equipo1')['Goles1'].sum().head().values
            visita = datos.loc[(datos['Temporada'] == '{0}-{1}'.format(año1, año2)) & (datos['Equipo2'] == equipo)].groupby('Equipo2')['Goles2'].sum().head().values
            
            return local + visita
    
      
    def resultados_tabla(self, año1: int, año2: int, bandera__f: str = None ):
        datos = pd.DataFrame(self.datos, columns=["Temporada", "Equipo1", "Equipo2", "Goles1", "Goles2"])
        d1 = datos.loc[(datos["Temporada"] == "{0}-{1}".format(año1, año2))].values

        puntajes = {}
        for v1 in d1:
            local = v1[1]
            visita = v1[2]
            gol_lo = v1[3]
            goles_visita = v1[4]
            guardado = puntajes.get(local) or 0
            guardado_salida = puntajes.get(visita) or 0

            if gol_lo == goles_visita:
                puntajes[local] = guardado + 1
                puntajes[visita] = guardado_salida + 1
           
           
            elif gol_lo > goles_visita:
                puntajes[local] = guardado + 3
            
            
            
            elif gol_lo < goles_visita:
                puntajes[visita] = guardado_salida + 3
        
        lista_puntajes = []
        
        
        
        for key, value in puntajes.items():
            lista_puntajes.append([key, value])
            
        def ordenar(elemento):
            return elemento[1]
        
        lista_puntajes.sort(key=ordenar)

        return lista_puntajes
    def resultado_equipo(self, equipo: str, año1: int, año2: int, bandera__f: str = None,   bandera_ji: str = None, bandera_jf: str = None):
        
        datos = pd.DataFrame(self.datos, columns=["Temporada", "Jornada", "Equipo1", "Equipo2", "Goles1", "Goles2"])
        datos = datos.loc[(datos["Temporada"] == "{0}-{1}".format(año1, año2))].loc[(datos["Equipo1"] == equipo) | (datos["Equipo2"] == equipo)]

        if bandera_ji != None and bandera_jf != None:
            datos = datos.loc[(datos["Jornada"] >= int(bandera_ji)) & (datos["Jornada"] <= int(bandera_jf))]
        
        return datos.values
    def resultado_top(self, condicion: str, año1: int, año2: int, bandera_n: int = 5):
        
        d1 = pd.DataFrame(self.datos, columns=["Temporada", "Equipo1", "Equipo2", "Goles1", "Goles2"])
        d1 = d1.loc[(d1["Temporada"] == "{0}-{1}".format(año1, año2))].values
        
        puntos = {}
        for v1 in d1:
            local = v1[1]
            visita = v1[2]
            goles_local = v1[3]
            goles_visita = v1[4]
            historico_local = puntos.get(local) or 0
            historico_visita = puntos.get(visita) or 0

            if goles_local == goles_visita:
                puntos[local] = historico_local + 1
                puntos[visita] = historico_visita + 1
            elif goles_local > goles_visita:
                puntos[local] = historico_local + 3
            elif goles_local < goles_visita:
                puntos[visita] = historico_visita + 3

        lista_puntajes = []
        for key, value in puntos.items():
            lista_puntajes.append([key, value])
            
        def ordenar(elemento):
            return elemento[1]
        
        lista_puntajes.sort(key=ordenar)
        
        if int(bandera_n) <= len(lista_puntajes):
            if condicion == "SUPERIOR":
                inicio = len(lista_puntajes) - int(bandera_n)
                lista_puntajes = lista_puntajes[inicio:]
                return lista_puntajes[::-1]
            else:
                return lista_puntajes[:int(bandera_n)]