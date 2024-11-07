import os

autos = []
propietarios = []
ubicaciones_disp = [True, True, True, True, True, True, True, True]
autos_parqueados = []
nro_parqueo = []
horas = []
minutos = []
pabellon = ""
num_lugar = 0
monto_total = []

class Auto:
    def __init__(self, marca, modelo, color, placa):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__placa = placa

    @property
    def guardar_marca(self):
        return self.__marca
    
    @guardar_marca.setter
    def guardar_marca(self, marca):
        self.__marca = marca

    @property
    def guardar_modelo(self):
        return self.__modelo
    
    @guardar_modelo.setter
    def guardar_modelo(self, modelo):
        self.__modelo = modelo

    @property
    def guardar_color(self):
        return self.__color
    
    @guardar_color.setter
    def guardar_color(self, color):
        self.__color = color

    @property
    def guardar_placa(self):
        return self.__placa
    
    @guardar_placa.setter
    def guardar_placa(self, placa):
        self.__placa = placa

    def mostrar_placas(self):
        
        print(self.__placa)

    def mostrar_datos_auto(self):
        print(self.__placa, "\t", self.__marca, "\t", self.__modelo, "\t\t", self.__color, sep="", end="")

class Propietario:
    def __init__(self, dni:int, nombre, apellido, telefono:int):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__telefono = telefono

    @property
    def registrar_dni(self):
        return self.__dni
    
    @registrar_dni.setter
    def registrar_dni(self, dni):
        self.__dni = dni

    @property
    def registrar_nombre(self):
        return self.__nombre
    
    @registrar_nombre.setter
    def registrar_nombre(self, nombre):
        self.__nombre = nombre

    @property
    def registrar_apellido(self):
        return self.__apellido
    
    @registrar_apellido.setter
    def registrar_apellido(self, apellido):
        self.__apellido = apellido

    @property
    def registrar_telefono(self):
        return self.__telefono
    
    @registrar_telefono.setter
    def registrar_telefono(self, telefono):
        self.__telefono = telefono

    def mostrar_dni(self):
        print(self.__dni)

    def mostrar_datos_prop(self):
        print(self.__nombre, " ", self.__apellido, "\t\t", self.__dni, "\t", self.__telefono, sep="")

class Parqueo:

    def __init__(self, num_parqueo, ubicacion, placa, dni, hora_inicio, hora_fin, monto):
        self.__num_parqueo = num_parqueo
        self.__ubicacion = ubicacion
        self.__placa = placa
        self.__dni = dni
        self.__hora_inicio = hora_inicio
        self.__hora_fin = hora_fin
        self.__monto = monto
    
    @property
    def grabar_num_parqueo(self):
        return self.__num_parqueo
    
    @grabar_num_parqueo.setter
    def grabar_num_parqueo(self, num_parqueo):
        self.__num_parqueo = num_parqueo

    @property
    def grabar_ubicacion(self):
        return self.__ubicacion
    
    @grabar_ubicacion.setter
    def grabar_ubicacion(self, ubicacion):
        self.__ubicacion = ubicacion

    @property
    def grabar_placa(self):
        return self.__placa
    
    @grabar_placa.setter
    def grabar_placa(self, placa):
        self.__placa = placa

    @property
    def grabar_dni(self):
        return self.__dni
    
    @grabar_dni.setter
    def grabar_dni(self, dni):
        self.__dni = dni

    @property
    def grabar_hora_inicio(self):
        return self.__hora_inicio
    
    @grabar_hora_inicio.setter
    def grabar_hora_inicio(self, hora_inicio):
        self.__hora_inicio = hora_inicio

    @property
    def grabar_hora_fin(self):
        return self.__hora_fin
    
    @grabar_hora_fin.setter
    def grabar_hora_fin(self, hora_fin):
        self.__hora_fin = hora_fin

    @property
    def grabar_monto(self):
        return self.__monto
    
    @grabar_monto.setter
    def grabar_monto(self, monto):
        self.__monto = monto

        
