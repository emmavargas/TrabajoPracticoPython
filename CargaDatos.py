import pandas as pd
from Alumno import Alumno

class CargaDatos:
    def __init__(self, archivo):

        self.df = pd.read_excel(archivo, sheet_name='Hoja 1', header=None)



        # opcion 1
        # Creamos objetos nodo, guardamos en un diccionario y luego lo pasamos a los grafos

    def cargaDeDatos(self):
        self.nodos = {}

        for i, fila in self.df.iterrows():
            if fila[0] in self.nodos.keys():
                self.nodos.get(fila[0]).agregar([fila[1], fila[2]])
            else:
                nodo = Alumno(fila[0])
                nodo.agregar([fila[1], fila[2]])
                self.nodos[fila[0]] = nodo


        # Opcion 2
        # copiamos los datos directamente del excel a los nodos
        '''for i, fila in df.iterrows():
            g.add_node(fila[0])
            g.add_node(fila[1])
            g.add_edge(fila[0], fila[1], weight=fila[2])'''





