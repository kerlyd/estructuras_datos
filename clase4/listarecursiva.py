import random

def crear_lista_recursiva(num_nodos, lista=None):
    if lista is None:
        lista = []

    if num_nodos > 0:
        numero_aleatorio = random.randint(0, 10)
        lista.append(numero_aleatorio)
        return crear_lista_recursiva(num_nodos - 1, lista)
    else:
        return lista

num_nodos = int(input("Ingrese el número de nodos a crear: "))
lista_generada = crear_lista_recursiva(num_nodos)
print("Lista generada:", lista_generada)
