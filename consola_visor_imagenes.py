# -*- coding: utf-8 -*-
"""
Ejemplo Nivel 4: Visor de imágenes

Temas:

* Matrices

@author: Cupi2
"""
import visor_imagenes


def imprimir_menu_principal():
    """ Imprime los items del menú principal de la aplicación
    """
    print("\n          Visor de imágenes\n")
    print("(1) Cargar imagen")
    print("(2) Binarizar")
    print("(3) Reflejar")
    print("(4) Salir")


def cargar_imagen()->list:
    """ Muestra las opciones para cargar una imagen y carga la imagen seleccionada por el usuario.
    """
    ruta = input("Ingrese el nombre del archivo que contiene la imagen: ")
    imagen = visor_imagenes.cargar_imagen(ruta)
    visor_imagenes.visualizar_imagen(imagen)
    return imagen


def ejecutar_binarizar_imagen(imagen: list)->list:
    """ Pide al usuario el umbral deseado y binariza la imagen recibida por parámetro.
    Parámetros:
        imagen (list) Matriz (M,N,3) con la imagen a binarizar.
    """
    umbral = float(input("Ingrese el umbral (valor entre 0 y 1):"))
    print("Calculando imagen...")
    imagen = visor_imagenes.binarizar_imagen(imagen, umbral)
    visor_imagenes.visualizar_imagen(imagen)
    return imagen

def ejecutar_reflejar_imagen(imagen: list)->list:
    print("Calculando imagen...")
    imagen = visor_imagenes.reflejar_imagen(imagen)
    visor_imagenes.visualizar_imagen(imagen)
    return imagen

salir = False
while(not salir):
    imprimir_menu_principal()
    opcion = int(input("Ingrese la opción deseada: "))
    
    if opcion == 1:
        imagen = cargar_imagen()
    elif opcion == 2:
        imagen = ejecutar_binarizar_imagen(imagen)
    elif opcion == 3:
        imagen = ejecutar_reflejar_imagen(imagen)
    elif opcion == 4:
        salir = True
    else:
        print("El valor ingresado no es válido.")
