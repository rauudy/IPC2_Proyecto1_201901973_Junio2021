from nodos import Nodo, nodoEncabezado

class listaEncabezado: #Lista doblemente enlazada
    def __init__(self, primero=None):
        self.primero = primero

    def setEncabezado(self, nuevo): #Insertar nodo cabecera
        if self.primero == None:
            self.primero = nuevo
        elif nuevo.id < self.primero.id: #validar si el nuevo valor en menor que la cabeza primero
            nuevo.siguiente = self.primero
            self.primero.anterior = nuevo
            self.primero = nuevo
        else:
            actual = self.primero #para recorrer
            while actual.siguiente != None: #insertar en medio, 2
                if nuevo.id < actual.siguiente.id:
                    nuevo.siguiente = actual.siguiente
                    actual.siguiente.anterior = nuevo
                    nuevo.anterior = actual
                    actual.siguiente = nuevo
                    break
                actual = actual.siguiente

            if actual.siguiente == None: #insertar al final nodo 4
                actual.siguiente = nuevo
                nuevo.anterior = actual
    
    def getEncabezado(self,id): #como busqeuda
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None


