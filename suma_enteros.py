from tkinter import *
from tkinter import messagebox

#-------------------------
# funciones de la app
#-------------------------

# sumar
def calcular():
    messagebox.showinfo("Mini calculadora 1.0", "Las operaciones han sido realizadas")
    s = int(x.get()) + int(y.get())
    r = int(x.get()) - int(y.get())
    m = int(x.get()) * int(y.get())
    d = int(x.get()) / int(y.get())
    de = int(x.get()) // int(y.get())
    mod = int(x.get()) % int(y.get())
    p = int(x.get()) ** int(y.get())
    t_resultados.insert(INSERT, f"{int(x.get())} + {int(y.get())} = {s}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} - {int(y.get())} = {r}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} * {int(y.get())} = {m}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} / {int(y.get())} = {d}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} // {int(y.get())} = {de}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} % {int(y.get())} = {mod}")
    t_resultados.insert(INSERT, f"\n{int(x.get())} ** {int(y.get())} = {p}")

# borrar
def borrar():
    messagebox.showinfo("Mini calculadora 1.0", "Los datos seran borrados")
    x.set("")
    y.set("")
    t_resultados.delete("1.0","end")

# salir
def salir():
    messagebox.showinfo("Mini calculadora 1.0", "La app se va a cerrar")
    ventana_principal.destroy()

# Bandera De España
ventana_principal = Tk()

# ventana
ventana_principal.title("Mini calculadora")
ventana_principal.geometry("500x500")
ventana_principal.resizable(False, False)
ventana_principal.config(bg="blue")
#-------------------------
# variables globales
#-------------------------
x = StringVar()
y = StringVar()

# frame entrada
Frame_entrada = Frame(ventana_principal)
Frame_entrada.config(bg="white", width=480, height=180)
Frame_entrada.place(x=10, y=10)

# logo de la app
logo = PhotoImage(file="img/escudo_colegio.png")
lb_logo = Label(Frame_entrada, image=logo, bg="white")
lb_logo.place(x=70, y=40)

# titulo de la app
titulo = Label(Frame_entrada, text="Minicalculadora 1.0")
titulo.config(bg="white", fg="blue", font=("Arial", 18))
titulo.place(x=240, y=10)

# etiqueta para valor de x
lb_x = Label(Frame_entrada, text= "x = ")
lb_x.config(bg = "white", fg ="blue", font=("Helventica", 18))
lb_x.place(x=240, y=60)

# caja de texto para valor x
Entry_x =Entry(Frame_entrada, textvariable=x)
Entry_x.config(bg="white", fg="blue", font=("Times New Roman",18), widt=6)
Entry_x.focus_set()
Entry_x.place(x=290, y=60)

# etiqueta para valor de y
lb_y = Label(Frame_entrada, text = "Y = ")
lb_y.config(bg = "white", fg ="blue", font=("Helvetica", 18))
lb_y.place(x=240, y=120)

# caja de texto para valor y
Entry_y =Entry(Frame_entrada, textvariable=y)
Entry_y.config(bg="white", fg="blue", font=("Times New Roman",18), width=6)
Entry_y.place(x=290, y=120)

# frame operaciones
Frame_calcular = Frame(ventana_principal)
Frame_calcular.config(bg="white", width=480, height=100)
Frame_calcular.place(x=10, y=200)

# boton para calcular
bt_calcular = Button(Frame_calcular,text="Calcular", command=calcular)
bt_calcular.place(x=45, y=35, width=100, height=30)

# boton para borrar
bt_borrar = Button(Frame_calcular, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=35, width=100, height=30)

# boton para salir
bt_salir = Button(Frame_calcular, text="Salir", command=salir)
bt_salir.place(x=335, y=35, width=100, height=30)

# frame resultados
Frame_resultados = Frame(ventana_principal)
Frame_resultados.config(bg="white", width=480, height=180)
Frame_resultados.place(x=10, y=310)

# area de texto para los resultados
t_resultados = Text(Frame_resultados)
t_resultados.config(bg="black", fg="green yellow", font=("Courier", 18))
t_resultados.place(x=10, y=10, width=460, height=160)


# run
ventana_principal.mainloop()