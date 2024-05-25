import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
from Nodo import Nodo

class CargaDatos:
    def __init__(self, archivo):

        df = pd.read_excel(archivo, sheet_name='Hoja 1', header=None)

        self.g = nx.Graph()

        # opcion 1
        # Creamos objetos nodo, guardamos en un diccionario y luego lo pasamos a los grafos
        nodos = {}

        for i, fila in df.iterrows():
            if fila[0] in nodos.keys():
                nodos.get(fila[0]).agregar([fila[1], fila[2]])
            else:
                nodo = Nodo(fila[0])
                nodo.agregar([fila[1], fila[2]])
                nodos[fila[0]] = nodo

        lista = list(nodos.keys())

        for key in lista:
            self.g.add_node(nodos[key].nombre)
            for i in nodos[key].lista:
                self.g.add_node(i[0])
                self.g.add_edge(nodos[key].nombre, i[0], weight=i[1])

        # Opcion 2
        # copiamos los datos directamente del excel a los nodos
        '''for i, fila in df.iterrows():
            g.add_node(fila[0])
            g.add_node(fila[1])
            g.add_edge(fila[0], fila[1], weight=fila[2])'''

        layout = nx.spring_layout(self.g)
        labels2 = nx.get_edge_attributes(self.g, 'weight')
        nx.draw(self.g, layout, with_labels=True, node_color='#FF5733', node_size=1000)
        nx.draw_networkx_edge_labels(self.g, layout, edge_labels=labels2)
        plt.show()


    def calcularDistanciaAmistadMinima(self, n1,n2):
        #print(nx.dijkstra_path(g, n1, n2, weight='weight'))
        print("Su nivel de amistad es: ",(nx.shortest_path_length(self.g, n1, n2, weight='weight')))




