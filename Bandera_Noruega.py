# Se importa la libreria con toda sus funciones
from tkinter import *

# se declara una vvariable llamada ventana principal, que tiene las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Bandera de Noruega")
# tamaño de la ventana
ventana_principal.geometry("600x600")

# desabilitar boton de maxinizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="coral")

#----------------------------
#frame rojo
#----------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config (bg="red3", width=600, height=600)
frame_rojo.place (x=0, y=0)

#----------------------------
#frame azul
#----------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config (bg="navy", width=50, height=600)
frame_azul.place (x=200, y=0)

#----------------------------
#frame azul
#----------------------------
frame_azul = Frame(ventana_principal)
frame_azul.config (bg="navy", width=600, height=50)
frame_azul.place (x=0, y=300)

#----------------------------
#frame blanco
#----------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config (bg="white", width=25, height=600)
frame_blanco.place (x=175, y=350)

#----------------------------
#frame blanco
#----------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config (bg="white", width=200, height=25)
frame_blanco.place (x=0, y=275)

#----------------------------
#frame blanco
#----------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config (bg="white", width=200, height=25)
frame_blanco.place (x=0, y=350)

#----------------------------
#frame blanco
#----------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config (bg="white", width=600, height=25)
frame_blanco.place (x=250, y=275)

#----------------------------
#frame blanco
#----------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config (bg="white", width=600, height=25)
frame_blanco.place (x=250, y=350)

#----------------------------
#frame blanco
#----------------------------
frame_blanco = Frame(ventana_principal)
frame_blanco.config (bg="white", width=25, height=600)
frame_blanco.place (x=250, y=350)

# run
ventana_principal.mainloop()