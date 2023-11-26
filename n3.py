
def son_anagramas(palabra1: str, palabra2: str)->bool:
    """ Anagramas
    Parámetros:
      palabra1 (str): Palabra 1
      palabra2 (str): Palabra 2
    Retorno:
      bool: True si las dos palabras son anagramas. False de lo contrario
    """
    contador=0
    i = 0
    while i < len(palabra1) :
        if palabra1[i] in palabra2:
            contador+=1
        i += 1
    if contador==len(palabra2):
        return True
    else:
        return False

def traducir_a_pig_latin(texto: str)->str:
    """ Pig Latin
    Parámetros:
      texto (str): Texto (cadena de caracteres) a traducir al Pig Latin. Consiste solamente de palabras en
                   minúscula, separadas por espacios.
    Retorno:
      str: Texto con las palabras de la cadena original traducidas a Pig Latin, separadas por espacios.
    """
    lista=texto.split(" ")
    oracion=""
    i = 0
    while i < len(lista) :
        palabra=lista[i]
        if ord(palabra[0]) == 97 or ord(palabra[0]) == 101 or ord(palabra[0]) ==105 or ord(palabra[0]) ==111 or ord(palabra[0]) ==117:
            if oracion=="":
                oracion+=lista[i]+"way"
            else:
                oracion+=" "+lista[i]+"way"
        elif not not palabra in ("a" or "e" or "i" or "o" or "u"):
            if oracion=="":
                oracion+=lista[i]
            else:
                oracion+=" "+lista[i]
        else:
            decision=False
            texto=""
            o=1
            while decision==False:
                if palabra[o]=="a" or palabra[o]=="e" or palabra[o]=="i" or palabra[o]=="o" or palabra[o]=="u":
                    decision=True
                    texto+=palabra[o:]+palabra[:o]+"ay"
                else:
                    o+=1
            if oracion=="":
                oracion+=texto
            else:
                oracion+=" "+texto
        i+=1
    return oracion

def comprar_jugador(jugadores: list, monedas: int)->str:
    """ Fifa Ultimate Team
    Parámetros:
      jugadores (list): Una lista de diccionarios que representan a los jugadores de FUT que podrían ser
                        comprados por Juan.  Cada diccionario tiene las siguientes llaves: "nombre": (str)
                        el nombre del jugador. "precio": (int), un entero que representa la cantidad de
                        monedas que vale el jugador. "media" (int): un entero mayor o igual a 50 y menor o
                        igual a 99, que representa la ponderación general del jugador.
      monedas (int): La cantidad de monedas FIFA de las que dispone Juan para comprar su jugador.
    Retorno:
      str: La función retorna el nombre del jugador comprado por Juan. Si las monedas no son suficientes para
           comprar algún jugador, retorna None.
    """
    valor=0
    max_medias=0
    jugador=""
    for cada_jugador in jugadores:
        nombre=cada_jugador["nombre"]
        precio=cada_jugador["precio"]
        media=cada_jugador["media"]
        if max_medias < media:
            if precio <= monedas:
                max_medias=media
                jugador=nombre
                valor=precio
        if max_medias == media:
            if precio < valor:
                max_medias=media
                jugador=nombre
                valor=precio
    if max_medias==0:
        jugador=None
    return jugador

def escala_musical(notas: list)->str:
    """ Escalas musicales
    Parámetros:
      notas (list): Lista de enteros que representan notas musicales en Hertz
    Retorno:
      str: Mensaje que indique si encontró notas similares: "No hay coincidencia", "Hay una nota idéntica" o
           "Hay una nota en otra octava". En caso que haya idénticas y en otra octava, primará retornar el
           mensaje que informe sobre la idéntica.
    """
    respuesta=""
    o=0                
    while o<len(notas) :
        nota=notas[o]
        if nota==440:
            if respuesta=="" or respuesta=="Hay una nota idéntica" or respuesta=="No hay coincidencia":
                respuesta="Hay una nota idéntica"
            elif respuesta=="Hay una nota en otra octava":
                respuesta="Hay una nota idéntica"+" "+"Hay una nota en otra octava"
                
            else:
                respuesta+="Hay una nota en otra octava"
                    
        elif nota<440:
            if nota*(8 or 4 or 2)== 440:
                if respuesta=="" or respuesta=="Hay una nota en otra octava" or respuesta=="No hay coincidencia":
                    respuesta="Hay una nota en otra octava"
                else:
                    respuesta+="Hay una nota en otra octava"
                    
            else:
                respuesta="No hay coincidencia"
        elif nota%440==0:
                if respuesta=="" or respuesta=="Hay una nota en otra octava" or respuesta=="No hay coincidencia":
                    respuesta="Hay una nota en otra octava"
                else:
                    respuesta+="Hay una nota en otra octava"
                    
        else:
            if respuesta=="Hay una nota idéntica" or respuesta=="Hay una nota en otra octava" or respuesta=="No hay coincidencia":
                respuesta
            else:
                respuesta="No hay coincidencia"
        o+=1
    
    return respuesta

def palabras_intercaladas(cadena1: str, cadena2: str)->str:
    """ Palabras intercaladas
    Parámetros:
      cadena1 (str): Primera cadena de la cual se desean intercalar sus palabras.
      cadena2 (str): Segunda cadena de la cual se desean intercalar sus palabras.
    Retorno:
      str: Cadena con las palabras intercaladas de las dos cadenas de entrada.
    """
    lista1=cadena1.split()
    lista2=cadena2.split()
    oracion_lista=""
    i = 0
    while i < len(lista1):
        if oracion_lista=="":
            oracion_lista+=lista1[i]+" "+lista2[i]
        else:
            oracion_lista+=" "+lista1[i]+" "+lista2[i]
        i+=1
    return oracion_lista

def descifrar_codigo_cesar(texto_cifrado: str, corrimiento: int)->str:
    """ Descifrar código César
    Parámetros:
      texto_cifrado (str): El texto cifrado que se quiere descifrar. Puede incluir minúsculas, mayúsculas,
                           espacios y otros caracteres especiales. Sólo tendrá letras del alfabeto inglés.
      corrimiento (int): El corrimiento (cantidad de lugares que se corre una letra) que se usó para generar
                         el cifrado, y por ende debe usarse para descrifar el mensaje
    Retorno:
      str: La cadena descifrada, incluyendo espacios y caracteres especiales que tenía la original.
    """
    texto=""
    for caracter in texto_cifrado:
        if ord(caracter) in range(97,123):
            if ord(caracter)-corrimiento<97:
                texto+=chr(ord(caracter)-corrimiento+26)
            else:
                texto+=chr(ord(caracter)-corrimiento)
        elif ord(caracter) in range(65,91):
            if ord(caracter)-corrimiento<65:
                texto+=chr(ord(caracter)-corrimiento+26)
            else:
                texto+=chr(ord(caracter)-corrimiento)
        else:
            texto+=caracter
    return texto