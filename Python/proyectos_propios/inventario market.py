import pandas as pd
import os

dataframe = pd.read_excel("c:/Users/Adrian/Desktop/ADRIAN/Repositorio/Python/proyectos_propios/inventario.xlsx")

def menu_principal():

    os.system("cls")
    print("-    BODEGA 'DON PEPE'    -")

suma = float(dataframe["Columna 3"][0]) + 1

print(suma)