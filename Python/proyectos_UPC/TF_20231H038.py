import pandas as pd
import time
import os
import matplotlib.pyplot as plt
import random

obj = object
fabricas = []
juguetes = []
nombres_paises = []
impuesto_ori = []
unidades_prod = []
impuesto_total_final = [0]
ingreso_total_final = [0]

for k in range(2):
    fabricas.append(obj)
    
for k in range(5):    
    juguetes.append(obj)
    unidades_prod.append(0)

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
    
    def calc_impuesto(self, impuesto_origen):
        
        print(f"\n\tCalculando el impuesto del juguete de tipo '{self.__tipo_juguete}'...")

        time.sleep(2)

        unid_producidas = self.__unid_producidas
        costo_prod = self.__costo_prod
        impuesto_destino = self.__pais_destino.porc_impuesto
        precio_unidad = self.__precio_unidad

        costo_total_prod = (unid_producidas * costo_prod)
        ingreso_total = unid_producidas * precio_unidad
        impuesto1 = impuesto_origen * ingreso_total
        impuesto2 = impuesto_destino * ingreso_total
        impuesto_final = costo_total_prod + impuesto1 + impuesto2

        print(f"\n\tEl impuesto total seria: {impuesto_final}")

        impuesto_total_final[0] = impuesto_total_final[0] + impuesto_final

        time.sleep(1)
    
    def calc_ingreso(self, impuesto_origen):

        print(f"\n\tCalculando el ingreso total del juguete de tipo '{self.__tipo_juguete}'...")

        time.sleep(2)
        
        unid_producidas = self.__unid_producidas
        costo_prod = self.__costo_prod
        impuesto_destino = self.__pais_destino.porc_impuesto
        precio_unidad = self.__precio_unidad

        costo_total_prod = (unid_producidas * costo_prod)
        ingreso_total = unid_producidas * precio_unidad
        impuesto1 = impuesto_origen * ingreso_total
        impuesto2 = impuesto_destino * ingreso_total
        impuesto_final = costo_total_prod + impuesto1 + impuesto2
        ingreso_final = ingreso_total - impuesto_final

        print(f"\n\tEl ingreso total seria: {ingreso_final}")

        ingreso_total_final[0] = ingreso_total_final[0] + ingreso_final

        time.sleep(1)

    
