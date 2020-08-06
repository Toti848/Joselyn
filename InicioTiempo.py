import tkinter as tk


PRECISION = 10 # Milisegundos entre actualizaciones


def iniciotiempo():
    global cronometrando
    global tiempo

    if not cronometrando:
        return

    tiempo = tiempo + PRECISION
    segundos, milisegundos = divmod(tiempo, 1000)
    minutos, segundos = divmod(segundos, 60)

    pantalla_label.config(text="{:02}:{:02}:{:03}".format(minutos, segundos, milisegundos))
    pantalla_label.after(PRECISION, iniciotiempo)


def comenzar():
    global cronometrando

    if cronometrando:
        cronometrando = False
        boton_comenzar.config(text="Reanudar")
    else:
        cronometrando = True
        boton_comenzar.config(text="Pausar")
        iniciotiempo()


def finalizar():
    global cronometrando
    global tiempo

    cronometrando = False
    tiempo = 0
    boton_comenzar.config(text="Comenzar")
    pantalla_label.config(text="00:00:00")


pantalla = tk.Tk()
pantalla.title("Cronómetro")
pantalla.resizable(0, 0)

cronometrando = False
tiempo = 0

frame = tk.Frame(pantalla, width=312, height=300, bg="red")
frame.pack()

boton_comenzar = tk.Button(frame,
                           text="Comenzar",
                           font=("bold", 20),
                           width=19,
                           command=comenzar
                           )
boton_comenzar.place(x=0, y=0)

boton_finalizar = tk.Button(frame,
                            text="Finalizar",
                            font=("bold", 20),
                            width=19,
                            command=finalizar
                            )
boton_finalizar.place(x=0, y=245)

pantalla_label = tk.Label(frame, font=("bold", 50), text="00:00:00")
pantalla_label.place(x=25, y=100)

pantalla.mainloop()