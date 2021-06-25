import numpy as np


def checklist(lst):
    elem = lst[0]
    resultado = True
    for i in range(1,len(lst)):
        if(lst[i] != elem):
            resultado = False
    return resultado


def tragaperras():
    opciones = ['ceraza', 'manzana', 'naranja', 'kiwi', 'melon']
    tirada = np.random.randint(0, len(opciones), size=len(opciones))
    print("El resultado de su tirada es: ")
    [print(opciones[i]) for i in tirada]
    resultado = checklist(tirada)
    print("Ha ganado el premio") if(resultado) else print("Mala suerte")


tragaperras()
