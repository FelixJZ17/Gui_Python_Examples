import tkinter as tk
import util.util_ventana as util_ventana

class FormularioInfoDesign(tk.Toplevel):
    ### Hereda de Toplevel, porque es una ventana secundaria. Al cerrar el principal cerrará esta tambien. 

    def __init__(self):
        super().__init__()
        self.config_window()
        self.construirWidget()

    def config_window(self):
        #Configuracion inicial de la ventana
        self.title('Python GUI')
        self.iconbitmap('./imagenes/logo.ico')
        w, h = 400, 100
        util_ventana.centrar_ventana(self, w, h)

    def construirWidget(self):
        self.labelVersion = tk.Label(self, text="Version: 1.0")
        self.labelVersion.config(fg="#000000", font=(
            'Roboto', 15), pady=10, width=20)
        self.labelVersion.pack()

        ## etiqueta Autor
        self.labelAutor = tk.Label(self, text="Autor: Félix Jiménez")
        self.labelAutor.config(fg="#000000", font=(
            'Roboto', 15), pady=10, width=20)
        self.labelAutor.pack()