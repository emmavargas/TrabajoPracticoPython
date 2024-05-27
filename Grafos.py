from itertools import pairwise

import networkx as nx
from matplotlib import pyplot as plt


class Grafos:
    def __init__(self, datos):
        self.g = nx.Graph()
        self.datos = datos
    def agregarNodos(self):
        lista = list(self.datos.keys())

        for key in lista:
            self.g.add_node(self.datos[key].nombre)
            for i in self.datos[key].lista:
                self.g.add_node(i[0])
                self.g.add_edge(self.datos[key].nombre, i[0], weight=i[1])


    def mostrarGraph(self):
        layout = nx.circular_layout(self.g)
        labels2 = nx.get_edge_attributes(self.g, 'weight')
        nx.draw(self.g, layout, with_labels=True, node_color='#FF5733', node_size=1000)
        nx.draw_networkx_edge_labels(self.g, layout, edge_labels=labels2)
        plt.show()

    def calcularDistanciaAmistadMinima(self, n1,n2):
        camino = nx.dijkstra_path(self.g, n1, n2, weight='weight')
        subgrafo = self.g.edge_subgraph(pairwise(camino))
        #print("Su nivel de amistad es: ",(nx.shortest_path_length(self.g, n1, n2, weight='weight')))
        nx.draw(subgrafo,nx.circular_layout(subgrafo), with_labels=True, node_color='#FF5733', node_size=1000)
        nx.draw_networkx_edge_labels(subgrafo, nx.circular_layout(subgrafo), edge_labels=nx.get_edge_attributes(subgrafo, 'weight'))
        plt.show()

