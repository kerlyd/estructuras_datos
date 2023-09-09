class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.top = None

    def apilar(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.top
        self.top = nuevo_nodo

    def desapilar(self):
        if self.top is not None:
            valor = self.top.valor
            self.top = self.top.siguiente
            return valor
        else:
            return None

    def recorrido(self):
        nodo_actual = self.top
        while nodo_actual is not None:
            print(nodo_actual.valor)
            nodo_actual = nodo_actual.siguiente

    def eliminar_nodo_interno(self, valor):
        nodo_actual = self.top
        nodo_anterior = None

        while nodo_actual is not None:
            if nodo_actual.valor == valor:
                if nodo_anterior is not None:
                    nodo_anterior.siguiente = nodo_actual.siguiente
                else:
                    self.top = nodo_actual.siguiente
                return
            nodo_anterior = nodo_actual
            nodo_actual = nodo_actual.siguiente

if __name__ == "__main__":
    pila = Pila()
    pila.apilar(1)
    pila.apilar(2)
    pila.apilar(3)
    pila.apilar(4)
    pila.apilar(5)

    print("Pila original:")
    pila.recorrido()

    print("\nDesapilando el valor 4:")
    pila.eliminar_nodo_interno(4)
    pila.recorrido()

    print("\nDesapilando el valor 2:")
    pila.eliminar_nodo_interno(2)
    pila.recorrido()
