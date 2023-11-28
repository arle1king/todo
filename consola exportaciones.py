
import pandas as pd

def cargar_datos(nombreArchivo: str)->pd.DataFrame:
    exportaciiones=pd.read_csv(nombreArchivo)
    return exportaciiones

function1=cargar_datos("exportaciones.csv")

def graficar(function1):
    loco=function1.groupby('Producto').ValorMilesDolar.sum()
    
    return loco


def graficar(loco):
    lalo=loco.groupby('Cavendish Valery')
    return 
