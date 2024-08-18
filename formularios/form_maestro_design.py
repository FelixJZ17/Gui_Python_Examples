import tkinter as tk
from tkinter import font, PhotoImage
from PIL import Image, ImageTk
from config import *  ## aquí importo todas las constantes

import util.util_ventana as util_ventana
import util.util_imagenes as util_img

import fontawesome as fa

class FormularioMaestroDesign(tk.Tk):

    # Constructor de la clase
    def __init__(self):
        super().__init__()  ##al heredar, invocamos al constructor del padre
        self.logo = util_img.leer_imagen('./imagenes/logo_central.png', (560, 136))
        self.perfil = util_img.leer_imagen('./imagenes/foto_perfil_felix.png', (100, 100))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        
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

    # Controles de barra superior
    def controles_barra_superior(self):
        # Configuracion de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        #Etiqueta de titulos
        self.labelTitulo = tk.Label(self.barra_superior, text='FJ Gestiones')
        self.labelTitulo.config(
            fg='#fff', font=('Roboto', 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón menú lateral   ---> texto \uf0c9 es un codigo para representar simbolo de "Bars " --> al final descargo como assets porque no lee bien
        # Cargar la imagen PNG
        img = Image.open("imagenes/assets/bars-solid-blanco_400x400.png")
        img = img.resize((20, 20), Image.Resampling.LANCZOS)  # Redimensionar si es necesario
        self.photo = ImageTk.PhotoImage(img)  ##tengo que hacerlo con el self, ya que sino no me muestra la foto.
        self.buttonMenuLateral = tk.Button(self.barra_superior, text='prueba', image=self.photo, font=font_awesome,
                                           command=lambda: print("¡Botón presionado!"), bd=0, bg=COLOR_BARRA_SUPERIOR, fg='white')
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de información
        self.labelInformacion = tk.Label(self.barra_superior, text='felix@fjgestiones.com')
        self.labelInformacion.config(
            fg='#fff', font=('Roboto', 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelInformacion.pack(side=tk.RIGHT)




