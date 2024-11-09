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
    def nombre_pais(self, nombre_pais):
        self.__nombre_pais = nombre_pais

    @property
    def porc_impuesto(self):
        return self.__porc_impuesto
    
    @porc_impuesto.setter
    def porc_impuesto(self, porc_impuesto):
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
    def tipo_juguete(self, tipo_juguete):
        self.__tipo_juguete = tipo_juguete

    @property
    def unid_producidas(self):
        return self.__unid_producidas
    
    @unid_producidas.setter
    def unid_producidas(self, unid_producidas):
        self.__unid_producidas = unid_producidas

    @property
    def precio_unidad(self):
        return self.__precio_unidad
    
    @precio_unidad.setter
    def precio_unidad(self, precio_unidad):
        self.__precio_unidad = precio_unidad

    @property
    def costo_prod(self):
        return self.__costo_prod
    
    @costo_prod.setter
    def costo_prod(self, costo_prod):
        self.__costo_prod = costo_prod

    @property
    def pais_destino(self):
        return self.__pais_destino
    
    @pais_destino.setter
    def pais_destino(self, pais_destino):
        self.__pais_destino = pais_destino

    #@property
    #def impuesto_destino(self):
        #return self.__impuesto_destino
    
    #@impuesto_destino.setter
    #def impuesto_destino(self, impuesto_destino):
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
    def nombre_fabrica(self, nombre_fabrica):
        self.__nombre_fabrica = nombre_fabrica

    @property
    def pais_origen(self):
        return self.__pais_origen
    
    @pais_origen.setter
    def pais_origen(self, pais_origen):
        self.__pais_origen = pais_origen

    @property
    def cap_produccion(self):
        return self.__cap_produccion
    
    @cap_produccion.setter
    def cap_produccion(self, cap_produccion):
        self.__cap_produccion = cap_produccion

    @property
    def list_juguetes(self):
        return self.__list_juguetes
    
    @list_juguetes.setter
    def list_juguetes(self, list_juguetes):
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

    print("\n\t-        JUGUETELANDIA        -")
    print("\t- Opcion 1: Modificar fabrica -")
    print("\t- Opcion 2: Modificar juguete -")
    print("\t- Opcion 3: Mostrar reportes  -")
    print("\t- Opcion 4: Cerrar sistema    -")

    print("\n\tIngrese la opcion que desee realizar: ", end="")

    while True:
                    
        try:
            opcion = int(input())
            if 1 <= opcion <= 4:
                break  
            else:
                print("\tOpcion no valida, debe estar en el rango de 1 a 4, intentelo nuevamente: ", end="")
        except ValueError:
            print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

    match opcion:
        case 1:
            
            modificar_fab()

        

def modificar_fab():

    os.system("cls")

    print("\n\t-        MENU MODIFICADOR        -")
    print("\t- Opcion 1: Agregar fabrica      -")
    print("\t- Opcion 2: Eliminar fabrica     -")
    print("\t- Opcion 3: Regresar             -")
    print("\t- Opcion 4: Cerrar sistema       -")

    print("\n\tIngrese la opcion que desee realizar: ", end="")
    
    while True:
                    
        try:
            opcion_fab = int(input())
            if 1 <= opcion_fab <= 4:
                break  
            else:
                print("\tOpcion no valida, debe estar en el rango de 1 a 4, intentelo nuevamente: ", end="")
        except ValueError:
            print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

    match opcion_fab:

        case 1:

            agregar_fabrica()
            
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
            
        case 3:
            
            menu_principal()
            
        case 4:

            exit()

