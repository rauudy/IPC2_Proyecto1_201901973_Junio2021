class Nodo: #TDA NODO, lo que esta como pieza
    def __init__(self, fila, columna, valor):
        self.valor = valor

        self.fila = fila
        self.columna = columna
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None

class nodoEncabezado: #NODO de encabezado
    def __init__(self,id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.accesoNodo = None
