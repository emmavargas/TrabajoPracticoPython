import pandas as pd
from Alumno import Alumno


class CargaDatos:
    def __init__(self, archivo, hoja):

        self.dataFrame = pd.read_excel(archivo, sheet_name=hoja, header=0)
        self.dataFrame = self.dataFrame.apply(lambda x: x.str.upper())
        self.alumnos = {}

    # opcion 1
    # Creamos objetos nodo, guardamos en un diccionario y luego lo pasamos a los grafos
    def cargaDeDatos(self):
        #iterrows metodo de pandas, itera la fila de los dataFrame en dos valores (indiceLineaa, Linea)
        for indice, fila in self.dataFrame.iterrows():
            #Si existe el nodo ya en el diccionario se agrega la relacion a la lista de adyacencia
            if fila['Alumno'] in self.alumnos.keys() and fila['Relacion'] in self.alumnos.keys():
                self.alumnos.get(fila['Alumno']).agregar((fila['Relacion'], fila['Tipo']))
                self.alumnos.get(fila['Relacion']).agregar((fila['Alumno'], fila['Tipo']))
            #Si no existe uno y el otro no
            elif fila['Alumno'] not in self.alumnos.keys() and fila['Relacion'] in self.alumnos.keys():
                alu = Alumno(fila['Alumno'])
                alu.agregar([fila['Relacion'], fila['Tipo']])
                self.alumnos[alu.nombre] = alu
                self.alumnos.get(fila['Relacion']).agregar((fila['Alumno'], fila['Tipo']))
            #Si no existe uno y el otro no
            elif fila['Alumno'] in self.alumnos.keys() and fila['Relacion'] not in self.alumnos.keys():
                self.alumnos.get(fila['Alumno']).agregar((fila['Relacion'], fila['Tipo']))
                alu = Alumno(fila['Relacion'])
                alu.agregar([fila['Alumno'], fila['Tipo']])
                self.alumnos[alu.nombre] = alu
            #Si no existe el nodo
            else:
                alu = Alumno(fila['Alumno'])
                alu.agregar([fila['Relacion'], fila['Tipo']])
                self.alumnos[alu.nombre] = alu
                alu1 = Alumno(fila['Relacion'])
                alu1.agregar([fila['Alumno'], fila['Tipo']])
                self.alumnos[alu1.nombre] = alu1
