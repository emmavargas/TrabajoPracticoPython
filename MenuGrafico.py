import tkinter as tk
from PIL import Image, ImageTk
from CargaDatos import CargaDatos
from Grafos import Grafos


class MenuGrafico:
    def __init__(self):
        self.direccion1 = 'C:\\Users\\emman\\PycharmProjects\\TrabajoPractico\\test.xlsx'
        # Crear ventana principal
        root = tk.Tk()
        root.title("Aplicacion")
        root.geometry("1000x600")
        root.resizable(False, False)

        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=3)
        root.grid_columnconfigure(0, weight=5)
        root.grid_columnconfigure(1, weight=3)


        self.marco1 = tk.Frame(root, relief="ridge",borderwidth=2)
        boton = tk.Button(self.marco1, text="Hoja 1", command=lambda: self.mostrar(1), width=10)
        boton.pack(anchor="center", padx=5, pady=20)
        boton1 = tk.Button(self.marco1, text="Hoja 2", command=lambda: self.mostrar(2),width=10)
        boton1.pack(anchor="center", padx=5, pady=1)
        self.marco1.propagate(False)

        self.marco2 = tk.Frame(root, relief="ridge",borderwidth=2)
        alu1 = tk.StringVar()
        alu2 = tk.StringVar()
        entradaAlu1 = tk.Entry(self.marco2, textvariable=alu1)
        entradaAlu1.pack(padx=5, pady=15)
        entradaAlu2 = tk.Entry(self.marco2, textvariable=alu2)
        entradaAlu2.pack(padx=5, pady=5)
        boton2 = tk.Button(self.marco2, text="Calcular Distancia Amistad", command=lambda: self.mostrarRelacion(alu1, alu2, self.grafos))
        boton2.pack(anchor="center", padx=5, pady=5)
        self.relacion = tk.Label(self.marco2, text="Nivel de Relacion: ")
        self.relacion.pack(anchor="center", padx=5, pady=5)
        self.marco2.propagate(False)


        self.marco3 = tk.Frame(root, relief="ridge",borderwidth=2)
        self.marco3.propagate(False)

        self.marco4 = tk.Frame(root, relief="ridge",borderwidth=2)
        self.marco4.propagate(False)


        self.marco1.grid(row=0, column=0, sticky="nsew")
        self.marco2.grid(row=0, column=1, sticky="nsew")
        self.marco3.grid(row=1, column=0, sticky="nsew")
        self.marco4.grid(row=1, column=1, sticky="nsew")

        root.mainloop()

    def mostrar(self, opcion):
        for widget in self.marco3.winfo_children():
            widget.destroy()
        if opcion == 1:
            #Cargamos los datos, generamos el grafo
            datos = CargaDatos(self.direccion1, 'Hoja 1')
            datos.cargaDeDatos()
            self.grafos = Grafos(datos.alumnos)
            self.grafos.agregarNodos()
            self.grafos.mostrarGraph()
            rutaImagen = 'grafo.png'

            # Cargamos la imagen y le ponemos la dimension de su marco
            img = Image.open(rutaImagen)
            img = img.resize((self.marco3.winfo_width(), self.marco3.winfo_height()), Image.BILINEAR)
            img_tk = ImageTk.PhotoImage(img)
            label = tk.Label(self.marco3, image=img_tk)
            label.image = img_tk
            label.pack(expand=True, fill="both")

        if opcion == 2:
            #Cargamos los datos, generamos el grafo
            datos = CargaDatos(self.direccion1, 'Hoja 2')
            datos.cargaDeDatos()
            self.grafos = Grafos(datos.alumnos)
            self.grafos.agregarNodos()
            self.grafos.mostrarGraph()

            rutaImagen = 'grafo.png'

            # Cargamos la imagen y le ponemos la dimension de su marco
            img = Image.open(rutaImagen)
            img = img.resize((self.marco3.winfo_width(), self.marco3.winfo_height()), Image.BILINEAR)
            img_tk = ImageTk.PhotoImage(img)
            label = tk.Label(self.marco3, image=img_tk)
            label.image = img_tk
            label.pack(expand=True, fill="both")

    def mostrarRelacion(self, alu1, alu2, datos):
        for widget in self.marco4.winfo_children():
            widget.destroy()
        alu1String = alu1.get()
        alu2String = alu2.get()
        datos.graficarDistanciaMinima(alu1String, alu2String)
        # Cargar la imagen y obtener sus dimensiones
        rutaImagen = 'relacion.png'
        img1 = Image.open(rutaImagen)
        img1 = img1.resize((self.marco4.winfo_width(), self.marco4.winfo_height()), Image.BILINEAR)
        img1Tk = ImageTk.PhotoImage(img1)
        label = tk.Label(self.marco4, image=img1Tk)
        label.image = img1Tk
        label.pack(expand=True, fill="both")
        relacionTexto = datos.calcularDistanciaMinima(alu1String,alu2String)
        self.relacion.config(text="Nivel de Relacion: " + relacionTexto)