def agregar_fabrica():

    os.system("cls")

    k = 0

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

    print("\n\t******** Paises *******\n")

    while k < len(paises):

        print(f"\tOpcion {k + 1}: ", end="")
        print(paises[k].nombre_pais)

        k += 1

    print(f"\tOpcion {k + 1}: Ingresar otro pais")

    print("\n\tIngrese la opcion en la que se encuentre el pais: ", end="")

    while True:
                    
        try:
            opcion_pa = int(input())
            if 1 <= opcion_pa <= k + 1:
                break  
            else:
                        print(f"\tOpcion no valida, debe estar en el rango de 1 a {k + 1}, intentelo nuevamente: ", end="")
        except ValueError:
            print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

    if opcion_pa == k + 1:

        pais = input("\n\tIngrese el nombre del país: ")
        print("\tIngrese el porcentaje del impuesto en el país (XX.X% reemplace las X por números): ", end="")               

        while True:
                    
            try:
                impuesto = float(input())
                if 0 <= impuesto <= 100:
                    break  
                else:
                    print("\tImpuesto no valido, debe estar en el rango de 0 a 100%, intentelo nuevamente: ", end="")
            except ValueError:
                print("\tImpuesto no valido, debe ser un valor numerico, intentelo nuevamente: ", end="")

        impuesto = impuesto / 100
        paises.append(Pais(pais, impuesto))

    print(f"\n\tIngrese la capacidad de produccion de la nueva fabrica '{nombre}': ", end="")
    
    while True:
                    
        try:
            cap_prod = int(input())
            if 1 <= cap_prod:
                break  
            else:
                        print("\tCapacidad no valida, debe ser mayor a 1, intentelo nuevamente: ", end="")
        except ValueError:
                    print("\tCapacidad no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

    k = 0

    print("\n\tLISTA DE JUGUETES...")

    time.sleep(2)

    list_borrar = juguetes
    list_final = []

    while True:

        print("\n\t******** Juguetes *******\n")

        while k < len(list_borrar):

            print(f"\tOpcion {k + 1}: ", end="")
            print(list_borrar[k].tipo_juguete)

            k += 1

        print("\n\tIngrese la opcion en la que se encuentre el juguete: ", end="")

        while True:
                    
            try:
                opcion_jug = int(input())
                if 1 <= opcion_jug <= k + 1:
                    break  
                else:
                    print(f"\tOpcion no valida, debe estar en el rango de 1 a {k + 1}, intentelo nuevamente: ", end="")
            except ValueError:
                print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

        k = 0

        list_final.append(list_borrar[opcion_jug - 1])
        list_borrar.pop(opcion_jug - 1)
               
        print("\n\t** Juguetes agregados **\n")

        for juguete in list_final:
            print("\t-", juguete.tipo_juguete)

        if len(list_borrar) == 0:
            break

        print("\n\tDesea agregar otro juguete? (S/si, N/no): ", end="")
                
        while True:
                    
            opcion_agr_jug = str(input())
            if opcion_agr_jug.upper() != 'S' and opcion_agr_jug.upper() != 'N':
                print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
            elif opcion_agr_jug.isdigit():
                print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
            else:
                break

        if opcion_agr_jug.upper() == 'S':
            continue
        elif opcion_agr_jug.upper() == 'N':
            break

    print("\n\tRegistrando la nueva fabrica...")

    time.sleep(2)
            
    fabricas.append(Fabrica(nombre, paises[opcion_pa - 1], cap_prod, list_final))
            
    k = 0
                
    print("\n\t******** Fabricas *******\n")

    while k < len(fabricas):

        print(f"\tFabrica {k + 1}: ", end="")                   

        if k == (len(fabricas) - 1):
            print("\033[32m"+ fabricas[k].nombre_fabrica)   
        else:
            print(fabricas[k].nombre_fabrica)

        k += 1

    print("\n\t" + "\033[37m" + "Fabrica registrada exitosamente")

    time.sleep(0.5)

    print("\n\tDesea agregar otra fabrica? (S/si, N/no): ", end="")

    while True:
                    
        opcion_agr_final = str(input())
        if opcion_agr_final.upper() != 'S' and opcion_agr_final.upper() != 'N':
                print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
        elif opcion_agr_final.isdigit():
            print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
        else:
            break

    if opcion_agr_final.upper() == 'S':
        agregar_fabrica()
    elif opcion_agr_final.upper() == 'N':
        print()

menu_principal()