class Fabrica:
    def __init__(self, nombre_fabrica, cap_produccion, list_juguetes):
        self.__nombre_fabrica = nombre_fabrica
        self.__cap_produccion = cap_produccion
        self.__list_juguetes = list_juguetes
        self.__pais_origen = []

    @property
    def nombre_fabrica(self):
        return self.__nombre_fabrica
    
    @nombre_fabrica.setter
    def nombre_fabrica(self, nombre_fabrica):
        self.__nombre_fabrica = nombre_fabrica

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

    def agregar_pais(self, pais_origen):
        self.__pais_origen.append(pais_origen)

        pais = self.__pais_origen[0]

        pais_obj = pais.nombre_pais

    def guardar_pais(self):
        
        for i in self.__pais_origen:

            nombres_paises.append(i.nombre_pais)

    def guardar_imp_ing(self):

        for i in self.__pais_origen:

            nombres_paises.append(i.porc_impuesto)

    def mod_pais_dest(self):

        k = 0

        while True:

            if len(self.__list_juguetes) == 0:
                
                print("\n\tNo hay juguetes registrados, es posible que todos hayan sido eliminados,")
                print("\tagregue un juguete, desea ir al menu 'agregar juguete'? (S/N): ", end="")

                while True:
                    
                    opcion_no_jug = str(input())
                    if opcion_no_jug.upper() != 'S' and opcion_no_jug.upper() != 'N':
                        print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                    elif opcion_no_jug.isdigit():
                        print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                    else:
                        break

                if opcion_no_jug.upper() == 'S':

                    self.agregar_jug()       
                elif opcion_no_jug.upper() == 'N':

                    print("\n\tRegresando al menu principal...")

                    time.sleep(1.5)

                    menu_principal()
        
            nombres_juguetes = [juguete.tipo_juguete for juguete in self.__list_juguetes]
            paises_dest = [pais.pais_destino.nombre_pais for pais in self.__list_juguetes]

            indices = [f"Opcion {k + 1}:" for k in range(len(self.__list_juguetes))]

            print("\n")

            dt_juguetes = pd.DataFrame({"Juguete" : nombres_juguetes,
                                        "Paises destino" : paises_dest
                                   })

            dt_juguetes.index = indices

            print(dt_juguetes)

            print("\n\tIngrese la opcion en la que se encuentre el juguete: ", end="")

            while True:
                    
                try:
                    opcion_jug = int(input())
                    if 1 <= opcion_jug <= len(self.__list_juguetes):
                        break  
                    else:
                        print(f"\tOpcion no valida, debe estar en el rango de 1 a {len(self.__list_juguetes)}, intentelo nuevamente: ", end="")
                except ValueError:
                    print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

            k = 0
            i = 0

            print("\n\t******** Paises *******\n")

            while k < len(paises):

                if self.__list_juguetes[opcion_jug - 1].pais_destino.nombre_pais == paises[k].nombre_pais:

                    k += 1
                else:
                    print(f"\tOpcion {i + 1}: ", end="")
                    print(paises[k].nombre_pais)

                    k += 1
                    i += 1

            print(f"\tOpcion {i + 1}: Ingresar otro pais")

            print("\n\tIngrese la opcion en la que se encuentre el pais: ", end="")

            while True:
                    
                try:
                    opcion_pa = int(input())
                    if 1 <= opcion_pa <= i + 1:
                        break  
                    else:
                        print(f"\tOpcion no valida, debe estar en el rango de 1 a {i + 1}, intentelo nuevamente: ", end="")
                except ValueError:
                    print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

            if opcion_pa == i + 1:

                pais = input("\n\tIngrese el nombre del país: ")
                print("\tIngrese el porcentaje del impuesto en el país ('XX.X%' reemplace las X por números): ", end="")               

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

            print("\n\tModificando el pais del juguete...")

            time.sleep(2)

            self.__list_juguetes[opcion_jug - 1] = Juguete(self.__list_juguetes[opcion_jug - 1].tipo_juguete, self.__list_juguetes[opcion_jug - 1].unid_producidas, self.__list_juguetes[opcion_jug - 1].precio_unidad, self.__list_juguetes[opcion_jug - 1].costo_prod, paises[opcion_pa - 1])

            print(f"\n\tSe modifico el pais de destino del juguete '{self.__list_juguetes[opcion_jug - 1].tipo_juguete}' de la fabrica '{self.__nombre_fabrica}'")

            time.sleep(1)

            print("\n\tDesea modificar otro juguete? (S/si, N/no): ", end="")

            while True:
                    
                opcion_mod_final = str(input())
                if opcion_mod_final.upper() != 'S' and opcion_mod_final.upper() != 'N':
                    print("\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                elif opcion_mod_final.isdigit():
                    print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                else:
                    break

            if opcion_mod_final.upper() == 'S':

                continue

            elif opcion_mod_final.upper() == 'N':

                break

    def impuesto_origen(self):

        for i in self.__pais_origen:

            impuesto_ori.append(i.porc_impuesto * 100)

    def asignar_unidades(self):

        k = 0
        capacidad = self.__cap_produccion

        while k < len(self.__list_juguetes):

            i = 0

            if capacidad == ((len(self.__list_juguetes) - 1) * 100):

                while k < len(self.__list_juguetes):

                    self.__list_juguetes[k].unid_producidas = 100
                    unidades_prod[k] = unidades_prod[k] + 100

                    k += 1

                print(f"\n\tDebido a que solo queda capacidad para fabricar {capacidad} juguetes mas, se le asignara 100 unidades al resto de juguetes...")

                time.sleep(5)

                break
        
            print(f"\n\tIngrese la cantidad de juguetes de tipo '{self.__list_juguetes[k].tipo_juguete}' que producira la fabrica '{self.__nombre_fabrica}': ", end="")

            if self.__list_juguetes[k].tipo_juguete == self.__list_juguetes[-1].tipo_juguete:

                while True:
                    try:
                        unidades = int(input())
                        if 100 <= unidades <= capacidad:
                            break  
                        else:
                            print(f"\tOpcion no valida, debe estar en el rango de 100 a {capacidad}, intentelo nuevamente: ", end="")
                    except ValueError:
                        print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

            else:
                while True:
                    
                    try:
                        unidades = int(input())
                        if 100 <= unidades <= capacidad - ((len(self.__list_juguetes) - 1) * 100):
                            break  
                        else:
                            print(f"\tOpcion no valida, debe estar en el rango de 100 a {capacidad - ((len(self.__list_juguetes) - 1) * 100)}, intentelo nuevamente: ", end="")
                    except ValueError:
                        print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

            self.__list_juguetes[k].unid_producidas = unidades
            capacidad = capacidad - unidades

            while i < len(juguetes):

                if self.__list_juguetes[k].tipo_juguete == juguetes[i].tipo_juguete:

                    unidades_prod[i] = unidades_prod[i] + unidades

                i += 1

            i = 0

            while i < len(juguetes):

                juguetes[i].unid_producidas = unidades_prod[i]

                i += 1

            print("\n\tREGISTRANDO...")

            time.sleep(2)

            print(f"\n\tUnidades registradas exitosamente")

            time.sleep(1)

            k += 1

        os.system("cls")
        
    def agregar_jug(self):

        i = 0
        k = 0
        list_final = juguetes
        list_borrar = self.__list_juguetes

        while i < len(self.__list_juguetes):

            k = 0

            while k < len(juguetes):
                if list_final[k].tipo_juguete == list_borrar[i].tipo_juguete:
                    list_final.pop(k)

                k += 1

            i += 1

        i = 0
        k = 0

        while True:

            print("\n\t******** Juguetes *******\n")

            while k < len(list_final):

                print(f"\tOpcion {k + 1}: ", end="")
                print(list_final[k].tipo_juguete)

                k += 1

            print("\n\tIngrese la opcion en la que se encuentre el juguete: ", end="")

            while True:
                    
                try:
                    opcion_jug = int(input())
                    if 1 <= opcion_jug <= k:
                        break  
                    else:
                        print(f"\tOpcion no valida, debe estar en el rango de 1 a {k}, intentelo nuevamente: ", end="")
                except ValueError:
                    print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

            k = 0

            self.__list_juguetes.append(list_final[opcion_jug - 1])
            list_final.pop(opcion_jug - 1)
               
            print(f"\n\t** Juguetes de la fabrica {self.__nombre_fabrica}**\n")

            for juguete in self.__list_juguetes:
                print("\t-", juguete.tipo_juguete)

            if len(list_final) == 0:
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
                os.system("cls")

                continue
            elif opcion_agr_jug.upper() == 'N':
                break

    def eliminar_jug(self):

        while True:

            if len(self.__list_juguetes) == 0:
                
                print("\n\tNo hay juguetes registrados, es posible que todos hayan sido eliminados,")
                print("\tagregue un juguete, desea ir al menu 'agregar juguete'? (S/N): ", end="")

                while True:
                    
                    opcion_no_jug = str(input())
                    if opcion_no_jug.upper() != 'S' and opcion_no_jug.upper() != 'N':
                        print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                    elif opcion_no_jug.isdigit():
                        print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                    else:
                        break

                if opcion_no_jug.upper() == 'S':

                    self.agregar_jug()       
                elif opcion_no_jug.upper() == 'N':

                    print("\n\tRegresando al menu principal...")

                    time.sleep(1.5)

                    menu_principal()

            nombres_juguetes = [juguete.tipo_juguete for juguete in self.__list_juguetes]
            unid_juguetes = [unid.unid_producidas for unid in self.__list_juguetes]

            indices = [f"Opcion {k + 1}:" for k in range(len(self.__list_juguetes))]

            print("\n")

            dt_juguetes = pd.DataFrame({"Juguete" : nombres_juguetes,
                                    "Unidades producidas" : unid_juguetes
                                   })

            dt_juguetes.index = indices

            print(dt_juguetes)

            print("\n\tIngrese la opcion en la que se encuentre el juguete a eliminar: ", end="")

            while True:
                    
                try:
                    opcion_elim_jug = int(input())
                    if 1 <= opcion_elim_jug <= len(nombres_juguetes):
                        break  
                    else:
                        print(f"\tOpcion no valida, debe estar en el rango de 1 a {len(nombres_juguetes)}, intentelo nuevamente: ", end="")
                except ValueError:
                    print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")
            
            print(f"\n\tSe eliminara el juguete '{self.__list_juguetes[opcion_elim_jug - 1].tipo_juguete}', estas seguro? (S/N) :  ", end="")
                
            while True:
                    
                opcion_conf_elim = str(input())
                if opcion_conf_elim.upper() != 'S' and opcion_conf_elim.upper() != 'N':
                    print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                elif opcion_conf_elim.isdigit():
                    print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                else:
                    break
 
            if opcion_conf_elim.upper() == 'S':

                print("\n\tJuguete eliminado exitosamente")
        
                unidades_prod[opcion_elim_jug - 1] = unidades_prod[opcion_elim_jug - 1] - self.__list_juguetes[opcion_elim_jug - 1].unid_producidas
                self.__list_juguetes.pop(opcion_elim_jug - 1)

            elif opcion_conf_elim.upper() == 'N':
                self.eliminar_jug()

            time.sleep(1.1)

            print("\n\tDesea eliminar otro juguete? (S/si, N/no): ", end="")

            while True:
                    
                opcion_elim_final = str(input())
                if opcion_elim_final.upper() != 'S' and opcion_elim_final.upper() != 'N':
                    print("\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                elif opcion_elim_final.isdigit():
                    print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                else:
                    break

            if opcion_elim_final.upper() == 'S':

                continue

            elif opcion_elim_final.upper() == 'N':

                return

    def mostrar_juguetes(self):

        if len(self.__list_juguetes) == 0:
                
            print("\n\tNo hay juguetes registrados, es posible que todos hayan sido eliminados,")
            print("\tagregue un juguete, desea ir al menu 'agregar juguete'? (S/N): ", end="")

            while True:
                    
                opcion_no_jug = str(input())
                if opcion_no_jug.upper() != 'S' and opcion_no_jug.upper() != 'N':
                    print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                elif opcion_no_jug.isdigit():
                    print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                else:
                    break

            if opcion_no_jug.upper() == 'S':

                self.agregar_jug()       
            elif opcion_no_jug.upper() == 'N':

                print("\n\tRegresando al menu principal...")

                time.sleep(1.5)

                menu_principal()

        nombres_juguetes = [juguete.tipo_juguete for juguete in self.__list_juguetes]
        unid_juguetes = [unid.unid_producidas for unid in self.__list_juguetes]
        precios_unid = [precio.precio_unidad for precio in self.__list_juguetes]
        costos_prod = [costo.costo_prod for costo in self.__list_juguetes]
        paises_dest = [pais.pais_destino.nombre_pais for pais in self.__list_juguetes]
        impuestos_dest = [impuesto.pais_destino.porc_impuesto * 100 for impuesto in self.__list_juguetes]

        indices = [f"Juguete {k + 1}:" for k in range(len(self.__list_juguetes))]

        print("\n")

        dt_juguetes = pd.DataFrame({"Juguete" : nombres_juguetes,
                                    "Unidades producidas" : unid_juguetes,
                                    "Precio unitario ($)" : precios_unid,
                                    "Costo de produccion ($)" : costos_prod,
                                    "Pais destino" : paises_dest,
                                    "Impuesto destino (%)" : impuestos_dest
                                   })

        dt_juguetes.index = indices

        print(dt_juguetes)

        print("\n\tDesea ver los graficos? (S/Si, N/No): ", end="")

        while True:
                    
            opcion_no_fab = str(input())
            if opcion_no_fab.upper() != 'S' and opcion_no_fab.upper() != 'N':
                print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
            elif opcion_no_fab.isdigit():
                print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
            else:
                break

        if opcion_no_fab.upper() == 'N':

            print("\n\tRegresando al menu principal...")

            time.sleep(1.5)

            menu_principal()

        # --- GRAFICO UNIDADES PRODUCIDAS ---

        print("\n\tCreando el grafico de lineas...")

        time.sleep(2)

        plt.plot(nombres_juguetes, unid_juguetes, marker = "o", linestyle = "-", color = "m")

        plt.title("Unidades producidas")
        plt.xlabel("Nombres de los juguetes")
        plt.ylabel("Unidades producidas")

        plt.show()

        unid_juguetes.clear()

        # --- GRAFICO PRECIO UNITARIO---

        print("\n\tCreando el grafico de lineas...")

        time.sleep(2)

        plt.plot(nombres_juguetes, precios_unid, marker = "o", linestyle = "-", color = "g")

        plt.title("Precio unitario")
        plt.xlabel("Nombres de los juguetes")
        plt.ylabel("Unidades producidas")

        plt.show()

        precios_unid.clear()

        # --- GRAFICO COSTO DE PRODUCCION ---

        print("\n\tCreando el grafico de lineas...")

        time.sleep(2)

        plt.plot(nombres_juguetes, costos_prod, marker = "o", linestyle = "-", color = "c")

        plt.title("Costo de produccion")
        plt.xlabel("Nombres de los juguetes")
        plt.ylabel("Costos de produccion")

        plt.show()

        costos_prod.clear()

        # --- GRAFICO PAISES -----

        print("\n\tCreando el grafico de barras...")

        time.sleep(2)

        valores_pais = []

        for pais in paises_dest:

            valores_pais.append(paises_dest.count(pais))

        plt.bar(paises_dest, valores_pais, color = "blue")

        plt.title("Paises Destino")
        plt.xlabel("Pais")
        plt.ylabel("Cantidad de juguetes")

        plt.show()

        valores_pais.clear()

        # --- GRAFICO % IMPUESTO

        print("\n\tCreando el grafico de lineas...")

        time.sleep(2)

        plt.plot(nombres_juguetes, impuestos_dest, marker = "o", linestyle = "-", color = "k")

        plt.title("Impuesto destino")
        plt.xlabel("Nombre de los juguetes")
        plt.ylabel("Porcentaje de impuesto")

        plt.show()

        print("\n\tRegresando al menu principal...")

        nombres_paises.clear()
        impuesto_ori.clear()
        nombres_juguetes.clear()
        indices.clear()

    def calcular_impuesto(self):

        i = 0
        k = 0

        for nom_pais in fabricas:
            nom_pais.guardar_imp_ing()

        while i < len(fabricas):
            if fabricas[i].nombre_fabrica == self.__nombre_fabrica:

                k = i

            i += 1

        i = 0

        os.system("cls")

        while i < len(self.__list_juguetes):

            impuesto_origen = nombres_paises[k]

            self.__list_juguetes[i].calc_impuesto(impuesto_origen)

            i += 1

        i = 0

        print(f"\n\tEl impuesto total de la fabrica '{self.__nombre_fabrica}' es: {impuesto_total_final[0]}")

        impuesto_total_final[0] = 0
        nombres_paises.clear()

    def calcular_ingresos(self):

        i = 0
        k = 0

        for nom_pais in fabricas:
            nom_pais.guardar_imp_ing()

        while i < len(fabricas):
            if fabricas[i].nombre_fabrica == self.__nombre_fabrica:

                k = i

            i += 1

        i = 0

        os.system("cls")

        while i < len(self.__list_juguetes):

            impuesto_origen = nombres_paises[k]

            self.__list_juguetes[i].calc_ingreso(impuesto_origen)

            i += 1

        i = 0

        print(f"\n\tEl ingreso total de la fabrica '{self.__nombre_fabrica}' es: {ingreso_total_final[0]}")

        ingreso_total_final[0] = 0
        nombres_paises.clear()

brasil = Pais("Brasil", 0.12)
eeuu = Pais("EE.UU.", 0.1)
canada = Pais("Canada", 0.08)
mexico = Pais("Mexico", 0.05)
china = Pais("China", 0.08)

paises = [brasil, canada, china, eeuu, mexico]
unidades_prod = [4500, 2500, 3000, 6000, 2000]

juguetes[0] = Juguete("Pelota", unidades_prod[0], 25, 10, paises[2])
juguetes[1] = Juguete("Robot", unidades_prod[1], 40, 25, paises[1])
juguetes[2] = Juguete("Munieca", unidades_prod[2], 20, 12, paises[3])
juguetes[3] = Juguete("Carro", unidades_prod[3], 8, 4, paises[4])
juguetes[4] = Juguete("Rompecabezas", unidades_prod[4], 10, 5, paises[0])

fabricas[0] = Fabrica("Mattel", 10000, [juguetes[1], juguetes[4]])
fabricas[1] = Fabrica("Fabrinquedo", 8000, [juguetes[0], juguetes[2], juguetes[3]])

fabricas[0].agregar_pais(paises[3])
fabricas[1].agregar_pais(paises[0])

def menu_principal():
    
    os.system("cls")

    print("\n\t-        JUGUETELANDIA        -")
    print("\t- Opcion 1: Modificar fabrica -")
    print("\t- Opcion 2: Modificar juguete -")
    print("\t- Opcion 3: Mostrar reportes  -")
    print("\t- Opcion 4: Cerrar sistema   -")

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
        case 2:

            modificar_jug()
        case 3:

            reportes()
        case 4:

            exit()

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

            eliminar_fab()
            
        case 3:
            
            menu_principal()
            
        case 4:

            exit()

def agregar_fabrica():

    os.system("cls")

    k = 0
    i = 0

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

    os.system("cls")

    print("\n\tLISTA DE JUGUETES...")

    time.sleep(2)

    list_borrar = [] 

    if len(list_borrar) > 0:

        while len(list_borrar) > 0:

            list_borrar.pop(0)
        
    while i < len(juguetes):

        list_borrar.append(juguetes[i])

        i += 1

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
                if 1 <= opcion_jug <= k:
                    break  
                else:
                    print(f"\tOpcion no valida, debe estar en el rango de 1 a {k}, intentelo nuevamente: ", end="")
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
            os.system("cls")

            continue
        elif opcion_agr_jug.upper() == 'N':
            break

    fabricas.append(Fabrica(nombre, cap_prod, list_final))

    fabricas[-1].asignar_unidades()

    print("\n\tRegistrando la nueva fabrica...")

    time.sleep(2)
            
    fabricas[-1].agregar_pais(paises[opcion_pa - 1])

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

    time.sleep(1)

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

        print("\n\tRegresando al menu principal...")

        time.sleep(2)

        menu_principal()

def eliminar_fab():

    os.system("cls")

    if len(fabricas) == 0:
        print("\n\tNo hay fabricas registradas, es posible que todas hayan sido eliminadas,")
        print("\tagregue una fabrica, desea ir al menu 'agregar fabrica'? (S/N): ", end="")

        while True:
                    
            opcion_no_fab = str(input())
            if opcion_no_fab.upper() != 'S' and opcion_no_fab.upper() != 'N':
                print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
            elif opcion_no_fab.isdigit():
                print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
            else:
                break

        if opcion_no_fab.upper() == 'S':

            agregar_fabrica()       
        elif opcion_no_fab.upper() == 'N':

            print("\n\tRegresando al menu principal...")

            time.sleep(1.5)

            menu_principal()

    print("\n\tLISTA DE FABRICAS...")

    time.sleep(2)

    nombres_fabricas = [fabrica.nombre_fabrica for fabrica in fabricas]

    for nom_pais in fabricas:
        nom_pais.guardar_pais()

    indices = [f"Opcion {k + 1}:" for k in range(len(nombres_fabricas))]

    print("\n")

    dt_fabricas = pd.DataFrame({"Fabrica": nombres_fabricas,
                                "Pais" : nombres_paises
                                })
    dt_fabricas.index = indices

    print(dt_fabricas)

    print("\n\tIngrese la opcion en la que se encuentre la fabrica a eliminar: ", end="")

    nombres_paises.clear()

    while True:
                    
        try:
            opcion_elim_fab = int(input())
            if 1 <= opcion_elim_fab <= len(nombres_fabricas):
                break  
            else:
                        print(f"\tOpcion no valida, debe estar en el rango de 1 a {len(nombres_fabricas)}, intentelo nuevamente: ", end="")
        except ValueError:
            print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")
            
    print(f"\n\tSe eliminara la fabrica '{fabricas[opcion_elim_fab - 1].nombre_fabrica}', estas seguro? (S/N) :  ", end="")
                
    while True:
                    
        opcion_conf_elim = str(input())
        if opcion_conf_elim.upper() != 'S' and opcion_conf_elim.upper() != 'N':
            print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
        elif opcion_conf_elim.isdigit():
            print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
        else:
            break
 
    nombres_paises.clear()

    if opcion_conf_elim.upper() == 'S':

        print("\n\tFabrica eliminada exitosamente")
        
        fabricas.pop(opcion_elim_fab - 1)

    elif opcion_conf_elim.upper() == 'N':
        eliminar_fab()

    time.sleep(1.1)

    print("\n\tDesea eliminar otra fabrica? (S/si, N/no): ", end="")

    while True:
                    
        opcion_elim_final = str(input())
        if opcion_elim_final.upper() != 'S' and opcion_elim_final.upper() != 'N':
                print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
        elif opcion_elim_final.isdigit():
            print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
        else:
            break

    if opcion_elim_final.upper() == 'S':

        eliminar_fab()       
    elif opcion_elim_final.upper() == 'N':

        print("\n\tRegresando al menu principal...")

        time.sleep(1.5)

        menu_principal()

def modificar_jug():

    os.system("cls")

    
    print("\n\t-         MENU MODIFICADOR         -")
    print("\t- Opcion 1: Agregar juguete        -")
    print("\t- Opcion 2: Eliminar juguete       -")
    print("\t- Opcion 3: Designar pais destino  -")
    print("\t- Opcion 4: Regresar               -")
    print("\t- Opcion 5: Cerrar sistema         -")

    print("\n\tIngrese la opcion que desee realizar: ", end="")
    
    while True:
                    
        try:
            opcion_jug = int(input())
            if 1 <= opcion_jug <= 5:
                break  
            else:
                print("\tOpcion no valida, debe estar en el rango de 1 a 5, intentelo nuevamente: ", end="")
        except ValueError:
            print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

    match opcion_jug:

        case 1:

            agregar_juguete()
            
        case 2:

            eliminar_jug()
            
        case 3:
            
            designar_pais()

        case 4:

            menu_principal()
            
        case 5:

            exit()

def agregar_juguete():
    
    os.system("cls")

    print("\n\t-           MENU AGREGAR JUGUETE             -")
    print("\t- Opcion 1: Agregar juguete nuevo            -")
    print("\t- Opcion 2: Agregar juguete en una fabrica   -")
    print("\t- Opcion 3: Regresar                         -")

    print("\n\tIngrese la opcion que desee realizar: ", end="")
    
    while True:
                    
        try:
            opcion_agr_jug = int(input())
            if 1 <= opcion_agr_jug <= 3:
                break  
            else:
                print("\tOpcion no valida, debe estar en el rango de 1 a 3, intentelo nuevamente: ", end="")
        except ValueError:
            print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

    
    match opcion_agr_jug:
         
        case 1:

            os.system("cls")
            
            print("\n\tIngrese el nombre del juguete a agregar: ", end="")

            k = 0

            nombre_jug = input()

            while k < len(juguetes):
                if nombre_jug.upper() == juguetes[k].tipo_juguete.upper():

                    print("\n\tEste juguete ya existe, escriba otro nombre: ", end="")
                    nombre_jug = input()

                else:

                    k += 1

            k = 0

            unidades_prod.append(0)

            print(f"\n\tIngrese el precio unitario del juguete '{nombre_jug}': ", end="")
    
            while True:
                    
                try:
                    precio_unit = float(input())
                    if 1 <= precio_unit:
                        break  
                    else:
                        print("\tCantidad no valida, debe ser mayor a S/1, intentelo nuevamente: ", end="")
                except ValueError:
                    print("\tCantidad no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

            print(f"\n\tIngrese el costo de produccion del juguete '{nombre_jug}': ", end="")
    
            while True:
                    
                try:
                    costo_prod = float(input())
                    if 1 <= costo_prod:
                        break  
                    else:
                        print("\tCantidad no valida, debe ser mayor a S/1, intentelo nuevamente: ", end="")
                except ValueError:
                    print("\tCantidad no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

            os.system("cls")

            print("\n\tRegistrando el nuevo juguete...")

            i = random.randint(0, (len(paises) - 1))

            juguetes.append(Juguete(nombre_jug, unidades_prod[-1], precio_unit, costo_prod, paises[i]))

            time.sleep(2)

            print(f"\n\tJuguete '{nombre_jug}' registrado exitosamente")

            print("\n\tDesea agregar otro juguete? (S/si, N/no): ", end="")

            while True:
                    
                opcion_agr_final = str(input())
                if opcion_agr_final.upper() != 'S' and opcion_agr_final.upper() != 'N':
                        print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                elif opcion_agr_final.isdigit():
                    print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                else:
                    break

            if opcion_agr_final.upper() == 'S':

                agregar_juguete()       
            elif opcion_agr_final.upper() == 'N':

                print("\n\tRegresando al menu principal...")

                time.sleep(2)

                menu_principal()
        
        case 2:

            k = 0
            i = 0

            os.system("cls")

            print("\n\tLISTA DE FABRICAS...")

            time.sleep(2)

            nombres_fabricas = [fabrica.nombre_fabrica for fabrica in fabricas]

            for nom_pais in fabricas:
                nom_pais.guardar_pais()

            indices = [f"Opcion {k + 1}:" for k in range(len(nombres_fabricas))]

            print("\n")

            dt_fabricas = pd.DataFrame({"Fabrica": nombres_fabricas,
                                        "Pais" : nombres_paises
                                        })
            dt_fabricas.index = indices

            print(dt_fabricas)

            print("\n\tIngrese la opcion en la que se encuentre la fabrica a modificar: ", end="")

            nombres_paises.clear()

            while True:
                    
                try:
                    opcion_fabr = int(input())
                    if 1 <= opcion_fabr <= len(nombres_fabricas):
                        break  
                    else:
                        print(f"\tOpcion no valida, debe estar en el rango de 1 a {len(nombres_fabricas)}, intentelo nuevamente: ", end="")
                except ValueError:
                    print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

            print("\n\tLISTA DE JUGUETES...")

            time.sleep(2)

            fabricas[opcion_fabr - 1].agregar_jug()
            fabricas[opcion_fabr - 1].asignar_unidades()

            print("\n\tAgregando todos los juguetes...")

            time.sleep(2)

            print(f"\n\tSe registraron los juguetes en la fabrica '{fabricas[opcion_fabr - 1].nombre_fabrica}' exitosamente")

            print("\n\tDesea agregar otro juguete? (S/si, N/no): ", end="")

            while True:
                    
                opcion_agr_final = str(input())
                if opcion_agr_final.upper() != 'S' and opcion_agr_final.upper() != 'N':
                        print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                elif opcion_agr_final.isdigit():
                    print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                else:
                    break

            if opcion_agr_final.upper() == 'S':

                agregar_juguete()       
            elif opcion_agr_final.upper() == 'N':

                print("\n\tRegresando al menu principal...")

                time.sleep(2)

                menu_principal()
        
        case 3:
           modificar_jug()

def eliminar_jug():
    
    os.system("cls")

    print("\n\t-           MENU ELIMINAR JUGUETE             -")
    print("\t- Opcion 1: Eliminar juguete del sistema      -")
    print("\t- Opcion 2: Eliminar juguete de una fabrica   -")
    print("\t- Opcion 3: Regresar                          -")

    print("\n\tIngrese la opcion que desee realizar: ", end="")
    
    while True:
                    
        try:
            opcion_eli_jug = int(input())
            if 1 <= opcion_eli_jug <= 3:
                break  
            else:
                print("\tOpcion no valida, debe estar en el rango de 1 a 3, intentelo nuevamente: ", end="")
        except ValueError:
            print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

    
    match opcion_eli_jug:

        case 1:

            while True:

                os.system("cls")

                if len(juguetes) == 0:
                    print("\n\tNo hay juguetes registradas, es posible que todos hayan sido eliminados,")
                    print("\tagregue un juguete, desea ir al menu 'agregar juguete'? (S/N): ", end="")

                    while True:
                    
                        opcion_no_jug = str(input())
                        if opcion_no_jug.upper() != 'S' and opcion_no_jug.upper() != 'N':
                            print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                        elif opcion_no_jug.isdigit():
                            print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                        else:
                            break

                    if opcion_no_jug.upper() == 'S':

                        agregar_juguete()       
                    elif opcion_no_jug.upper() == 'N':

                        print("\n\tRegresando al menu principal...")

                        time.sleep(1.5)

                        menu_principal()

                print("\n\tLISTA DE JUGUETES...")

                time.sleep(2)

                nombres_juguetes = [juguete.tipo_juguete for juguete in juguetes]

                indices = [f"Opcion {k + 1}:" for k in range(len(nombres_juguetes))]

                print("\n")

                dt_juguetes = pd.DataFrame({"Juguete": nombres_juguetes,
                                            "Unid. Producidas" : unidades_prod
                                            })
                dt_juguetes.index = indices

                print(dt_juguetes)

                print("\n\tIngrese la opcion en la que se encuentre el juguete a eliminar: ", end="")

                while True:
                    
                    try:
                        opcion_elim_jug = int(input())
                        if 1 <= opcion_elim_jug <= len(nombres_juguetes):
                            break  
                        else:
                            print(f"\tOpcion no valida, debe estar en el rango de 1 a {len(nombres_juguetes)}, intentelo nuevamente: ", end="")
                    except ValueError:
                        print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")
            
                print(f"\n\tSe eliminara el juguete '{juguetes[opcion_elim_jug - 1].tipo_juguete}', estas seguro? (S/N) :  ", end="")
                
                while True:
                    
                    opcion_conf_elim = str(input())
                    if opcion_conf_elim.upper() != 'S' and opcion_conf_elim.upper() != 'N':
                        print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                    elif opcion_conf_elim.isdigit():
                        print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                    else:
                        break
 
                if opcion_conf_elim.upper() == 'S':

                    print("\n\tJuguete eliminado exitosamente")
        
                    juguetes.pop(opcion_elim_jug - 1)
                    unidades_prod.pop(opcion_elim_jug - 1)

                elif opcion_conf_elim.upper() == 'N':
                    eliminar_jug()

                time.sleep(1.1)

                print("\n\tDesea eliminar otro juguete? (S/si, N/no): ", end="")

                while True:
                    
                    opcion_elim_final = str(input())
                    if opcion_elim_final.upper() != 'S' and opcion_elim_final.upper() != 'N':
                        print("\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                    elif opcion_elim_final.isdigit():
                        print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                    else:
                        break

                if opcion_elim_final.upper() == 'S':

                    continue

                elif opcion_elim_final.upper() == 'N':

                    print("\n\tRegresando al menu principal...")

                    time.sleep(1.5)

                    menu_principal()

        case 2:

            k = 0

            os.system("cls")

            while True:

                print("\n\tLISTA DE FABRICAS...")

                time.sleep(2)

                nombres_fabricas = [fabrica.nombre_fabrica for fabrica in fabricas]

                for nom_pais in fabricas:
                    nom_pais.guardar_pais()

                indices = [f"Opcion {k + 1}:" for k in range(len(nombres_fabricas))]

                print("\n")

                dt_fabricas = pd.DataFrame({"Fabrica": nombres_fabricas,
                                            "Pais" : nombres_paises
                                           })
                dt_fabricas.index = indices

                print(dt_fabricas)

                print("\n\tIngrese la opcion en la que se encuentre la fabrica: ", end="")

                nombres_paises.clear()

                while True:
                    
                    try:
                        opcion_fabr = int(input())
                        if 1 <= opcion_fabr <= len(nombres_fabricas):
                            break  
                        else:
                            print(f"\tOpcion no valida, debe estar en el rango de 1 a {len(nombres_fabricas)}, intentelo nuevamente: ", end="")
                    except ValueError:
                        print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

                fabricas[opcion_fabr - 1].eliminar_jug()

                nombres_paises.clear()

                print("\n\tDesea eliminar el juguete de otra fabrica? (S/si, N/no): ", end="")

                while True:
                    
                    opcion_jug_final = str(input())
                    if opcion_jug_final.upper() != 'S' and opcion_jug_final.upper() != 'N':
                        print("\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                    elif opcion_jug_final.isdigit():
                        print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                    else:
                        break

                if opcion_jug_final.upper() == 'S':

                    continue

                elif opcion_jug_final.upper() == 'N':

                    print("\n\tRegresando al menu principal...")

                    time.sleep(1.5)

                    menu_principal()

        case 3:

            modificar_jug()

def designar_pais():

    os.system("cls")

    while True:

        print("\n\tLISTA DE FABRICAS...")

        time.sleep(2)

        nombres_fabricas = [fabrica.nombre_fabrica for fabrica in fabricas]

        for nom_pais in fabricas:
            nom_pais.guardar_pais()

        indices = [f"Opcion {k + 1}:" for k in range(len(nombres_fabricas))]

        print("\n")

        dt_fabricas = pd.DataFrame({"Fabrica": nombres_fabricas,
                                    "Pais" : nombres_paises
                                    })
        dt_fabricas.index = indices

        print(dt_fabricas)

        print("\n\tIngrese la opcion en la que se encuentre la fabrica: ", end="")

        nombres_paises.clear()

        while True:
                    
            try:
                opcion_fabr = int(input())
                if 1 <= opcion_fabr <= len(nombres_fabricas):
                    break  
                else:
                    print(f"\tOpcion no valida, debe estar en el rango de 1 a {k + 1}, intentelo nuevamente: ", end="")
            except ValueError:
                        print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

        fabricas[opcion_fabr - 1].mod_pais_dest()

        print("\n\tDesea modificar el juguete de otra fabrica? (S/si, N/no): ", end="")

        while True:
                    
            opcion_jug_final = str(input())
            if opcion_jug_final.upper() != 'S' and opcion_jug_final.upper() != 'N':
                print("\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
            elif opcion_jug_final.isdigit():
                print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
            else:
                break

        if opcion_jug_final.upper() == 'S':

            continue

        elif opcion_jug_final.upper() == 'N':

            print("\n\tRegresando al menu principal...")

            time.sleep(1.5)

            menu_principal()

def reportes():

    os.system("cls")

    k = 0

    print("\n\t-          MENU REPORTES          -")
    print("\t- Opcion 1: Mostrar fabricas      -")
    print("\t- Opcion 2: Mostrar juguetes      -")
    print("\t- Opcion 3: Impuestos e ingresos  -")
    print("\t- Opcion 4: Regresar              -")
    print("\t- Opcion 5: Cerrar sistema        -")

    print("\n\tIngrese la opcion que desee realizar: ", end="")

    while True:
                    
        try:
            opcion_reportes = int(input())
            if 1 <= opcion_reportes <= 5:
                break  
            else:
                print("\tOpcion no valida, debe estar en el rango de 1 a 5, intentelo nuevamente: ", end="")
        except ValueError:
            print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

    match opcion_reportes:

        case 1:

            nombres_paises.clear()
            impuesto_ori.clear()

            os.system("cls")

            if len(fabricas) == 0:
                print("\n\tNo hay fabricas registradas, por ende, no hay ingresos.")
                print("\tAgregue una fabrica, desea ir al menu 'agregar fabrica'? (S/N): ", end="")

                while True:
                    
                    opcion_no_fab = str(input())
                    if opcion_no_fab.upper() != 'S' and opcion_no_fab.upper() != 'N':
                        print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                    elif opcion_no_fab.isdigit():
                        print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                    else:
                        break

                if opcion_no_fab.upper() == 'S':

                    agregar_fabrica()       
                elif opcion_no_fab.upper() == 'N':

                    print("\n\tRegresando al menu principal...")

            print("\n\tLISTA DE FABRICAS...")

            time.sleep(2)

            nombres_fabricas = [fabrica.nombre_fabrica for fabrica in fabricas]

            for nom_pais in fabricas:
                nom_pais.guardar_pais()

            capacidad_prod = [cap_prod.cap_produccion for cap_prod in fabricas]

            for imp_org in fabricas:
                imp_org.impuesto_origen()

            indices = [f"Fabrica {k + 1}:" for k in range(len(nombres_fabricas))]

            print("\n")

            dt_fabricas = pd.DataFrame({"Fabrica": nombres_fabricas,
                                        "Pais" : nombres_paises,
                                        "Capacidad produccion" : capacidad_prod,
                                        "Impuesto origen (%)" : impuesto_ori
                                        })
            dt_fabricas.index = indices

            print(dt_fabricas)

            dt_fabricas.to_excel("fabricas.xlsx")

            print("\n\tDesea ver los graficos? (S/Si, N/No): ", end="")

            while True:
                    
                opcion_no_fab = str(input())
                if opcion_no_fab.upper() != 'S' and opcion_no_fab.upper() != 'N':
                    print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                elif opcion_no_fab.isdigit():
                    print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                else:
                    break
   
            if opcion_no_fab.upper() == 'N':

                print("\n\tRegresando al menu principal...")

                time.sleep(1.5)

                menu_principal()

            # --- GRAFICO PAISES -----

            print("\n\tCreando el grafico de barras...")

            time.sleep(2)

            valores_pais = []

            for pais in nombres_paises:

                valores_pais.append(nombres_paises.count(pais))

            plt.bar(nombres_paises, valores_pais, color = "blue")

            plt.title("Paises")
            plt.xlabel("Pais")
            plt.ylabel("Cantidad de fabricas")

            plt.show()

            valores_pais.clear()

            # --- GRAFICO CAPACIDAD DE PRODUCCION ---

            print("\n\tCreando el grafico de lineas...")

            time.sleep(2)

            plt.plot(nombres_fabricas, capacidad_prod, marker = "o", linestyle = "-", color = "r")

            plt.title("Capacidad de produccion")
            plt.xlabel("Nombres de las fabricas")
            plt.ylabel("Capacidad de produccion")

            plt.show()

            capacidad_prod.clear()

            # --- GRAFICO % IMPUESTO

            print("\n\tCreando el grafico de lineas...")

            time.sleep(2)

            plt.plot(nombres_fabricas, impuesto_ori, marker = "o", linestyle = "-", color = "y")

            plt.title("Porcentaje de impuesto")
            plt.xlabel("Nombre de las fabricas")
            plt.ylabel("Porcentaje impuesto")

            plt.show()

            print("\n\tRegresando al menu principal...")

            nombres_paises.clear()
            impuesto_ori.clear()
            nombres_fabricas.clear()
            capacidad_prod.clear()
            indices.clear()

            time.sleep(1.5)

            menu_principal()

        case 2:

            if len(fabricas) == 0:
                print("\n\tNo hay fabricas registradas, por ende, no hay juguetes aun")
                print("\tAgregue una fabrica, desea ir al menu 'agregar fabrica'? (S/N): ", end="")

                while True:
                    
                    opcion_no_jug = str(input())
                    if opcion_no_jug.upper() != 'S' and opcion_no_jug.upper() != 'N':
                        print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                    elif opcion_no_jug.isdigit():
                        print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                    else:
                        break

                if opcion_no_jug.upper() == 'S':

                    agregar_fabrica()       
                elif opcion_no_jug.upper() == 'N':

                    print("\n\tRegresando al menu principal...")

                    time.sleep(1.5)

                    menu_principal()

            while True:

                nombres_paises.clear()
                impuesto_ori.clear()

                os.system("cls")

                print("\n\tLISTA DE FABRICAS...")

                time.sleep(2)

                nombres_fabricas = [fabrica.nombre_fabrica for fabrica in fabricas]

                for nom_pais in fabricas:
                    nom_pais.guardar_pais()

                capacidad_prod = [cap_prod.cap_produccion for cap_prod in fabricas]

                for imp_org in fabricas:
                    imp_org.impuesto_origen()

                indices = [f"Opcion {k + 1}:" for k in range(len(nombres_fabricas))]

                print("\n")

                dt_fabricas = pd.DataFrame({"Fabrica": nombres_fabricas,
                                            "Pais" : nombres_paises,
                                            "Capacidad produccion" : capacidad_prod,
                                            "Impuesto origen (%)" : impuesto_ori
                                            })
                dt_fabricas.index = indices

                print(dt_fabricas)

                print("\n\tIngrese la opcion en la que se encuentre la fabrica: ", end="")

                nombres_paises.clear()

                while True:
                    
                    try:
                        opcion_most_list = int(input())
                        if 1 <= opcion_most_list <= len(nombres_fabricas):
                            break  
                        else:
                            print(f"\tOpcion no valida, debe estar en el rango de 1 a {len(nombres_fabricas)}, intentelo nuevamente: ", end="")
                    except ValueError:
                        print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")
            
                fabricas[opcion_most_list - 1].mostrar_juguetes()

                print("\n\tDesea ver los reportes de los juguetes de otra fabrica? (S/si, N/no): ", end="")

                while True:
                    
                    opcion_jug_final = str(input())
                    if opcion_jug_final.upper() != 'S' and opcion_jug_final.upper() != 'N':
                        print("\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                    elif opcion_jug_final.isdigit():
                        print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                    else:
                        break

                if opcion_jug_final.upper() == 'S':

                    continue

                elif opcion_jug_final.upper() == 'N':

                    print("\n\tRegresando al menu principal...")

                    time.sleep(1.5)

                    menu_principal()

        case 3:

            if len(fabricas) == 0:
                print("\n\tNo hay fabricas registradas, es posible que todos hayan sido eliminados,")
                print("\tagregue un juguete, desea ir al menu 'agregar fabrica'? (S/N): ", end="")

                while True:
                    
                    opcion_no_fab = str(input())
                    if opcion_no_fab.upper() != 'S' and opcion_no_fab.upper() != 'N':
                        print(f"\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                    elif opcion_no_fab.isdigit():
                        print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                    else:
                        break

                if opcion_no_fab.upper() == 'S':

                    agregar_fabrica()       
                elif opcion_no_fab.upper() == 'N':

                    print("\n\tRegresando al menu principal...")

                    time.sleep(1.5)

                    menu_principal()

            os.system("cls")

            print("\n\t-           CALCULAR           -")
            print("\t- Opcion 1: Calcular impuestos -")
            print("\t- Opcion 2: Calcular ingresos  -")
            print("\t- Opcion 3: Regresar           -")

            print("\n\tIngrese la opcion que desee realizar: ", end="")

            while True:
                    
                try:
                    opcion_calculos = int(input())
                    if 1 <= opcion_calculos <= 5:
                        break  
                    else:
                        print("\tOpcion no valida, debe estar en el rango de 1 a 5, intentelo nuevamente: ", end="")
                except ValueError:
                    print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

            match opcion_calculos:

                case 1:

                    while True:

                        nombres_paises.clear()
                        impuesto_ori.clear()

                        os.system("cls")

                        print("\n\tLISTA DE FABRICAS...")

                        time.sleep(2)

                        nombres_fabricas = [fabrica.nombre_fabrica for fabrica in fabricas]

                        for nom_pais in fabricas:
                            nom_pais.guardar_pais()

                        capacidad_prod = [cap_prod.cap_produccion for cap_prod in fabricas]

                        for imp_org in fabricas:
                            imp_org.impuesto_origen()

                        indices = [f"Opcion {k + 1}:" for k in range(len(nombres_fabricas))]

                        print("\n")

                        dt_fabricas = pd.DataFrame({"Fabrica": nombres_fabricas,
                                                    "Pais" : nombres_paises,
                                                    "Capacidad produccion" : capacidad_prod,
                                                    "Impuesto origen (%)" : impuesto_ori
                                                    })
                        dt_fabricas.index = indices

                        print(dt_fabricas)

                        print("\n\tIngrese la opcion en la que se encuentre la fabrica: ", end="")

                        nombres_paises.clear()

                        while True:
                    
                            try:
                                opcion_most_list = int(input())
                                if 1 <= opcion_most_list <= len(nombres_fabricas):
                                    break  
                                else:
                                    print(f"\tOpcion no valida, debe estar en el rango de 1 a {len(nombres_fabricas)}, intentelo nuevamente: ", end="")
                            except ValueError:
                                print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")        

                        fabricas[opcion_most_list - 1].calcular_impuesto()

                        print("\n\tDesea ver los impuestos totales de otra fabrica? (S/si, N/no): ", end="")

                        while True:
                    
                            opcion_jug_final = str(input())
                            if opcion_jug_final.upper() != 'S' and opcion_jug_final.upper() != 'N':
                                print("\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                            elif opcion_jug_final.isdigit():
                                print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                            else:
                                break

                        if opcion_jug_final.upper() == 'S':

                            continue

                        elif opcion_jug_final.upper() == 'N':

                            print("\n\tRegresando al menu principal...")

                            time.sleep(1.5)

                            menu_principal()

                case 2:

                    while True:

                        nombres_paises.clear()
                        impuesto_ori.clear()

                        os.system("cls")

                        print("\n\tLISTA DE FABRICAS...")

                        time.sleep(2)

                        nombres_fabricas = [fabrica.nombre_fabrica for fabrica in fabricas]

                        for nom_pais in fabricas:
                            nom_pais.guardar_pais()

                        capacidad_prod = [cap_prod.cap_produccion for cap_prod in fabricas]

                        for imp_org in fabricas:
                            imp_org.impuesto_origen()

                        indices = [f"Opcion {k + 1}:" for k in range(len(nombres_fabricas))]

                        print("\n")

                        dt_fabricas = pd.DataFrame({"Fabrica": nombres_fabricas,
                                                    "Pais" : nombres_paises,
                                                    "Capacidad produccion" : capacidad_prod,
                                                    "Impuesto origen (%)" : impuesto_ori
                                                    })
                        dt_fabricas.index = indices

                        print(dt_fabricas)

                        print("\n\tIngrese la opcion en la que se encuentre la fabrica: ", end="")

                        nombres_paises.clear()

                        while True:
                    
                            try:
                                opcion_most_list = int(input())
                                if 1 <= opcion_most_list <= len(nombres_fabricas):
                                    break  
                                else:
                                    print(f"\tOpcion no valida, debe estar en el rango de 1 a {len(nombres_fabricas)}, intentelo nuevamente: ", end="")
                            except ValueError:
                                print("\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")        

                        fabricas[opcion_most_list - 1].calcular_ingresos()

                        print("\n\tDesea ver los ingresos totales de otra fabrica? (S/si, N/no): ", end="")

                        while True:
                    
                            opcion_jug_final = str(input())
                            if opcion_jug_final.upper() != 'S' and opcion_jug_final.upper() != 'N':
                                print("\tOpcion no valida, debe ser (S/N), intentelo nuevamente: ", end="")
                            elif opcion_jug_final.isdigit():
                                print("\tOpcion no valida, debe ser un caracter (S/N), intentelo nuevamente: ", end="")  
                            else:
                                break

                        if opcion_jug_final.upper() == 'S':

                            continue

                        elif opcion_jug_final.upper() == 'N':

                            print("\n\tRegresando al menu principal...")

                            time.sleep(1.5)

                            menu_principal()

                case 3:

                    reportes()

        case 4:

            menu_principal()

        case 5:

            exit()

menu_principal()    