def menu_principal(pabellon, num_lugar):

    os.system("cls")

    u = True

    print('\t-    PARQUEO "TU TRANQUILO, YO NERVIOSO"   -')
    print("\tOpcion 1: Ingresar auto")
    print("\tOpcion 2: Ingresar propietario")
    print("\tOpcion 3: Ingreso parqueo")
    print("\tOpcion 4: Salida parqueo")
    print("\tOpcion 5: Mostrar reportes")
    print("\tOpcion 6: Salir")

    print("\n\tIngrese la opcion a elegir: ", end="")

    opcion = int(input())

    if opcion < 1 or opcion > 6:
        while u:
            opcion = int(input("\n\topcion no valida, intentelo nuevamente ->: "))

            if 0 < opcion < 7:
                u = False

    match opcion:
        case 1:
            registrar_auto(pabellon, num_lugar)
        case 2:
            ingresar_propietario(pabellon, num_lugar)
        case 3:
            ingreso_parqueo()
        case 4:
            salida_parqueo(pabellon, num_lugar)
        case 5:
            mostrar_reportes(pabellon, num_lugar)
        case 6:
            exit()

def registrar_auto(pabellon, num_lugar):

    os.system("cls")

    marca = input("Ingrese la marca del auto: ")
    modelo = input("Ingrese el modelo del auto: ")
    color = input("Ingrese el color del auto: ")
    placa = input("Ingrese la placa del auto: ")

    autos.append(Auto(marca, modelo, color, placa))

    print("\n\tAuto registrado exitosamente!")

    print("\n\tOpcion 1: Ingresar propietario")
    print("\tOpcion 2: Ingreso parqueo")
    print("\tOpcion 3: Regresar al menu principal")
    print("\tOpcion 4: Salir")

    print("\n\tQue desea hacer ahora? ", end="")
    opcion = int(input())

    match opcion:
        case 1:
            ingresar_propietario(pabellon, num_lugar)
        case 2:
            ingreso_parqueo()
        case 3:
            menu_principal(pabellon, num_lugar)
        case 4:
            exit()

def ingresar_propietario(pabellon, num_lugar):

    os.system("cls")
    i = True

    dni = input("Ingrese el DNI del propietario: ")
    
    while i:
        if dni.isdigit() and 10000000 < int(dni) < 99999999:
            i = False
        else:
            dni = input("DNI no valido, ingrese correctamente su DNI (8 digitos): ")

    nombre = input("Ingrese el nombre del propietario: ")
    apellido = input("Ingrese el apellido del propietario: ")
    telefono = input("Ingrese el telefono del propietario: ")

    while i:
        if telefono.isdigit() and 900000000 < int(telefono) < 999999999:
            i = False
        else:
            telefono = input("Telefono no valido, ingrese correctamente su telefono (9 digitos): ")

    propietarios.append(Propietario(dni, nombre, apellido, telefono))

    print("\n\tPropietario registrado exitosamente!")

    print("\n\tOpcion 1: Ingresar auto")
    print("\tOpcion 2: Ingreso parqueo")
    print("\tOpcion 3: Regresar al menu principal")
    print("\tOpcion 4: Salir")

    print("\n\tQue desea hacer ahora? ", end="")
    opcion = int(input())

    match opcion:
        case 1:
            registrar_auto(pabellon, num_lugar)
        case 2:
            ingreso_parqueo()
        case 3:
            menu_principal(pabellon, num_lugar)
        case 4:
            exit()

