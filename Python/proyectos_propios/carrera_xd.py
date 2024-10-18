import os
import time
import random

i = 0
Espacios1 = [" "]
Espacios2 = [" "]

Final1 = [" "]
Final2 = [" "]

while i < 145:
    Final1.append(" ")
    Final2.append(" ")

    i += 1

i = 0

while i < 1:

    ElegirAuto = random.randint(0, 1)

    Cadena1 = "".join(Espacios1)
    Cadena2 = "".join(Espacios2)

    CadenaF1 = "".join(Final1)
    CadenaF2 = "".join(Final2)

    if len(Final1) == 0:

        print("Rayo McQueen: ")
        print(Cadena1, "      ____     |M|")
        print(Cadena1, "   __/    |___ |E|")
        print(Cadena1, "  |__   __   _||T|")
        print(Cadena1, "      O    O   |A|")
        print("Francesco Virgolini: ")
        print(Cadena2, "    ____     ", CadenaF2, "|M|")
        print(Cadena2, " __/    |___ ", CadenaF2, "|E|")
        print(Cadena2, "|__   __   _|", CadenaF2, "|T|")
        print(Cadena2, "    O    O   ", CadenaF2, "|A|")
    elif len(Final2) == 0:

        print("Rayo McQueen: ")
        print(Cadena1, "    ____     ", CadenaF1, "|M|")
        print(Cadena1, " __/    |___ ", CadenaF1, "|E|")
        print(Cadena1, "|__   __   _|", CadenaF1, "|T|")
        print(Cadena1, "    O    O   ", CadenaF1, "|A|")
        print("Francesco Virgolini: ")
        print(Cadena2, "      ____     |M|")
        print(Cadena2, "   __/    |___ |E|")
        print(Cadena2, "  |__   __   _||T|")
        print(Cadena2, "      O    O   |A|")
    else:

        print("Rayo McQueen: ")
        print(Cadena1, "    ____     ", CadenaF1, "|M|")
        print(Cadena1, " __/    |___ ", CadenaF1, "|E|")
        print(Cadena1, "|__   __   _|", CadenaF1, "|T|")
        print(Cadena1, "    O    O   ", CadenaF1, "|A|")
        print("Francesco Virgolini: ")
        print(Cadena2, "    ____     ", CadenaF2, "|M|")
        print(Cadena2, " __/    |___ ", CadenaF2, "|E|")
        print(Cadena2, "|__   __   _|", CadenaF2, "|T|")
        print(Cadena2, "    O    O   ", CadenaF2, "|A|")

    

    if ElegirAuto == 0:

        Espacios1.append(" ")

        if len(Final1) > 0:
            Final1.pop()

        if len(Espacios1) <= 147:

            time.sleep(0.02)

            os.system("cls")

    if ElegirAuto == 1:
        
        Espacios2.append(" ")

        if len(Final2) > 0:
            Final2.pop()

        if len(Espacios2) <= 147:

            time.sleep(0.02)

            os.system("cls")


    if len(Espacios1) == 148:

        time.sleep(2)

        print("Ganador...", end=" ")

        time.sleep(5)

        print("El Rayo McQueen")

        time.sleep(3)
        os.system("cls")

        print("\tCUCHAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")

        i += 1

    if len(Espacios2) == 148:

        time.sleep(2)

        print("Ganador...", end=" ")

        time.sleep(5)

        print("FRANCESCO", end=" ")

        time.sleep(2)

        print("VIRGOLINIIIII")

        time.sleep(2)

        os.system("cls")

        print("\tFIUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU")

        i += 1

