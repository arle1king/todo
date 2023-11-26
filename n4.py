import random

def encontrar_manzana(barrio: list)->tuple:
    """ Barrio_Peligroso
    Parámetros:
      barrio (list): Matriz de enteros que representa el barrio peligroso a intervenir.
    Retorno:
      tuple: Tupla con las coordenadas en las cuales se debe instalar la estación de policía.
    """
    max_barri=0
    cordenada=[0,0]
    for i in range(0,len(barrio)):
        for j in range(0,len(barrio[0])):
            max_bari=0
            for b in range(i-1,i+2):
                if b>=0 and b<len(barrio):    
                    for y in range(j-1,j+2):
                        if  y>=0 and y<len(barrio[0]) :
                            v=barrio[b][y]
                            max_bari+=v
            max_bari=max_bari-barrio[i][j]
            if max_bari>max_barri:
                max_barri=max_bari
                cordenada[0]=i
                cordenada[1]=j
            elif max_bari==max_barri:
                k=((j)**2+(i)**2)**0.5
                r=((cordenada[0])**2+(cordenada[1])**2)**0.5
                if r>k:
                    cordenada[0]=i
                    cordenada[1]=j
    return tuple(cordenada)

def guardar_colores(x: int, caja: list)->list:
    """ Empacando colores
    Parámetros:
      x (int): La cantidad de colores a guardar.
      caja (list): Una matriz con el estado inicial de la caja. Cada entrada de la matriz es un diccionario
                   con las llaves "capacidad_maxima" y "capacidad_actual", que representan el estado actual
                   de esa posición en la caja.
    Retorno:
      list: Una matriz con el estado de la caja después de guardar los colores. Cada entrada de la matriz es un
            diccionario con las llaves "capacidad_maxima" y "capacidad_actual"  que representan el estado final
            de esa posición en la caja.
    """
    no_hay=False
    while no_hay==False:
        for i in range(0,len(caja)):
            for j in range(0,len(caja[0])):
                v=caja[i][j]
                capacidad=v["capacidad_maxima"]-v["capacidad_actual"]
                if x>capacidad:
                    x=x-capacidad
                    v["capacidad_actual"]+=capacidad
                    caja[i][j]=v
                else:
                    v["capacidad_actual"]+=x
                    x=0
                    caja[i][j]=v
                    no_hay=True
        if x!=0:
            return None
    return caja

def analizar_texto(texto: str, caracteres_permitidos: list)->dict:
    """ Analizador léxico
    Parámetros:
      texto (str): La cadena de caracteres que se debe analizar
      caracteres_permitidos (list): Una lista de caracteres que pueden hacer partede las palabras que se van
                                    a analizar
    Retorno:
      dict: Un diccionario donde las llaves son todas las palabras que aparecen en el texto y los valores son
            tuplas con tres números enteros.
    """
    dicio={} 
    if texto=="":
        return dicio
    text_com=""
    if texto[0]!=" ":
        text_com+=" "
    for i in range(0,len(texto)):
        if not texto[i] in caracteres_permitidos:
            text_com+=" "
        else:
            text_com+=texto[i].lower()
        if i==len(texto)-1:
            text_com+=" "
    lis_tex=text_com.split(" ")
    for i in range(0,len(lis_tex)):
        contador=lis_tex.count(lis_tex[i])
        cantidad=text_com.find(" "+lis_tex[i]+" ")
        if contador>2:
            cont = 1
            lugar=cantidad
            while contador>cont:
                lugar=text_com.find(" "+lis_tex[i]+" ",lugar+1)
                cont += 1
            if cont==contador:
                dicio[lis_tex[i].lower()]=contador,cantidad,lugar
        elif contador>1:
            dicio[lis_tex[i].lower()]=contador,cantidad,text_com.find(" "+lis_tex[i]+" ",cantidad+1)
        else:
            dicio[lis_tex[i].lower()]=contador,cantidad,cantidad
    dicio.pop("")
    return dicio

def encontrar_primos(mapa: list)->list:
    """ Buscando primos
    Parámetros:
      mapa (list): Matriz que representa cada una de las casillas del mapa del bósque. Cada uno de sus
                   valores es un número entero entre 1 y 100.
    Retorno:
      list: Una lista ordenada con los números que son familiares de Dos y que se encontraron en el bosque. La
            lista puede tener números repetidos.
    """
    lista_fami=[]
    for i in range(0,len(mapa)):
        for j in range(0,len(mapa[0])):
            v=mapa[i][j]
            rest=True
            if v==1:
                rest=False
            for n in range(2,v):
                if v%n==0:
                    rest=False
            if rest==True:
                lista_fami.append(v)
    lista_fami.sort()
    return lista_fami

def res_repartir_cartas(num_jugadores:int, num_mazos:int):
    valores = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    multi=[]
    for x in range(0,num_mazos):
        multi+=valores.values()
    random.shuffle(multi)
    cartas=len(multi)//num_jugadores
    print(cartas)
    for jugador in range(1,num_jugadores+1):
        inicio=(jugador-1)*cartas
        fin=jugador*cartas
        mano_jugador=multi[inicio:fin]
    return mano_jugador

print(res_repartir_cartas(3,2))

def poema():
    i=0
    while i in range(1000):
        print("Te dedico un poema... quebonitos ojos tienes")
        i += 1
    pass

poema()