def ingreso_parqueo():

    os.system("cls")

    i = True
    u = 0
    contador = 0

    if len(autos) == 0 or len(propietarios) == 0:
        print("\tAun no hay autos y/o propietarios registrados")

        print("\n\tOpcion 1: Ingresar auto")
        print("\tOpcion 2: Ingreso propietario")
        print("\tOpcion 3: Regresar al menu principal")
        print("\tOpcion 4: Salir")

        print("\n\tQue desea hacer ahora? ", end="")
        opcion = int(input())

        match opcion:
            case 1:
                return registrar_auto(pabellon, num_lugar)
            case 2:
                return ingresar_propietario(pabellon, num_lugar)
            case 3:
                return menu_principal(pabellon, num_lugar)
            case 4:
                return exit()
    
    while u < 8:
        if ubicaciones_disp[u] == False:
            contador += 1

        u += 1

    u = 0

    if contador == 8:
        print("\tYa no hay espacios disponibles")

        print("\n\tOpcion 1: Salida parqueo")
        print("\tOpcion 2: Regresar al menu principal")
        print("\tOpcion 3: Salir")

        print("\n\tQue desea hacer ahora? ", end="")
        opcion = int(input())

        match opcion:
            case 1:
                return salida_parqueo(pabellon, num_lugar)
            case 2:
                return menu_principal(pabellon, num_lugar)
            case 3:
                return exit()

    print("\t\t------------------")

    print("\t\t| ", end="")
    if ubicaciones_disp[0] == True:
        print("\033[32m", "A1    ", sep="", end="")
        if ubicaciones_disp[4] == True:
            print("      B1 ", "\033[37m", "|", sep="")
        else:
            print("\033[31m", "      B1 ", "\033[37m", "|", sep="")
    else:
        print("\033[31m", "A1    ", sep="", end="")
        if ubicaciones_disp[4] == True:
            print("\033[32m", "      B1 ", "\033[37m", "|", sep="")
        else:
            print("      B1 ", "\033[37m", "|", sep="")

    print("\t\t------      ------")

    print("\t\t| ", end="")
    if ubicaciones_disp[1] == True:
        print("\033[32m", "A2    ", sep="", end="")
        if ubicaciones_disp[5] == True:
            print("      B2 ", "\033[37m", "|", sep="")
        else:
            print("\033[31m", "      B2 ", "\033[37m", "|", sep="")
    else:
        print("\033[31m", "A2    ", sep="", end="")
        if ubicaciones_disp[5] == True:
            print("\033[32m", "      B2 ", "\033[37m", "|", sep="")
        else:
            print("      B2 ", "\033[37m", "|", sep="")

    print("\t\t------      ------")

    print("\t\t| ", end="")
    if ubicaciones_disp[2] == True:
        print("\033[32m", "A3    ", sep="", end="")
        if ubicaciones_disp[6] == True:
            print("      B3 ", "\033[37m", "|", sep="")
        else:
            print("\033[31m", "      B3 ", "\033[37m", "|", sep="")
    else:
        print("\033[31m", "A2    ", sep="", end="")
        if ubicaciones_disp[6] == True:
            print("\033[32m", "      B3 ", "\033[37m", "|", sep="")
        else:
            print("      B3 ", "\033[37m", "|", sep="")

    print("\t\t------      ------")

    print("\t\t| ", end="")
    if ubicaciones_disp[3] == True:
        print("\033[32m", "A4    ", sep="", end="")
        if ubicaciones_disp[7] == True:
            print("      B4 ", "\033[37m", "|", sep="")
        else:
            print("\033[31m", "      B4 ", "\033[37m", "|", sep="")
    else:
        print("\033[31m", "A4    ", sep="", end="")
        if ubicaciones_disp[7] == True:
            print("\033[32m", "      B4 ", "\033[37m", "|", sep="")
        else:
            print("      B4 ", "\033[37m", "|", sep="")

    print("\t\t------      ------")

    pabellon = input("\tIngrese el pabellon (A o B) en el que desea parquearse: ")

    while i:
        if pabellon.upper() != "A" and pabellon.upper() != "B":    
            pabellon = input("\tPabellon no encontrado, ingrese el pabellon (A o B) en el que desea parquearse: ")
        elif pabellon.upper() == "A":
            if ubicaciones_disp[0] == False and ubicaciones_disp[1] == False and ubicaciones_disp[2] == False and ubicaciones_disp[3] == False:
                pabellon = input("\tPabellon no disponible, ingrese el pabellon (A o B) en el que desea parquearse: ")
            else:
                i = False
        elif pabellon.upper() == "B":
            if ubicaciones_disp[4] == False and ubicaciones_disp[5] == False and ubicaciones_disp[6] == False and ubicaciones_disp[7] == False:
                pabellon = input("\tPabellon no disponible, ingrese el pabellon (A o B) en el que desea parquearse: ")
            else:
                i = False
        else:
            i = False

    i = True

    num_lugar = int(input("\tIngrese el numero del lugar en el que desea parquearse: "))

    while i:
        if num_lugar < 1 or num_lugar > 4:
            num_lugar = int(input("\tNumero no encontrado, ingrese el numero del lugar en el que desea parquearse: "))
        elif pabellon.upper() == "A":
            if ubicaciones_disp[num_lugar - 1] == False:
                num_lugar = int(input("\tNumero no disponible, ingrese el numero del lugar en el que desea parquearse: "))
            else:
                i = False
        elif pabellon.upper() == "B":
            if ubicaciones_disp[num_lugar + 3] == False:
                num_lugar = int(input("\tNumero no disponible, ingrese el numero del lugar en el que desea parquearse: "))
            else:
                i = False
        else:
            i = False

    i = True

    print("\n\tAutos disponibles:")
    print("\n\t        Placa")

    while u < len(autos):

        print(f"\tAuto {u + 1}: ", end="")
            
        autos[u].mostrar_placas()

        u += 1

    u = 0

    opcion_auto_prop = int(input("Ingrese el numero del auto que sera parqueado (solo numero, NO PLACA): "))

    while i:
        if opcion_auto_prop < 1 or opcion_auto_prop > len(autos):
            opcion_auto_prop = int(input("Numero ingresado no valido (solo numero, NO PLACA), intentelo nuevamente: "))
        else:
            i = False

    i = True

    print("\n\tAuto", opcion_auto_prop, "de placa: ", end="")
    autos[opcion_auto_prop - 1].mostrar_placas()
    print("\tDNI del propietario: ", end="")
    propietarios[opcion_auto_prop - 1].mostrar_dni()

    num_parqueo = input("Ingrese un nombre o un numero al parqueo registrado: ")

    nro_parqueo.append(num_parqueo)

    if pabellon.upper() == "A":
        ubicaciones_disp[num_lugar - 1] = False
    elif pabellon.upper() == "B":
        ubicaciones_disp[num_lugar + 3] = False

    autos_parqueados.append(autos[opcion_auto_prop - 1])

    hora_ingreso = int(input("Ingrese SOLO la hora en la que esta ingresando el auto: "))
    min_ingreso = int(input("Ingrese SOLO los minutos en los que esta ingresando el auto: "))

    horas.append(hora_ingreso)
    minutos.append(min_ingreso)

    print("\n\tRegistro exitoso!")

    print("\n\tOpcion 1: Salida parqueo")
    print("\tOpcion 2: Regresar al menu principal")
    print("\tOpcion 3: Salir")

    print("\n\tQue desea hacer ahora? ", end="")
    opcion = int(input())

    match opcion:
        case 1:
            return salida_parqueo(pabellon, num_lugar)
        case 2:
            return menu_principal(pabellon, num_lugar)
        case 3:
            return exit()

