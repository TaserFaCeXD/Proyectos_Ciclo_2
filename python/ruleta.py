import random
import os
import time

saldo = float(input("Ingrese la cantidad a depositar ->: "))
i = 0

def menu_principal():
    print("\t-             RULETA             -")
    print("\tOpcion 1: 1-18/19-36 ......... x2")
    print("\tOpcion 2: 1-12/13-24/25-36 ... x3")
    print("\tOpcion 3: Rojo/Negro ......... x2")
    print("\tOpcion 4: Par/Impar .......... x2")
    print("\tOpcion 5: Cualquier numero ... x31")
    print("\tOpcion 6: Salir")

    opcion = int(input("Ingrese la opcion a elegir: "))

    os.system("cls")

    menu_opcion(opcion)

def menu_opcion(opcion):

    match opcion:
        case 1:

            print("\t-             RULETA             -")
            print("\tOpcion 1: 1-18 ............... x2")
            print("\tOpcion 2: 19-36 .............. x2")
            print("\tOpcion 3: Regresar")

            opcion_1 = int(input("Ingrese la opcion a elegir "))

            while i < 0:
                if opcion_1 > 3 or opcion_1 < 1:
                    opcion_1 = int(input("Opcion no valida, intentelo nuevamente: "))
                else:
                    i += 1

            i = 0

            match opcion_1:
                case 1:
                    apuesta = float(input("Ingrese la cantidad a apostar: "))

                    while i < 0:
                        if apuesta > saldo or apuesta < 0:
                            apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                        else:
                            i += 1

                    i = 0
                

                case 2:
                    
                    apuesta = float(input("Ingrese la cantidad a apostar: "))

                    while i < 0:
                        if apuesta > saldo or apuesta < 0:
                            apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                        else:
                            i += 1

                    i = 0
                
                case 3:

                    os.system("cls")

                    menu_principal()

        case 2:

            print("\t-             RULETA             -")
            print("\tOpcion 1: 1-12 ............... x3")
            print("\tOpcion 2: 13-24 .............. x3")
            print("\tOpcion 3: 25-36 .............. x3")
            print("\tOpcion 4: Regresar")

            opcion_1 = int(input("Ingrese la opcion a elegir "))

            while i < 0:
                if opcion_1 > 4 or opcion_1 < 1:
                    opcion_1 = int(input("Opcion no valida, intentelo nuevamente: "))
                else:
                    i += 1

            i = 0

            match opcion_1:
                case 1:
                    apuesta = float(input("Ingrese la cantidad a apostar: "))

                    while i < 0:
                        if apuesta > saldo or apuesta < 0:
                            apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                        else:
                            i += 1

                    i = 0
                

                case 2:
                    
                    apuesta = float(input("Ingrese la cantidad a apostar: "))

                    while i < 0:
                        if apuesta > saldo or apuesta < 0:
                            apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                        else:
                            i += 1

                    i = 0
                
                case 3:

                    apuesta = float(input("Ingrese la cantidad a apostar: "))

                    while i < 0:
                        if apuesta > saldo or apuesta < 0:
                            apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                        else:
                            i += 1

                    i = 0

                case 4:

                    os.system("cls")

                    menu_principal()

        case 3:

            print("\t-             RULETA             -")
            print("\tOpcion 1: Rojo ............... x2")
            print("\tOpcion 2: Negro .............. x2")
            print("\tOpcion 3: Regresar")

            opcion_1 = int(input("Ingrese la opcion a elegir "))

            while i < 0:
                if opcion_1 > 4 or opcion_1 < 1:
                    opcion_1 = int(input("Opcion no valida, intentelo nuevamente: "))
                else:
                    i += 1

            i = 0

            match opcion_1:
                case 1:

                    apuesta = float(input("Ingrese la cantidad a apostar: "))

                    while i < 0:
                        if apuesta > saldo or apuesta < 0:
                            apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                        else:
                            i += 1

                    i = 0
                

                case 2:
                    
                    apuesta = float(input("Ingrese la cantidad a apostar: "))

                    while i < 0:
                        if apuesta > saldo or apuesta < 0:
                            apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                        else:
                            i += 1

                    i = 0
                
                case 3:

                    os.system("cls")

                    menu_principal()

        case 4:

            print("\t-             RULETA             -")
            print("\tOpcion 1: Par ............... x2")
            print("\tOpcion 2: Impar .............. x2")
            print("\tOpcion 3: Regresar")

            opcion_1 = int(input("Ingrese la opcion a elegir "))

            while i < 0:
                if opcion_1 > 4 or opcion_1 < 1:
                    opcion_1 = int(input("Opcion no valida, intentelo nuevamente: "))
                else:
                    i += 1

            i = 0

            match opcion_1:
                case 1:

                    apuesta = float(input("Ingrese la cantidad a apostar: "))

                    while i < 0:
                        if apuesta > saldo or apuesta < 0:
                            apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                        else:
                            i += 1

                    i = 0
                

                case 2:
                    
                    apuesta = float(input("Ingrese la cantidad a apostar: "))

                    while i < 0:
                        if apuesta > saldo or apuesta < 0:
                            apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                        else:
                            i += 1

                    i = 0
                
                case 3:

                    os.system("cls")

                    menu_principal()

        case 5:
            
            print("\t |   |", "\033[31m", " 1 ", "\033[37m", "| 4 |", "\033[31m", " 7 ", "\033[37m", "| 10 | 13 |", "\033[31m", " 16 ", "\033[37m", "|", 
            "\033[31m", " 19 ", "\033[37m", "| 22 |", "\033[31m", " 25 ", "\033[37m", "| 28 | 31 |", "\033[31m", " 34 ", "\033[37m", "|", sep="")
            print("\t\033[37m", " |", "\033[32m", " 0 ", "\033[37m", "| 2 |", "\033[31m", " 5 ", "\033[37m", "| 8 | 11 |", "\033[31m", " 14 ", "\033[37m", 
            "| 17 | 20 |", "\033[31m", " 23 ", "\033[37m", "| 26 | 29 |", "\033[31m", " 32 ", "\033[37m", "| 35 |", sep="")
            print("\t\033[37m", " |   |", "\033[31m", " 3 ", "\033[37m", "| 6 |", "\033[31m", " 9 ", "\033[37m", "|", "\033[31m", " 12 ", "\033[37m", "| 15 |", 
            "\033[31m", " 18 ", "\033[37m", "|", "\033[31m", " 21 ", "\033[37m", "| 24 |", "\033[31m", " 27 ", "\033[37m", "|", "\033[31m", " 30 ", "\033[37m", "| 33 |", "\033[31m", " 36 ", "\033[37m", "|", sep="")

            num_jugador = int(input("Ingrese el numero a apostar "))

            while i < 0:
                if num_jugador > 36 or num_jugador < 0:
                    num_jugador = int(input("Numero ingresado no valido, intentelo nuevamente: "))
                else:
                    i += 1

            i = 0

            apuesta = float(input("Ingrese la cantidad a apostar: "))

            while i < 0:
                if apuesta > saldo or apuesta < 0:
                    apuesta = float(input("La cantidad ingresada no es valida, intentelo nuevamente: "))
                else:
                    i += 1

            i = 0

        case 6:

            exit()
        
menu_principal()
