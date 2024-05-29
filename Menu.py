from CargaDatos import CargaDatos
from Grafos import Grafos



class Menu:
    def __init__(self):
        entrada =0
        while entrada == 0:
            direccion1 = 'C:\\Users\\emman\\PycharmProjects\\TrabajoPractico\\test.xlsx'
            opcion = input("ingrese la hoja del Excel:  ")
            if(opcion == "1"):
                hoja = 'Hoja 1'
                datos = CargaDatos(direccion1,hoja)
                datos.cargaDeDatos()
                grafos = Grafos(datos.alumnos)
                grafos.agregarNodos()
                grafos.mostrarGraph()
                alu1= input("Ingrese Alumno 1")
                alu2= input("Ingrese Alumno 2")
                grafos.calcularDistanciaAmistadMinima(alu1,alu2)

            if(opcion == "2"):
                hoja = 'Hoja 2'
                datos = CargaDatos(direccion1,hoja)
                datos.cargaDeDatos()
                grafos = Grafos(datos.alumnos)
                grafos.agregarNodos()
                grafos.mostrarGraph()
                alu1= input("Ingrese Alumno 1")
                alu2= input("Ingrese Alumno 2")
                grafos.calcularDistanciaAmistadMinima(alu1,alu2)
