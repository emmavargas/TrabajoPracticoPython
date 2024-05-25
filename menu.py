from main import CargaDatos


class Menu:
    def __init__(self):
        entrada =0
        while entrada == 0:
            opcion = input("ingrese el excel que desea importar: ")
            if(opcion == "1"):
                direccion1 = 'C:\\Users\\emman\\PycharmProjects\\TrabajoPractico\\test.xlsx'
                grafo = CargaDatos(direccion1)
                n1= input("Ingrese persona 1")
                n2= input("Ingrese persona 2")
                grafo.calcularDistanciaAmistadMinima(n1,n2)
