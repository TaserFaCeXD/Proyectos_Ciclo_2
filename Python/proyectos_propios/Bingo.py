import random
import time

def menu_principal():
    print("\n\t\tBINGO")
    print("\n\t- Escriba 0 para empezar la partida o 1 para cerrar el juego: ", end="")

    while True:
        try:
            go = int(input("\t"))  

            if go in (0, 1):  
                return go 
            else:
                print("\n\tOpción no válida, debe ser 0 o 1. Inténtelo nuevamente.")
        except ValueError:
            print("\n\tOpción no válida. Ingrese un número.")

def inicio_juego():
    print("\n\t\tBINGO")
    # Aquí iría la lógica del juego
    print("\n\tJuego iniciado")

# Inicio del programa
while True:
    opcion = menu_principal()
    if opcion == 0:
        inicio_juego()
    elif opcion == 1:
        print("\n\tGracias por jugar!")
        break # Sale del bucle principal y termina el programa