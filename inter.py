from tkinter import *

raiz = Tk()
raiz.title('Proyecto 1')
frame=Frame(raiz)
frame.pack()
frame.config(width=900, height=600)

clmas=StringVar()
fls=StringVar()

columnas=''
filas=''

# ---------------------------- Funciones ---------------------------------------

def extraerDimension():
    global columnas, filas
    columnas = clmas.get()
    filas = fls.get()
    print('Columnas: '+columnas)
    print('Filas: '+filas)

    matriz(filas,columnas)

def matriz(x,y):
    for posX in range(int(x)):
        for posY in range(int(y)):
            btn = Button(frame,text= str(posX+1) + "," + str(posY+1))
            btn.grid(row=posX+5 , column=posY+4)
        


# -------------------- Dimensiones de Tablero ----------------------------------

lblDimCol = Label(frame, text='No. Columnas')
lblDimCol.grid(row=0,column=0)

lblDimFil = Label(frame, text='No. Filas')
lblDimFil.grid(row=1,column=0)

txtDimCol = Entry(frame, width=3, textvariable=clmas)
txtDimCol.grid(row=0,column=1)

txtDimFil = Entry(frame, width=3, textvariable=fls)
txtDimFil.grid(row=1,column=1)

btnTablero = Button(frame, text='Crear \nTablero', command=extraerDimension)
btnTablero.grid(row=0,column=3)

# ---------------------- Informacion Jugadores --------------------------------

# -------------- Jugador1 --------------------
lblJ1 = Label(frame, text='Jugador1')
lblJ1.grid(row=0,column=5)

lblJ1Puntos = Label(frame, text='Puntos:')
lblJ1Puntos.grid(row=1,column=4)

lblJ1P = Label(frame,width=1, bg='blue')
lblJ1P.grid(row=1,column=5)

lblJ1Color = Label(frame, text='Color:')
lblJ1Color.grid(row=1,column=6)

txtJ1Col = Entry(frame, width=7)
txtJ1Col.grid(row=1,column=7)

btnJ1Col = Button(frame, text='Y', width=2, height=0)
btnJ1Col.grid(row=1,column=8)

# -------------- Jugador2 --------------------
lblJ1 = Label(frame, text='Jugador2')
lblJ1.grid(row=0,column=10)

lblJ1Puntos = Label(frame, text='Puntos:')
lblJ1Puntos.grid(row=1,column=9)

lblJ2P = Label(frame,width=1, bg='blue')
lblJ2P.grid(row=1,column=10)

lblJ2Color = Label(frame, text='Color:')
lblJ2Color.grid(row=1,column=11)

txtJ2Col = Entry(frame, width=7)
txtJ2Col.grid(row=1,column=12)

btnJ2Col = Button(frame, text='Y', width=2, height=0)
btnJ2Col.grid(row=1,column=13)

# ------------------------ INSERTAR PIEZAS -------------------------------------

# -------------- Jugador1 -------------------- 
lblJ1_D = Label(frame, text='Jugador1')
lblJ1_D.grid(row=4,column=17)

lblJ1_F = Label(frame, text='Fila')
lblJ1_F.grid(row=5,column=17)

lblJ1_C = Label(frame, text='Columna')
lblJ1_C.grid(row=6,column=17)

txtJ1_F = Entry(frame, width=2)
txtJ1_F.grid(row=5,column=18)

txtJ1_C = Entry(frame, width=2)
txtJ1_C.grid(row=6,column=18)

btnJ1_pieza = Button(frame, text='Poner', height=2)
btnJ1_pieza.grid(row=5,column=19)

# -------------- Jugador2 --------------------
lblJ2_D = Label(frame, text='Jugador2')
lblJ2_D.grid(row=8,column=17)

lblJ2_F = Label(frame, text='Fila')
lblJ2_F.grid(row=9,column=17)

lblJ2_C = Label(frame, text='Columna')
lblJ2_C.grid(row=10,column=17)

txtJ2_F = Entry(frame, width=2)
txtJ2_F.grid(row=9,column=18)

txtJ2_C = Entry(frame, width=2)
txtJ2_C.grid(row=10,column=18)

btnJ2_pieza = Button(frame, text='Poner', height=2)
btnJ2_pieza.grid(row=9,column=19)


# ------------------------------- TIEMPO ---------------------------------------

raiz.mainloop()