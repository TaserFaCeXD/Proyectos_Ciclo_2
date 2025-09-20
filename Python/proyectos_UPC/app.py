import tkinter as tk
from PIL import Image, ImageTk
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
imagen_path = os.path.join(BASE_DIR, "fondo.png")

# Crear ventana
ventana = tk.Tk()
ventana.title("App con Fondo y Botones")
ventana.geometry("900x600")

# --- Imagen de fondo ---
imagen = Image.open(imagen_path)  # usa tu propia imagen
imagen = imagen.resize((900, 600))  # ajusta al tamaño de la ventana
fondo = ImageTk.PhotoImage(imagen)

label_fondo = tk.Label(ventana, image=fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # ocupa toda la ventana

# --- Botón personalizado ---
def accion():
    exit()

boton = tk.Button(
    ventana, 
    text="Salir", 
    command=accion,
    font=("Arial", 25, "bold"),
    bg="#365785",      # color de fondo
    fg="white",        # color del texto
    activebackground="#365785",  # color al presionar
    relief="flat",     # estilo (flat, raised, sunken, groove, ridge)
    padx=100, pady=0   # tamaño del botón
)
boton.place(x=485, y=490)  # posición absoluta (x, y)

# Iniciar ventana
ventana.mainloop()
