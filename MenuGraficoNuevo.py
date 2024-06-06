import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import customtkinter as ctk
from CargaDatos import CargaDatos
from Grafos import Grafos


class MenuGraficoNuevo:

    def __init__(self):
        self.grafos = None
        self.direccion1 = 'test.xlsx'

        ctk.set_appearance_mode("Dark")
        root = ctk.CTk()
        root.title("TP POO2")
        root.geometry("800x600")
        root.resizable(False, False)
        root.grid_rowconfigure(0, weight=1)
        root.grid_rowconfigure(1, weight=3)
        root.grid_columnconfigure(0, weight=3)
        root.grid_columnconfigure(1, weight=3)

        self.marco1 = ctk.CTkFrame(root, corner_radius=10)
        self.marcobotones = ctk.CTkFrame(self.marco1, corner_radius=10)
        infoexcel = ctk.CTkLabel(self.marcobotones, text="Seleccione una hoja de Excel para cargar", font=ctk.CTkFont('Arial', 16))
        infoexcel.pack(anchor="center", padx=10, pady=10)
        boton = ctk.CTkButton(self.marcobotones, text="Hoja 1", command=lambda: self.mostrar(1), width=150)
        boton.pack(anchor="center", padx=5, pady=10)
        boton1 = ctk.CTkButton(self.marcobotones, text="Hoja 2", command=lambda: self.mostrar(2), width=150)
        boton1.pack(anchor="center", padx=5, pady=10)
        self.marco1.propagate(False)
        self.marco1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.marcobotones.pack(anchor="center", expand=True, padx=10, pady=10)

        self.marco2 = ctk.CTkFrame(root, corner_radius=10)
        alu1 = tk.StringVar()
        alu2 = tk.StringVar()
        self.marcoentradas = ctk.CTkFrame(self.marco2, corner_radius=10)
        entradaAlu1 = ctk.CTkEntry(self.marcoentradas, textvariable=alu1, width=200)
        entradaAlu1.pack(padx=5, pady=5)
        entradaAlu2 = ctk.CTkEntry(self.marcoentradas, textvariable=alu2, width=200)
        entradaAlu2.pack(padx=5, pady=5)
        self.boton2 = ctk.CTkButton(self.marcoentradas, text="Calcular Distancia Amistad", command=lambda: self.mostrarRelacion(alu1, alu2, self.grafos))
        self.boton2.configure(state="disabled")
        self.boton2.pack(anchor="center", padx=5, pady=5)
        self.relacion = ctk.CTkLabel(self.marco2, text="La distancia de relacion es: ", font=ctk.CTkFont('Arial', 16))
        self.marco2.propagate(False)
        self.marco2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.marcoentradas.pack(anchor="center", expand=True, padx=10, pady=10)

        self.marco3 = ctk.CTkFrame(root)
        self.marco3.propagate(False)
        self.marco3.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self.marco4 = ctk.CTkFrame(root)
        self.marco4.propagate(False)
        self.marco4.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)

        root.mainloop()

    def mostrar(self, opcion):
        self.limpiarMarcos(self.marco3)
        self.limpiarMarcos(self.marco4)
        self.relacion.pack_forget()
        if opcion == 1:
            # Cargamos los datos, generamos el grafo
            datos = CargaDatos(self.direccion1, 'Hoja 1')
            datos.cargaDeDatos()
            self.grafos = Grafos(datos.alumnos)
            self.grafos.agregarNodos()
            self.grafos.mostrarGraph()
            rutaImagen = 'grafo.png'

            # Cargamos la imagen y le ponemos la dimension de su marco
            self.mostrarImagen(rutaImagen, self.marco3)

        elif opcion == 2:
            # Cargamos los datos, generamos el grafo
            datos = CargaDatos(self.direccion1, 'Hoja 2')
            datos.cargaDeDatos()
            self.grafos = Grafos(datos.alumnos)
            self.grafos.agregarNodos()
            self.grafos.mostrarGraph()

            rutaImagen = 'grafo.png'

            # Cargamos la imagen y le ponemos la dimension de su marco
            self.mostrarImagen(rutaImagen, self.marco3)

        self.boton2.configure(state='normal')

    def mostrarRelacion(self, alu1, alu2, grafo):
        # nunca entra hay que revisar para que sea la condicion del disable boton
        if self.grafos is None:
            self.limpiarMarcos(self.marco4)
            messagebox.showinfo(message="No se ha cargado ningun Excel", title="Error")
        else:
            self.limpiarMarcos(self.marco4)
            self.relacion.configure(text="La distancia de relacion es: ")
            alu1String = alu1.get()
            alu2String = alu2.get()
            grafo.graficarDistanciaMinima(alu1String, alu2String)

            # Cargar la imagen y obtener sus dimensiones
            rutaImagen = 'relacion.png'
            self.mostrarImagen(rutaImagen, self.marco4)

            relacionTexto = grafo.calcularDistanciaMinima(alu1String, alu2String)
            if relacionTexto == 1:
                self.limpiarMarcos(self.marco4)
                self.relacion.pack_forget()
                messagebox.showinfo(message="No existe camino posible", title="Error")
            elif relacionTexto == 2:
                self.limpiarMarcos(self.marco4)
                self.relacion.pack_forget()
                messagebox.showinfo(message="Alguno de los nodos no existe en el grafo.", title="Error")
            else:
                self.relacion.configure(text="La distancia de relacion es: " + relacionTexto)
                self.relacion.pack(anchor="center", padx=5, pady=5)

    @staticmethod
    def mostrarImagen(rutaImagen, marco):
        img = ctk.CTkImage(light_image=Image.open(rutaImagen), size=(marco.winfo_width(), marco.winfo_height()))
        label = ctk.CTkLabel(marco, image=img, text='')
        label.pack()

    @staticmethod
    def limpiarMarcos(marco):
        for widget in marco.winfo_children():
            widget.destroy()
