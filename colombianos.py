
def carga_de_datos(nombre_del_archivo: str)->dict:
    colombianos = {}
    archivo = open(nombre_del_archivo)
    encabesado = archivo.readline().split(",")
    linea = archivo.readline()
    while len(linea)>0:
        lista=[]
        datos = linea.split(",")
        ocupacion = datos[4]
        colombiano = {}
        colombiano[encabesado[0]] = datos[0]
        colombiano[encabesado[1]] = datos[1]
        colombiano[encabesado[2]] = int(datos[2])
        colombiano[encabesado[3]] = int(datos[3])
        colombiano[encabesado[5]] = datos[5]
        colombiano[encabesado[6][:-1]] = int(datos[6][:-1])
        lista.append(colombiano)
        if ocupacion in colombianos:
            lis=colombianos[ocupacion]
            lis.append(colombiano)
            colombianos[ocupacion]=lis
        else:
            colombianos[ocupacion]=lista
                    
        linea = archivo.readline()
    archivo.close()
    return colombianos
#funcion1=carga_de_datos("colombianos.csv")

def mayor_lectores(colombianos: dict) -> str:
    lectores=0
    nombre_lect=""
    for cada_ocu in colombianos:
        lis_colom=colombianos[cada_ocu]
        i=0
        while len(lis_colom)>i:
            colombiano=lis_colom[i]
            nombre=colombiano["nombre"]
            lectore=colombiano["numero_lectores"]
            if lectore>lectores:
                lectores=lectore
                nombre_lect=nombre
            i+=1
    return nombre_lect

def hay_3_colombianos(colombianos: dict,ocupación: str,genero: str,numero_lect: int) -> bool:
    lectores=0
    si_hay=False
    lis_colom=colombianos[ocupación]
    i=0
    while len(lis_colom)>i and si_hay==False:
        colombiano=lis_colom[i]
        lectore=colombiano["numero_lectores"]
        if lectore>numero_lect:
            if genero==colombiano["genero"]:
                lectores+=1
        if lectores>=3:
            si_hay=True
        i+=1
    return si_hay

def promedio_lectores(colombianos: dict,ocupacion: str) -> float:
    lis_colom=colombianos[ocupacion]
    i=0
    sumatoria=0
    while len(lis_colom)>i:
        colombiano=lis_colom[i]
        sumatoria+=colombiano["numero_lectores"]
        i+=1
    respuesta=round(sumatoria/i,2)
    return respuesta

def mayor_rating(colombianos: dict) -> str:
    max_ocupa=""
    max_prome=0
    for cada_ocu in colombianos:
        promedio=promedio_lectores(colombianos,cada_ocu)
        if promedio>max_prome:
            max_prome=promedio
            max_ocupa=cada_ocu
    return max_ocupa

def colombianos_rango(colombianos: dict,ocupacion: str,rango: str) -> list:
    retorno = []
    lis_ran=rango.split("-")
    lis_colom=colombianos[ocupacion]
    i=0
    while len(lis_colom)>i:
        colombiano=lis_colom[i]
        if colombiano["anio_nacimiento"]>int(lis_ran[0]) and colombiano["anio_nacimiento"]<int(lis_ran[1]):
            colombiano["ocupacion"]=ocupacion
            retorno.append(colombiano)
        i+=1      
    return retorno
#funcion4=colombianos_rango(funcion1,"actor","1940-1980")

def nacionalidades(colombianos: dict) -> dict:
    nacionalidades={}
    for cada_ocu in colombianos:
        lis_colom=colombianos[cada_ocu]
        i=0
        while len(lis_colom)>i:
            colombiano=lis_colom[i]
            nali=colombiano["ciudadania"]
            if nali in nacionalidades:
                nacionalidades[nali]+=1
            else:
                nacionalidades[nali]=1
            i+=1
    return nacionalidades

def calcular_edad(colombianos: dict) -> dict:
    import datetime
    currentDateTime=datetime.datetime.now()
    date=currentDateTime.date()
    year=int(date.strftime("%Y"))
    for cada_ocu in colombianos:
        lis_colom=colombianos[cada_ocu] 
        i=0
        while len(lis_colom)>i:
            colombiano=lis_colom[i]
            anio_n=colombiano["anio_nacimiento"]
            anio_m=colombiano["anio_muerte"]
            if anio_m == 0:
                edad=year-anio_n
                colombiano["edad"]=edad
            else:
                edad=anio_m-anio_n
                colombiano["edad"]=edad
            i+=1
    return colombianos
#funcion2=calcular_edad(funcion1)

def colombianos_fallecidos(colombianos: dict) -> dict:
    colombianos_fallecidos={}
    for cada_ocu in colombianos:
        lis_colom=colombianos[cada_ocu]
        lis_falle=[]
        i=0
        while len(lis_colom)>i:
            colombiano=lis_colom[i]
            anio_m=colombiano["anio_muerte"]
            if not anio_m == 0:
                lis_falle.append(colombiano)
            i+=1
        if lis_falle != []:
            colombianos_fallecidos[cada_ocu]=lis_falle      
    return colombianos_fallecidos
#funcion3=colombianos_fallecidos(funcion2)

def poema():
    i=0
    while i in range(1000):
        if i<=1000:
            print("Te dedico un poema... Que bonitos ojos tienes")
        i+=1
        pass

poema()