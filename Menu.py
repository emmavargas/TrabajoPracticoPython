from CargaDatos import CargaDatos
from Grafos import Grafos



class Menu:
    def __init__(self):
        entrada =0
        while entrada == 0:
            opcion = input("ingrese el excel que desea importar: ")
            if(opcion == "1"):
                direccion1 = 'C:\\Users\\emman\\PycharmProjects\\TrabajoPractico\\test.xlsx'
                datos = CargaDatos(direccion1)
                datos.cargaDeDatos()
                grafos = Grafos(datos.nodos)
                grafos.agregarNodos()
                grafos.mostrarGraph()
                n1= input("Ingrese persona 1")
                n2= input("Ingrese persona 2")
                grafos.calcularDistanciaAmistadMinima(n1,n2)

            if(opcion == "2"):
                direccion1 = 'C:\\Users\\emman\\PycharmProjects\\TrabajoPractico\\test2.xlsx'
                datos = CargaDatos(direccion1)
                datos.cargaDeDatos()
                grafos = Grafos(datos.nodos)
                grafos.agregarNodos()
                grafos.mostrarGraph()
                n1= input("Ingrese persona 1")
                n2= input("Ingrese persona 2")
                grafos.calcularDistanciaAmistadMinima(n1,n2)
