import random
import time

def menu_principal():
    print("\n\t\tBINGO")
    print("\n\t- Escriba 0 para empezar la partida o 1 para cerrar el juego: ", end="")

    while True:

        try:

            go = int(input())

            if go == 0 or go == 1:

                break
            else:

                print("\n\tOpcion no valida, debe estar en el rango de 0 a 1, intentelo nuevamente: ", end="")
        
        except ValueError:

            print("\n\tOpcion no valida, debe ser un valor numerico, intentelo nuevamente: ", end="")

menu_principal()