import pandas as pd
import time
import os
import random

obj = object
fabricas = []
juguetes = []

for k in range(2):
    fabricas.append(obj)
    juguetes.append(obj)

class Pais:
    def __init__(self, nombre_pais, porc_impuesto):
        self.__nombre_pais = nombre_pais
        self.__porc_impuesto = porc_impuesto

class Juguete:
    def __init__(self, tipo_juguete, unid_producidas, precio_unidad, costo_prod, pais_destino, impuesto_destino):
        self.__tipo_juguete = tipo_juguete
        self.__unid_producidas = unid_producidas
        self.__precio_unidad = precio_unidad
        self.__costo_prod = costo_prod
        self.__pais_destino = pais_destino
        self.__impuesto_destino = impuesto_destino

    def calc_impuesto(self):
        return
    
    def calc_ingreso(self):
        return
    
class Fabrica:
    def __init__(self, nombre_fabrica, pais_origen, cap_produccion, list_juguetes):
        self.__nombre_fabrica = nombre_fabrica
        self.__pais_origen = pais_origen
        self.__cap_produccion = cap_produccion
        self.__list_juguetes = list_juguetes
        #self.__imp_origen = imp_origen

def menu_principal():
    
    os.system("cls")
    
    i = True

    print("\n\t-     JUGUETELANDIA     -")
    print("\t- Opcion 1: Agregar fabrica")
    print("\t- Opcion 2: Agregar juguete")
    print("\t- Opcion 3: Mostrar reportes")
    print("\t- Opcion 4: Cerrar sistema")

    print("\n\tIngrese la opcion que desee realizar: ", end="")
    opcion = int(input())

    while i:
        if opcion < 1 or opcion > 4:
            opcion = int(input("Opcion no valida (no esta en el rango 1-4), intentelo nuevamente: "))
        else: 
            break

menu_principal()