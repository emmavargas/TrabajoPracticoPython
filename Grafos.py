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
                if i[1]=="Amigo Personal":
                    self.g.add_edge(self.datos[key].nombre, i[0], weight=3)
                elif i[1]=="Conocido":
                    self.g.add_edge(self.datos[key].nombre, i[0], weight=2)
                elif i[1]=="Compañero":
                    self.g.add_edge(self.datos[key].nombre, i[0], weight=1)
    def mostrarGraph(self):
        layout = nx.planar_layout(self.g)
        labels2 = nx.get_edge_attributes(self.g, 'weight')
        nx.draw(self.g, layout, with_labels=True, node_color='#FF5733', node_size=1000)
        nx.draw_networkx_edge_labels(self.g, layout, edge_labels=labels2)
        plt.savefig('grafo.png')
        plt.close()

    def graficarDistanciaMinima(self, n1, n2):
        if  self.g.has_node(n1) and  self.g.has_node(n2) and nx.has_path(self.g, n1, n2):
            camino = nx.dijkstra_path(self.g, n1, n2, weight='weight')
            subgrafo = self.g.edge_subgraph(pairwise(camino)).copy()
            layout = nx.planar_layout(self.g)
            labels2 = nx.get_edge_attributes(subgrafo, 'weight')
            nx.draw(subgrafo, layout, with_labels=True, node_color='#FF5733', node_size=1000)
            nx.draw_networkx_edge_labels(subgrafo, layout, edge_labels=labels2)
            plt.savefig('relacion.png')
            plt.close()
        elif  self.g.has_node(n1) and  self.g.has_node(n2) and not nx.has_path(self.g, n1, n2):
            grafoAux = self.g.copy()
            grafoAux.clear()
            layout = nx.planar_layout(grafoAux)
            labels2 = nx.get_edge_attributes(grafoAux, 'weight')
            nx.draw(grafoAux, layout, with_labels=True, node_color='#FF5733', node_size=1000)
            nx.draw_networkx_edge_labels(grafoAux, layout, edge_labels=labels2)
            plt.savefig('relacion.png')
            plt.close()
        else:
            grafoAux = self.g.copy()
            grafoAux.clear()
            layout = nx.planar_layout(grafoAux)
            labels2 = nx.get_edge_attributes(grafoAux, 'weight')
            nx.draw(grafoAux, layout, with_labels=True, node_color='#FF5733', node_size=1000)
            nx.draw_networkx_edge_labels(grafoAux, layout, edge_labels=labels2)
            plt.savefig('relacion.png')
            plt.close()


    def calcularDistanciaMinima(self,n1,n2):
        if self.g.has_node(n1) and self.g.has_node(n2) and nx.has_path(self.g, n1, n2):
            nivelRelacion = nx.shortest_path_length(self.g, n1, n2, weight='weight')
            return "La distancia de Amistad es " + str(nivelRelacion)
        elif self.g.has_node(n1) and self.g.has_node(n2) and not nx.has_path(self.g, n1, n2):
            return "No existe camino posible"
        else:
            return "Alguno de los nodos no existe en el grafo."