def salida_parqueo(pabellon, num_lugar):

    os.system("cls")

    i = True

    if len(autos_parqueados) == 0:
        print("\tAun no hay autos parqueados")

        print("\n\tOpcion 1: Ingresar auto")
        print("\tOpcion 2: Ingreso propietario")
        print("\tOpcion 3: Regresar al menu principal")
        print("\tOpcion 4: Salir")

        print("\n\tQue desea hacer ahora? ", end="")
        opcion = int(input())

        match opcion:
            case 1:
                return registrar_auto(pabellon, num_lugar)
            case 2:
                return ingresar_propietario(pabellon, num_lugar)
            case 3:
                return menu_principal(pabellon, num_lugar)
            case 4:
                return exit()

    u = 0

    print("\n\tAutos disponibles:")
    print("\n\t        Placa")

    while u < len(autos_parqueados):

        print(f"\tAuto {u + 1}: ", end="")
            
        autos_parqueados[u].mostrar_placas()

        u += 1

    u = 0

    opcion_auto_prop = int(input("Ingrese el numero del auto que sera retirado (solo numero, NO PLACA): "))

    while i:
        if opcion_auto_prop < 1 or opcion_auto_prop > len(autos_parqueados):
            opcion_auto_prop = int(input("Numero ingresado no valido (solo numero, NO PLACA), intentelo nuevamente: "))
        else:
            i = False

    i = True

    hora_fin = int(input("Ingrese SOLO la hora en la que esta saliendo el auto: "))
    min_fin = int(input("Ingrese SOLO los miutos en los que esta saliendo el auto: "))

    if min_fin <= minutos[opcion_auto_prop - 1]:
        monto = (((hora_fin - horas[opcion_auto_prop - 1])*60) + (min_fin - minutos[opcion_auto_prop - 1])) * 0.15
    else:
        monto = (((hora_fin - horas[opcion_auto_prop - 1])*60) - (minutos[opcion_auto_prop - 1] - min_fin)) * 0.15

    monto_total.append(monto)

    if pabellon.upper() == "A":
        ubicaciones_disp[num_lugar - 1] = True
    elif pabellon.upper() == "B":
        ubicaciones_disp[num_lugar + 3] = True

    autos_parqueados.pop(opcion_auto_prop - 1)

    print("\n\tLa salida fue registrada correctamente!")
    print("\tEl monto a pagar es:", monto)
    print("\tGracias por su preferencia")

    print("\n\tOpcion 1: Ingresar auto")
    print("\tOpcion 2: Mostrar reportes")
    print("\tOpcion 3: Regresar al menu principal")
    print("\tOpcion 4: Salir")

    print("\n\tQue desea hacer ahora? ", end="")
    opcion = int(input())

    match opcion:
        case 1:
            return registrar_auto(pabellon, num_lugar)
        case 2:
            return mostrar_reportes(pabellon, num_lugar)
        case 3:
            return menu_principal(pabellon, num_lugar)
        case 4:
            return exit()
        
