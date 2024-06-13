from itertools import pairwise
import networkx as nx
from matplotlib import pyplot as plt

class Grafos:
    def __init__(self, datos):
        self.g = nx.Graph()
        self.datos = datos

    def agregarNodos(self):
        for key in self.datos:
            nombreInicial = self.datos[key].nombre
            self.g.add_node(nombreInicial)
            for adyacencia in self.datos[key].lista:
                nombreFinal = adyacencia[0]
                self.g.add_node(nombreFinal)
                if adyacencia[1] == "AMIGO PERSONAL":
                    self.g.add_edge(nombreInicial, nombreFinal, weight=3)
                elif adyacencia[1] == "CONOCIDO":
                    self.g.add_edge(nombreInicial, nombreFinal, weight=2)
                elif adyacencia[1] == "COMPAÑERO":
                    self.g.add_edge(nombreInicial, nombreFinal, weight=1)

    def mostrarGraph(self):
        self.generarGrafico(self.g, 'grafo.png')

    def graficarDistanciaMinima(self, n1, n2):
        alu1Mayus = n1.upper()
        alu2Mayus = n2.upper()
        if self.g.has_node(alu1Mayus) and self.g.has_node(alu2Mayus) and nx.has_path(self.g, alu1Mayus, alu2Mayus):
            camino = nx.dijkstra_path(self.g, alu1Mayus, alu2Mayus, weight='weight')
            subgrafo = self.g.edge_subgraph(pairwise(camino)).copy()
            self.generarGrafico(subgrafo, 'relacion.png')
        else:
            self.generarGrafico(self.g, 'relacion.png')

    def calcularDistanciaMinima(self, n1, n2):
        alu1Mayus = n1.upper()
        alu2Mayus = n2.upper()
        if self.g.has_node(alu1Mayus) and self.g.has_node(alu2Mayus) and nx.has_path(self.g, alu1Mayus, alu2Mayus) and alu1Mayus != alu2Mayus:
            nivelRelacion = nx.shortest_path_length(self.g, alu1Mayus, alu2Mayus, weight='weight')
            return "" + str(nivelRelacion)  #retorno correcto
        elif self.g.has_node(alu1Mayus) and self.g.has_node(alu2Mayus) and not nx.has_path(self.g, alu1Mayus,alu2Mayus):
            return 1  #significa que no existe camino posible
        elif alu1Mayus == alu2Mayus and self.g.has_node(alu1Mayus):
            return 2
        else:
            if(self.g.has_node(alu2Mayus) and not self.g.has_node(alu1Mayus)):
                return 3
            elif(self.g.has_node(alu1Mayus) and not self.g.has_node(alu2Mayus)):
                return 4
            elif(not self.g.has_node(alu1Mayus) and not self.g.has_node(alu2Mayus)):
                return 5
            #return 3  #significa que uno o ambos nodos no existen en el grafo


    @staticmethod
    def generarGrafico(g, nombrearchivo):
        layout = nx.planar_layout(g)
        labels2 = nx.get_edge_attributes(g, 'weight')
        nx.draw(g, layout, with_labels=True, node_color='#FF5733', node_size=3000, font_size=10)
        nx.draw_networkx_edge_labels(g, layout, edge_labels=labels2)
        plt.savefig(nombrearchivo)
        plt.close()
