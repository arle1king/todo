# -*- coding: utf-8 -*-
"""
Ejemplo Nivel 4: Visor de imágenes

Temas:

* Matrices

@author: Cupi2
"""
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def cargar_imagen(ruta_imagen: str)-> list:
    """ Carga la imagen que se encuentra en la ruta dada.
    Parámetros:
        ruta_imagen (str) Ruta donde se encuentra la imagen a cargar.
    Retorno:
        list: Matriz (M,N,3) con la imagen cargada.
    """

    imagen = mpimg.imread(ruta_imagen).tolist()
    return imagen

def visualizar_imagen(imagen: list)->None:
    """ Muestra la imagen recibida
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a visualizar.
    """
    plt.imshow(imagen)
    plt.show()

    return imagen


def reflejar_imagen(imagen: list)->list:
    """Refleja la imagen.
    Consiste en intercambiar las columnas enteras de la imagen, de las finales a la iniciales.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a reflejar.
    """
    return imagen


def binarizar_imagen(imagen: list, umbral: float)->list:
    """ Binariza la imagen.
    Consiste en llevar cada pixel de una imagen a negro o blanco.
    Para ello se requiere un umbral: si el promedio de los componentes RGB del pixel está por encima o igual se lleva a blanco y si está por debajo se lleva a negro.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a binarizar.
        umbral (float) Umbral de la binarización.
     """
    return imagen


