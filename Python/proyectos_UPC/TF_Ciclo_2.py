import pandas as pd
import time
import os
import matplotlib.pyplot as plt

obj = object
fabricas = []
juguetes = []

for k in range(2):
    fabricas.append(obj)
    
for k in range(5):    
    juguetes.append(obj)

class Pais:
    def __init__(self, nombre_pais, porc_impuesto):
        self.__nombre_pais = nombre_pais
        self.__porc_impuesto = porc_impuesto

    @property
    def nombre_pais(self):
        return self.__nombre_pais

    @nombre_pais.setter
    def set_nombre_pais(self, nombre_pais):
        self.__nombre_pais = nombre_pais

    @property
    def porc_impuesto(self):
        return self.__porc_impuesto
    
    @porc_impuesto.setter
    def set_porc_impuesto(self, porc_impuesto):
        self.__porc_impuesto = porc_impuesto

class Juguete:
    def __init__(self, tipo_juguete, unid_producidas, precio_unidad, costo_prod, pais_destino):#, impuesto_destino):
        self.__tipo_juguete = tipo_juguete
        self.__unid_producidas = unid_producidas
        self.__precio_unidad = precio_unidad
        self.__costo_prod = costo_prod
        self.__pais_destino = pais_destino
        #self.__impuesto_destino = impuesto_destino

    @property
    def tipo_juguete(self):
        return self.__tipo_juguete
    
    @tipo_juguete.setter
    def set_tipo_juguete(self, tipo_juguete):
        self.__tipo_juguete = tipo_juguete

    @property
    def unid_producidas(self):
        return self.__unid_producidas
    
    @unid_producidas.setter
    def set_unid_producidas(self, unid_producidas):
        self.__unid_producidas = unid_producidas

    @property
    def precio_unidad(self):
        return self.__precio_unidad
    
    @precio_unidad.setter
    def set_precio_unidad(self, precio_unidad):
        self.__precio_unidad = precio_unidad

    @property
    def costo_prod(self):
        return self.__costo_prod
    
    @costo_prod.setter
    def set_costo_prod(self, costo_prod):
        self.__costo_prod = costo_prod

    @property
    def pais_destino(self):
        return self.__pais_destino
    
    @pais_destino.setter
    def set_pais_destino(self, pais_destino):
        self.__pais_destino = pais_destino

    #@property
    #def impuesto_destino(self):
        #return self.__impuesto_destino
    
    #@impuesto_destino.setter
    #def set_impuesto_destino(self, impuesto_destino):
        #self.__impuesto_destino = impuesto_destino
    
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

    @property
    def nombre_fabrica(self):
        return self.__nombre_fabrica
    
    @nombre_fabrica.setter
    def set_nombre_fabrica(self, nombre_fabrica):
        self.__nombre_fabrica = nombre_fabrica

    @property
    def pais_origen(self):
        return self.__pais_origen
    
    @pais_origen.setter
    def set_pais_origen(self, pais_origen):
        self.__pais_origen = pais_origen

    @property
    def cap_produccion(self):
        return self.__cap_produccion
    
    @cap_produccion.setter
    def set_cap_produccion(self, cap_produccion):
        self.__cap_produccion = cap_produccion

    @property
    def list_juguetes(self):
        return self.__list_juguetes
    
    @list_juguetes.setter
    def set_list_juguetes(self, list_juguetes):
        self.__list_juguetes = list_juguetes


brasil = Pais("Brasil", 0.12)
eeuu = Pais("EE.UU.", 0.1)
canada = Pais("Canada", 0.08)
mexico = Pais("Mexico", 0.05)
china = Pais("China", 0.08)

paises = [brasil, canada, china, eeuu, mexico]

juguetes[0] = Juguete("Pelota", 3500, 25, 10, paises[2])
juguetes[1] = Juguete("Robot", 1000, 40, 25, paises[1])
juguetes[2] = Juguete("Munieca", 2000, 20, 12, paises[3])
juguetes[3] = Juguete("Carro", 5000, 8, 4, paises[4])
juguetes[4] = Juguete("Rompecabezas", 1000, 10, 5, paises[0])

