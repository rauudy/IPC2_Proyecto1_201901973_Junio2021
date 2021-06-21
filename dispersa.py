from nodos import Nodo,nodoEncabezado
from encabezado import listaEncabezado

class Mdispersa:
    def __init__(self):
        self.eFilas = listaEncabezado()
        self.eColumnas = listaEncabezado()

    def insertarM(self, fila, columna, valor):
        nuevo = Nodo(fila, columna, valor)

        eFila = self.eFilas.getEncabezado(fila) #Filas
        if(eFila == None):
            eFila = nodoEncabezado(fila)
            self.eFilas.setEncabezado(eFila)
            eFila.accesoNodo = nuevo
        else:
            if(nuevo.columna < eFila.accesoNodo.columna):
                nuevo.derecha = eFila.accesoNodo
                eFila.accesoNodo.izquierda = nuevo
                eFila.accesoNodo = nuevo
            else:
                actual=eFila.accesoNodo
                while(actual.derecha != None):
                    if(nuevo.columna < actual.derecha.columna):
                        nuevo.derecha=actual.derecha
                        actual.derecha.izquierda=nuevo
                        nuevo.izquierda=actual
                        actual.derecha=nuevo
                        break
                    actual=actual.derecha

                if(actual.derecha == None):
                    actual.derecha=nuevo
                    nuevo.izquierda=actual

        eColumna = self.eColumnas.getEncabezado(columna)  # Columnas
        if (eColumna == None):
            eColumna = nodoEncabezado(columna)
            self.eColumnas.setEncabezado(eColumna)
            eColumna.accesoNodo = nuevo
        else:
            if (nuevo.fila < eColumna.accesoNodo.fila):
                nuevo.abajo = eColumna.accesoNodo
                eColumna.accesoNodo.arriba = nuevo
                eColumna.accesoNodo = nuevo
            else:
                actual = eColumna.accesoNodo
                while (actual.abajo != None):
                    if (nuevo.fila < actual.abajo.fila):
                        nuevo.abajo = actual.abajo
                        actual.abajo.arriba = nuevo
                        nuevo.arriba = actual
                        actual.abajo = nuevo
                        break
                    actual = actual.abajo

                if (actual.abajo == None):
                    actual.abajo = nuevo
                    nuevo.arriba = actual

    def recorrerFilas(self):
        eFila=self.eFilas.primero
        print("\nRecorrido por filas\n")

        while(eFila != None):
            actual = eFila.accesoNodo
            while(actual != None):
                print(actual.valor + " ",end="")
                print(" Fila: " + str(actual.fila),end="")
                print("| Columna: " + str(actual.columna),end="")
                print()
                actual=actual.derecha
            print("")
            eFila=eFila.siguiente



    def graphiz(self, columnas):
        cont = 0

        f = open('graphizP1.dot', 'w', encoding='utf-8')
        f.write("digraph proyec{\n")
        f.write('tabla[shape = plaintext, fontsize = 10, label = <\n')
        f.write('<TABLE BORDER = " 0" border  = "0" cellborder = "0">\n"')
        
        efila = self.eFilas.primero
        f.write('<tr>')
        for x in range(int(columnas)+1):
            f.write('<td BGCOLOR="green">' + str(x) + '</td>')
        f.write('</tr>')

        while (efila != None):
            ac = efila.accesoNodo
            f.write('<tr>')

            while (ac != None):
                if cont == 0:
                    f.write('<td BGCOLOR="red">'+str(ac.fila)+'</td>')
                    cont= cont+1
                f.write('<td>'+ str(ac.valor)+'</td>')
                if (efila.siguiente != None or ac.derecha != None):
                    pass
                ac = ac.derecha
            f.write('</tr>')
            cont =0
            print("")
            efila = efila.siguiente
        f.write('</TABLE>\n')
        f.write('>];')
        f.write('}')
        f.close()
        #os.system('dot -Tpng grafica.dot -o S.png')


#m = Mdispersa()

# Parametros Fila, Columna, Valor
#m.insertarM('1','0', "adolfo")
#m.insertarM('2','1', "brandon")
#m.insertarM(0,1, "daniel")
#m.insertarM(1,2, "eduardo")
#m.insertarM(0,2, "diego")
#m.insertarM(0,4, "javier")

#m.recorrerColumnas()
#m.recorrerFilas()