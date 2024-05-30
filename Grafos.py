from itertools import pairwise
from tkinter import messagebox

import networkx as nx
from matplotlib import pyplot as plt


class Grafos:
    def __init__(self, datos):
        self.g = nx.Graph()
        self.datos = datos

    def agregarNodos(self):
        lista = list(self.datos.keys())

        for key in lista:
            nombreMayusNodo = self.datos[key].nombre.upper()
            self.g.add_node(nombreMayusNodo)
            for i in self.datos[key].lista:
                nombreMayusNodoFinal = i[0].upper()
                self.g.add_node(nombreMayusNodoFinal)
                if i[1]=="Amigo Personal":
                    self.g.add_edge(nombreMayusNodo, nombreMayusNodoFinal, weight=3)
                elif i[1]=="Conocido":
                    self.g.add_edge(nombreMayusNodo, nombreMayusNodoFinal, weight=2)
                elif i[1]=="Compañero":
                    self.g.add_edge(nombreMayusNodo, nombreMayusNodoFinal, weight=1)
    def mostrarGraph(self):
        layout = nx.planar_layout(self.g)
        labels2 = nx.get_edge_attributes(self.g, 'weight')
        #armamos el grafico del nodo, layout es el posicionamient, with_labels si se van a mostrar las etiquetas
        nx.draw(self.g, layout, with_labels=True, node_color='#FF5733', node_size=2000, font_size=8)
        #edge_labels= especifica las etiquetas que se van a agregar, draw_networkx_edge_label agrega las etiquetas al previo grafico
        nx.draw_networkx_edge_labels(self.g, layout, edge_labels=labels2)
        #Guarda la imagen en el directorio y el close es obligatorio para limpiar siempre el armado del grafo
        plt.savefig('grafo.png')
        plt.close()

    def graficarDistanciaMinima(self, n1, n2):
        alu1Mayus =n1.upper()
        alu2Mayus =n2.upper()
        if  self.g.has_node(alu1Mayus) and  self.g.has_node(alu2Mayus) and nx.has_path(self.g, alu1Mayus, alu2Mayus):
            camino = nx.dijkstra_path(self.g, alu1Mayus, alu2Mayus, weight='weight')
            subgrafo = self.g.edge_subgraph(pairwise(camino)).copy()
            layout = nx.planar_layout(self.g)
            labels2 = nx.get_edge_attributes(subgrafo, 'weight')
            nx.draw(subgrafo, layout, with_labels=True, node_color='#FF5733', node_size=3000, font_size=10)
            nx.draw_networkx_edge_labels(subgrafo, layout, edge_labels=labels2)
            plt.savefig('relacion.png')
            plt.close()
        elif  self.g.has_node(alu1Mayus) and  self.g.has_node(alu2Mayus) and not nx.has_path(self.g, alu1Mayus, alu2Mayus):
            grafoAux = self.g.copy()
            grafoAux.clear()
            layout = nx.planar_layout(grafoAux)
            labels2 = nx.get_edge_attributes(grafoAux, 'weight')
            nx.draw(grafoAux, layout, with_labels=True, node_color='#FF5733', node_size=3000, font_size=10)
            nx.draw_networkx_edge_labels(grafoAux, layout, edge_labels=labels2)
            plt.savefig('relacion.png')
            plt.close()
        else:
            grafoAux = self.g.copy()
            grafoAux.clear()
            layout = nx.planar_layout(grafoAux)
            labels2 = nx.get_edge_attributes(grafoAux, 'weight')
            nx.draw(grafoAux, layout, with_labels=True, node_color='#FF5733', node_size=3000, font_size=10)
            nx.draw_networkx_edge_labels(grafoAux, layout, edge_labels=labels2)
            plt.savefig('relacion.png')
            plt.close()


    def calcularDistanciaMinima(self,n1,n2):
        alu1Mayus = n1.upper()
        alu2Mayus = n2.upper()
        if self.g.has_node(alu1Mayus) and self.g.has_node(alu2Mayus) and nx.has_path(self.g, alu1Mayus, alu2Mayus):
            nivelRelacion = nx.shortest_path_length(self.g, alu1Mayus, alu2Mayus, weight='weight')
            return "La distancia de Amistad es " + str(nivelRelacion)
        elif self.g.has_node(alu1Mayus) and self.g.has_node(alu2Mayus) and not nx.has_path(self.g, alu1Mayus, alu2Mayus):
            messagebox.showinfo(message="No existe camino posible", title="Error")
            return ""
        else:
            messagebox.showinfo(message="Alguno de los nodos no existe en el grafo.", title="Error")
            return ""




