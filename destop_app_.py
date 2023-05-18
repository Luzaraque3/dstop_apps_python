#---------------------------------------------------------------------------------------------------------------
#Desktop
#Se importa Tkinter

from tkinter import *

#---------------------------------------------------------------------------------------------------------------
#Funciones App
#Ventana Principal  App
#---------------------------------------------------------------------------------------------------------------

#Se Aclara Una Variable Llamada Ventana_Principal
ventana_principal = Tk()

#Titulo

ventana_principal.title("MonekyLand")
#Tamaño
ventana_principal.geometry("500x500")
#NoMaximizar? pipipipi
ventana_principal.resizable(False,False)
#Color
ventana_principal.config(bg="darkorchid")
#Frame Extra
frame_Amarillo = Frame (ventana_principal)
frame_Amarillo.config(bg="yellow", width=500, height=250,)
frame_Amarillo.place(x=0, y=0)

frame_Amarillo = Frame (ventana_principal)
frame_Amarillo.config(bg="blue", width=500, height=125,)
frame_Amarillo.place(x=0, y=250)

frame_Amarillo = Frame (ventana_principal)
frame_Amarillo.config(bg="red", width=500, height=125,)
frame_Amarillo.place(x=0, y=370)


#Run
ventana_principal.mainloop()