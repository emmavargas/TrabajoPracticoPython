import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from CargaDatos import CargaDatos
from Grafos import Grafos


class MenuGrafico:
    def __init__(self):
        self.grafos = None
        self.direccion1 = 'test.xlsx'
        self.condicionMostrarRelacion = False

        # Crear ventana principal
        root = tk.Tk()
        root.title("Aplicacion")
        root.geometry("1200x700")
        root.resizable(False, False)

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=3)
        root.grid_columnconfigure(0, weight=5)
        root.grid_columnconfigure(1, weight=3)

        self.marco1 = tk.Frame(root, relief="ridge", borderwidth=2)
        boton = tk.Button(self.marco1, text="Hoja 1", command=lambda: self.mostrar(1), width=10)
        boton.pack(anchor="center", padx=5, pady=20)
        boton1 = tk.Button(self.marco1, text="Hoja 2", command=lambda: self.mostrar(2), width=10)
        boton1.pack(anchor="center", padx=5, pady=1)
        self.marco1.propagate(False)
        #emma

        self.marco2 = tk.Frame(root, relief="ridge", borderwidth=2)
        alu1 = tk.StringVar()
        alu2 = tk.StringVar()
        entradaAlu1 = tk.Entry(self.marco2, textvariable=alu1)
        entradaAlu1.pack(padx=5, pady=15)
        entradaAlu2 = tk.Entry(self.marco2, textvariable=alu2)
        entradaAlu2.pack(padx=5, pady=5)
        self.boton2 = tk.Button(self.marco2, text="Calcular Distancia Amistad", command=lambda: self.mostrarRelacion(alu1, alu2, self.grafos))
        self.boton2.config(state=tk.DISABLED)
        self.boton2.pack(anchor="center", padx=5, pady=5)
        self.relacion = tk.Label(self.marco2, text="La distancia de relacion es: ")
        self.marco2.propagate(False)

        self.marco3 = tk.Frame(root, relief="ridge", borderwidth=2)
        self.marco3.propagate(False)

        self.marco4 = tk.Frame(root, relief="ridge", borderwidth=2)
        self.marco4.propagate(False)

        self.marco1.grid(row=0, column=0, sticky="nsew")
        self.marco2.grid(row=0, column=1, sticky="nsew")
        self.marco3.grid(row=1, column=0, sticky="nsew")
        self.marco4.grid(row=1, column=1, sticky="nsew")

        root.mainloop()

    def mostrar(self, opcion):
        self.limpiarMarcos(self.marco3)
        self.limpiarMarcos(self.marco4)
        self.relacion.pack_forget()
        if opcion == 1:
            #Cargamos los datos, generamos el grafo
            datos = CargaDatos(self.direccion1, 'Hoja 1')
            datos.cargaDeDatos()
            self.grafos = Grafos(datos.alumnos)
            self.grafos.agregarNodos()
            self.grafos.mostrarGraph()
            rutaImagen = 'grafo.png'

            # Cargamos la imagen y le ponemos la dimension de su marco
            self.mostrarImagen(rutaImagen, self.marco3)

        elif opcion == 2:
            #Cargamos los datos, generamos el grafo
            datos = CargaDatos(self.direccion1, 'Hoja 2')
            datos.cargaDeDatos()
            self.grafos = Grafos(datos.alumnos)
            self.grafos.agregarNodos()
            self.grafos.mostrarGraph()

            rutaImagen = 'grafo.png'

            # Cargamos la imagen y le ponemos la dimension de su marco
            self.mostrarImagen(rutaImagen, self.marco3)

        self.boton2.config(state=tk.NORMAL)

    def mostrarRelacion(self, alu1, alu2, grafo):
        if self.grafos is None:
            self.limpiarMarcos(self.marco4)
            messagebox.showinfo(message="No se ha cargado ningun Excel", title="Error")
        else:
            self.limpiarMarcos(self.marco4)
            self.relacion.config(text="La distancia de relacion es: ")
            alu1String = alu1.get()
            alu2String = alu2.get()
            grafo.graficarDistanciaMinima(alu1String, alu2String)

            # Cargar la imagen y obtener sus dimensiones
            rutaImagen = 'relacion.png'
            self.mostrarImagen(rutaImagen, self.marco4)

            relacionTexto = grafo.calcularDistanciaMinima(alu1String, alu2String)
            if relacionTexto == 1:
                self.limpiarMarcos(self.marco4)
                messagebox.showinfo(message="No existe camino posible", title="Error")
            elif relacionTexto == 2:
                self.limpiarMarcos(self.marco4)
                messagebox.showinfo(message="Alguno de los nodos no existe en el grafo.", title="Error")
            else:
                self.relacion.config(text="La distancia de relacion es: " + relacionTexto)
                self.relacion.pack(anchor="center", padx=5, pady=5)


    @staticmethod
    def mostrarImagen(rutaImagen, marco):
        img = Image.open(rutaImagen)
        img = img.resize((marco.winfo_width(), marco.winfo_height()), Image.BILINEAR)
        img_tk = ImageTk.PhotoImage(img)
        label = tk.Label(marco, image=img_tk)
        label.image = img_tk
        label.pack(expand=True, fill="both")

    @staticmethod
    def limpiarMarcos(marco):
        for widget in marco.winfo_children():
            widget.destroy()
