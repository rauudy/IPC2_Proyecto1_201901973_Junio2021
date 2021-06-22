# P R O Y E C T O 1

from tkinter import *
from dispersa import *
import os

raiz = Tk()
raiz.title('Blokker')
frame=Frame(raiz)
frame.pack()
frame.config(width=900, height=600)

m = Mdispersa()
matButt=[]


# -------------- Variables Tablero --------------------
clmas=StringVar()
fls=StringVar()

# ----------------- Pieza Jugador1 --------------------
fj1=StringVar()
cj1=StringVar()
colorj1=StringVar()

# ----------------- Pieza Jugador2 --------------------
fj2=StringVar()
cj2=StringVar()
colorj2=StringVar()

# ------------------ Tamaño Matriz --------------------
columnas=''
filas=''
grapCol=0
puntosJ1=1
puntosJ2=0

# --------------------- Imagenes ----------------------
  


# ---------------------------- Funciones ---------------------------------------

def extraerDimension():
    global columnas, filas, grapCol
    columnas = clmas.get()
    grapCol = int(columnas)
    filas = fls.get()
    print('Columnas: '+columnas)
    print('Filas: '+filas)

    matriz(filas,columnas)
    clmas.set('')
    fls.set('')
    #clmas.trace_vdelete()

def matriz(x,y):
    for posX in range(int(x)):
        for posY in range(int(y)):
            ids = Button(frame, bg='black', fg='white', width=2)
            ids.grid(row=posX+2 , column=posY+2)
  
def PngGraphiz(col):
    m.graphiz(col)  

def repHtml():
    m.imprimirHtml()
# ------------------ Insertar Judador1 --------------------
def extraerJ1():
    columnas = cj1.get()
    filas = fj1.get()
    clor = colorj1.get()

    insertarPieza(filas,columnas, clor)

    cj1.set('')
    fj1.set('')
# ------------------ Insertar Judador2 --------------------
def extraerJ2():
    columnas = cj2.get()
    filas = fj2.get()
    clor = colorj2.get()

    insertarPieza(filas,columnas, clor)
    cj2.set('')
    fj2.set('')

def movimiento():
    mov.set('Pieza puesta en' )

def puntaj1 ():
    global puntosJ1
    lblJ1P.set(str(puntosJ1))
    puntosJ1+=1


# ------------------ Insertar en Matriz --------------------
def insertarPieza(fila,columna,color):
    m.insertarM(fila,columna,color)

def imprimirNodos():
    m.recorrerFilas()

def mostrarInf():
    os.startfile("acerca.html")

def docmu():
    os.startfile('Documentacion-Proyecto1.pdf')

# -------------- Barra Herramientas --------------------
menu = Menu()
raiz.config(menu=menu)    

Report=Menu(menu, tearoff=0)
Ayuda=Menu(menu, tearoff=0)

menu.add_cascade(label='Reporte', menu=Report)
Report.add_command(label='HTML', command=lambda:repHtml)
Report.add_command(label='GRAPHIZ', command=lambda:PngGraphiz(grapCol))

menu.add_cascade(label='Ayuda', menu=Ayuda)
Ayuda.add_command(label='DOCUMENTACION', command=lambda:docmu)
Ayuda.add_command(label='ACERCA DE MI', command=lambda:mostrarInf)


# -------------------- Dimensiones de Tablero ----------------------------------

lblDimCol = Label(frame, text='No. Columnas')
lblDimCol.grid(row=0,column=22)

lblDimFil = Label(frame, text='No. Filas')
lblDimFil.grid(row=1,column=22)

txtDimCol = Entry(frame, width=3, textvariable=clmas)
txtDimCol.grid(row=0,column=23)

txtDimFil = Entry(frame, width=3, textvariable=fls)
txtDimFil.grid(row=1,column=23)

btnTablero = Button(frame, text='Crear \nTablero', command=extraerDimension)
btnTablero.grid(row=0,column=24, rowspan=2, columnspan=2)

# ---------------------- Informacion Jugadores --------------------------------


# -------------- Jugador1 --------------------
lblJ1 = Label(frame, text='Jugador1')
lblJ1.grid(row=3,column=22, columnspan=4)

lblJ1Puntos = Label(frame, text='Puntos:')
lblJ1Puntos.grid(row=4,column=22)

lblJ1P = Label(frame,width=1, bg='blue')
lblJ1P.grid(row=4,column=23)

lblJ1Color = Label(frame, text='Color:')
lblJ1Color.grid(row=4,column=24)

txtJ1Col = Entry(frame, width=7, textvariable=colorj1)
txtJ1Col.grid(row=4,column=25)

#btnJ1Col = Button(frame, text='Y', width=2, height=0)
#btnJ1Col.grid(row=5,column=24)

# -------------- Jugador2 --------------------
lblJ1 = Label(frame, text='Jugador2')
lblJ1.grid(row=5,column=22, columnspan=4)

lblJ1Puntos = Label(frame, text='Puntos:')
lblJ1Puntos.grid(row=6,column=22)

lblJ2P = Label(frame,width=1, bg='blue')
lblJ2P.grid(row=6,column=23)

lblJ2Color = Label(frame, text='Color:')
lblJ2Color.grid(row=6,column=24)

txtJ2Col = Entry(frame, width=7,textvariable=colorj2)
txtJ2Col.grid(row=6,column=25)

#btnJ2Col = Button(frame, text='Y', width=2, height=0)
#btnJ2Col.grid(row=9,column=13)
# ------------------------ Reporte -------------------------------------

mostarNodos = Button(frame, text='imprimir\nnodos',command=imprimirNodos )
mostarNodos.grid(row=20,column=22, columnspan=4)

mov = Label(frame, text='')
mov.grid(row=19,column=22, columnspan=4)

# ------------------------ INSERTAR PIEZAS -------------------------------------

lEle = Label(frame, text='Hola')
lEle.grid(row=8, column=22)

# -------------- Jugador1 -------------------- 
lblJ1_D = Label(frame, text='Jugador1')
lblJ1_D.grid(row=12,column=22, columnspan=4)

lblJ1_F = Label(frame, text='Fila')
lblJ1_F.grid(row=13,column=22)

lblJ1_C = Label(frame, text='Columna')
lblJ1_C.grid(row=14,column=22)

txtJ1_F = Entry(frame, width=2, textvariable=fj1)
txtJ1_F.grid(row=13,column=23)

txtJ1_C = Entry(frame, width=2, textvariable=cj1)
txtJ1_C.grid(row=14,column=23)

btnJ1_pieza = Button(frame, text='Poner', command=extraerJ1)
#btnJ1_pieza.config(command=puntaj1)
btnJ1_pieza.grid(row=13,column=24, rowspan=2, columnspan=2)

# -------------- Jugador2 --------------------
lblJ2_D = Label(frame, text='Jugador2')
lblJ2_D.grid(row=15,column=22, columnspan=4)

lblJ2_F = Label(frame, text='Fila')
lblJ2_F.grid(row=16,column=22)

lblJ2_C = Label(frame, text='Columna')
lblJ2_C.grid(row=17,column=22)

txtJ2_F = Entry(frame, width=2, textvariable=fj2)
txtJ2_F.grid(row=16,column=23)

txtJ2_C = Entry(frame, width=2, textvariable=cj2)
txtJ2_C.grid(row=17,column=23)

btnJ2_pieza = Button(frame, text='Poner', command=extraerJ2)
btnJ2_pieza.grid(row=16,column=24, rowspan=2, columnspan=2)


# ------------------------------- TIEMPO ---------------------------------------

raiz.mainloop()