fabricas[0] = Fabrica("Mattel", paises[3], 10000, [juguetes[1], juguetes[4]])
fabricas[1] = Fabrica("Fabrinquedo", paises[0], 8000, [juguetes[0], juguetes[2], juguetes[3]])

def menu_principal():
    
    os.system("cls")

    i = True

    print("\n\t-        JUGUETELANDIA        -")
    print("\t- Opcion 1: Modificar fabrica -")
    print("\t- Opcion 2: Modificar juguete -")
    print("\t- Opcion 3: Mostrar reportes  -")
    print("\t- Opcion 4: Cerrar sistema    -")

    print("\n\tIngrese la opcion que desee realizar: ", end="")
    opcion = int(input())

    while i:
        if opcion < 1 or opcion > 4:
            opcion = int(input("Opcion no valida (no esta en el rango 1-4), intentelo nuevamente: "))
        else: 
            break

    match opcion:
        case 1:
            
            modificar_fab()

        

def modificar_fab():

    os.system("cls")

    i = True
    k = 0

    print("\n\t-        MENU MODIFICADOR        -")
    print("\t- Opcion 1: Agregar fabrica      -")
    print("\t- Opcion 2: Eliminar fabrica     -")
    print("\t- Opcion 3: Regresar             -")
    print("\t- Opcion 4: Cerrar sistema       -")

    print("\n\tIngrese la opcion que desee realizar: ", end="")
    opcion_fab = int(input())

    while i:
        if opcion_fab < 1 or opcion_fab > 4:
            opcion_fab = int(input("Opcion no valida (no esta en el rango 1-4), intentelo nuevamente: "))
        else: 
            break

    match opcion_fab:

        case 1:

            os.system("cls")

            print("\n\tIngrese el nombre de la fabrica a registrar: ", end="")
            nombre = input()

            while k < len(fabricas):
                if nombre.upper() == fabricas[k].nombre_fabrica.upper():

                    print("\n\tEsta fabrica ya existe, escriba otro nombre: ", end="")
                    nombre = input()
                else:
                    k += 1

            k = 0

            print("\n\tLISTA DE PAISES...")

            time.sleep(2)

            print("\n\t\t  Paises")

            while k < len(paises):

                print(f"\tOpcion {k + 1}: ", end="")
                print(paises[k].nombre_pais)

                k += 1

            print(f"\tOpcion {k + 1}: Ingresar otro pais")

            print("\n\tIngrese la opcion en la que se encuentre el pais: ", end="")
            opcion_pa = int(input())

            while i:
                if opcion_pa < 1 or opcion_pa > (len(paises) + 1):
                    opcion_pa = int(input("Opcion no valida, intentelo nuevamente: "))
                else: 
                    break

            if opcion_pa == k + 1:

                pais = input("\n\tIngrese el nombre del país: ")
                impuesto = input("\tIngrese el porcentaje del impuesto en el país (XX.X% reemplace las X por números): ")

                while True:
                    
                    try:
                        impuesto = float(impuesto)
                        if 0 <= impuesto <= 100:
                            break  
                        else:
                            impuesto = input("\tImpuesto no valido, debe estar en el rango de 0 a 100%, intentelo nuevamente: ")
                    except ValueError:
                        impuesto = input("\tImpuesto no valido, debe ser un valor numerico, intentelo nuevamente: ")

                print("\n\tRegistrando el nuevo pais...")

                time.sleep(2)

                paises.append(Pais(pais, impuesto))

                print(paises[k].nombre_pais)
            
        case 2:

            os.system("cls")

            print("\n\tLISTA DE FABRICAS...")

            time.sleep(2)

            nombres_fabricas = [fabrica.nombre_fabrica for fabrica in fabricas]
            paises_fabricas = [pais_fab.pais_origen.nombre_pais for pais_fab in fabricas]
            indices = [f"Opcion {k + 1}" for k in range(len(nombres_fabricas))]

            print("\n")

            dt_fabricas = pd.DataFrame({"Fabricas": nombres_fabricas,
                                        "Paises" : paises_fabricas
                                        })
            dt_fabricas.index = indices

            print(dt_fabricas)
menu_principal()