def mostrar_reportes(pabellon, num_lugar):

    os.system("cls")
    
    u = True
    i = 0
    
    print("\t-                   REPORTES                    -")
    print("\tOpcion 1: Lista de autos y propietarios registrados")
    print("\tOpcion 2: Monto total recaudado y parqueos por dia")
    print("\tOpcion 3: Regresar al menu principal")
    print("\tOpcion 4: Salir")

    print("\n\tIngrese la opcion a elegir: ", end="")

    opcion = int(input())

    if opcion < 1 or opcion > 5:
        while u:
            opcion = int(input("\n\topcion no valida, intentelo nuevamente ->: "))

            if 0 < opcion < 6:
                u = False

    u = True

    match opcion:
        case 1:

            if len(autos) == 0:
            
                print("\tAun no hay autos registrados")

                print("\n\tOpcion 1: Ingresar auto")
                print("\tOpcion 2: Ingreso propietario")
                print("\tOpcion 3: Regresar al menu principal")
                print("\tOpcion 4: Salir")

                print("\n\tQue desea hacer ahora? ", end="")
                opcion_final = int(input())

                match opcion_final:
                    case 1:
                        return registrar_auto(pabellon, num_lugar)
                    case 2:
                        return ingresar_propietario(pabellon, num_lugar)
                    case 3:
                        return menu_principal(pabellon, num_lugar)
                    case 4:
                        return exit()
            else:
                print("\n\t\t Placa\t\tMarca\t\tModelo\t\tColor\t\tPropietario\t\tDNI\t\tNum. telefono")
            
                while i < len(autos):
            
                    print("\tAuto", i + 1, ": ", end="")
                    autos[i].mostrar_datos_auto()
                    print("\t", end="")
                    propietarios[i].mostrar_datos_prop()

                    i += 1

                print("\n\tOpcion 1: Regresar al menu principal")
                print("\tOpcion 2: Salir")

                print("\n\tQue desea hacer ahora? ", end="")
                opcion_final = int(input())

                if opcion < 1 or opcion > 2:
                    while u:
                        opcion = int(input("\n\topcion no valida, intentelo nuevamente ->: "))

                        if 0 < opcion < 3:
                            u = False

                u = True

                match opcion_final:
                    case 1:
                        return menu_principal(pabellon, num_lugar)
                    case 2:
                        return exit()

        case 2:
            print("\n\tMonto total recaudado:", sum(monto_total))
            print("\tParqueos por dia:", len(autos))

            print("\n\tOpcion 1: Regresar al menu principal")
            print("\tOpcion 2: Salir")

            print("\n\tQue desea hacer ahora? ", end="")
            opcion_final = int(input())

            if opcion < 1 or opcion > 2:
                while u:
                    opcion = int(input("\n\topcion no valida, intentelo nuevamente ->: "))

                    if 0 < opcion < 3:
                        u = False

            u = True

            match opcion_final:
                case 1:
                    return menu_principal(pabellon, num_lugar)
                case 2:
                    return exit()
        case 3:
            menu_principal(pabellon, num_lugar)
        case 4:
            exit()

menu_principal(pabellon, num_lugar)