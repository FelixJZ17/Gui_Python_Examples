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
        self.perfil = util_img.leer_imagen('./imagenes/foto_perfil_felix_redondo.png', (250, 200)) #width,height
        self.config_window()
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()

        
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
        self.buttonBarraSuperior = tk.Button(self.barra_superior, text='prueba', image=self.photo, font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg='white')
        self.buttonBarraSuperior.pack(side=tk.LEFT)

        # Etiqueta de información
        self.labelInformacion = tk.Label(self.barra_superior, text='felix@fjgestiones.com')
        self.labelInformacion.config(
            fg='#fff', font=('Roboto', 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelInformacion.pack(side=tk.RIGHT)


    # Controles de barra superior
    def controles_menu_lateral(self):


        # Configuracion del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
        
        # Etiquetas de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botón del menú lateral
        self.buttonDashBoard =tk.Button(self.menu_lateral)
        self.buttonProfile =tk.Button(self.menu_lateral)
        self.buttonPicture =tk.Button(self.menu_lateral)
        self.buttonInfo =tk.Button(self.menu_lateral)
        self.buttonSettings =tk.Button(self.menu_lateral)

        ## Lista de botones para configurarlos de la misma manera
        buttons_menu_lateral_list = [
            ("Dashboard", "💻", self.buttonDashBoard),
            ("Profile", "🙎", self.buttonProfile),
            ("Picture", "🖼️", self.buttonPicture),
            ("Info", "ℹ️", self.buttonInfo),
            ("Settings", "⚙️", self.buttonSettings),
        ]

        for text, icon, button in buttons_menu_lateral_list:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu)

    # Controles de cuerpo
    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)


    ## Función para configurar botones con el for
    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu):
        button.config(text=f'{text}    {icon}', anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="white", width=ancho_menu, height=alto_menu)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

        ## Asociar eventos Enter y Leave con la función dinámica
    def bind_hover_events(self, button):
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

        # Cambiar el estilo al pasar el ratón por encima
    def on_enter(self, event, button):
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA, fg="white")

        # Restaurar estilo al salir el ratón
    def on_leave(self, event, button):
        button.config(bg=COLOR_MENU_LATERAL, fg="white")

        # Alternar visibilidad del menú lateral
    def toggle_panel(self):
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    

