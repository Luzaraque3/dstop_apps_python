# Se importa la libreria con toda sus funciones
from tkinter import *

# se declara una vvariable llamada ventana principal, que tiene las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Bandera de Suiza")
# tamaño de la ventana
ventana_principal.geometry("500x500")

# desabilitar boton de maxinizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="coral")

#----------------------------
#frame rojo
#----------------------------
frame_rojo = Frame(ventana_principal)
frame_rojo.config (bg="red3", width=500, height=500)
frame_rojo.place (x=0, y=0)

#----------------------------
#frame blanco 1
#----------------------------
frame_blanco1 = Frame(ventana_principal)
frame_blanco1.config (bg="white", width=100, height=300)
frame_blanco1.place (x=200, y=100)

#----------------------------
#frame blanco 2
#----------------------------
frame_blanco2 = Frame(ventana_principal)
frame_blanco2.config (bg="white", width=300, height=100)
frame_blanco2.place (x=100, y=200)


# run
ventana_principal.mainloop()