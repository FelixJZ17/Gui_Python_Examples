import tkinter as tk
from tkinter import font
from config import *  ## aquí importo todas las constantes

import util.util_ventana as util_ventana
import util.util_imagenes as util_img

class FormularioMaestroDesign(tk.Tk):

    # Constructor de la clase
    def __init__(self):
        super().__init__()  ##al heredar, invocamos al constructor del padre
        self.logo = util_img.leer_imagen('./imagenes/logo_central.png', (560, 136))
        self.perfil = util_img.leer_imagen('./imagenes/foto_perfil_felix.png', (100, 100))
        self.config_window()
        self.paneles()
        
    # Codigo para ordenar la configuracion inicial de la ventana    
    def config_window(self):
        self.title('Python_GUI')
        self.iconbitmap('./imagenes/logo.ico')
        w, h = 1024, 600
        #self.geometry('%dx%d+0+0' % (w, h))  #no sé porque quita este codigo
        util_ventana.centrar_ventana(self, w, h)

    # Crear paneles
    def paneles(self):
        #Crear paneles: barra superior:
        self.barra_superior=tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')

        #Crear paneles: menú lateral:
        self.menu_lateral = tk.Frame(
            self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False)

        # Crear paneles: cuerpo principal
        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL, width=150)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)


