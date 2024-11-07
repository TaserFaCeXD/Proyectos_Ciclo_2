import random

vicAhorcado = 0
derAhorcado = 0
recordAhorcado = 0
vicPupiletras = 0

def funcionAhorcado(vicAhorcado, derAhorcado, recordAhorcado, vicPupiletras):

    palabrasAhorcado = {1 : "INNOVACION", 2 : "EXCELENCIA", 3 : "TUTORIA", 4 : "CACHIMBO", 5 : "TECNOLOGIA", 6 : "PABELLON",
                        7 : "CAMPUS", 8 : "TRIKA", 9 : "REMEDIAL", 10 : "TALLER", 11 : "CURSO", 12 : "TIU", 13 : "DELEGADO", 14 : "UPC", 15 : "BIKA"}

    puntajeAhorcado = 0
    letra = str
    palabra = list
    lista = list
    interacciones = 0

    def ahorcadoInicio(palabrasAhorcado, puntajeAhorcado, recordAhorcado, letra, interacciones, lista, vicAhorcado, derAhorcado): 

        numKeyPalabras = random.randint(1 , 15)
        i = int()
        k = int()
        contadorIntentos = 0
    
        
        #El programa debe elegir una de esas palabras al azhar y mostrar en pantalla de cuantos caracteres es la palabra a adivina

        cantidadLetras = len(palabrasAhorcado[numKeyPalabras])

        print('\t\tBIENVENIDO AL JUEGO "AHORCADOS DE LA UPC"')
    
        print('\t\t')

        funcionAhorcado1(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, interacciones, lista, recordAhorcado, vicAhorcado)

    def funcionAhorcado1(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, interacciones, lista, recordAhorcado, vicAhorcado):
        
        print("\t\t\t____________")
        #print("\t\t\t            |")
        #print("\t\t\t           (_) ")
        #print("\t\t\t           /|\ ")
        #print("\t\t\t           / \ ") 

        print("\n\t\t\t", end="")

        palabra = list(palabrasAhorcado[numKeyPalabras])

        while i < cantidadLetras:
        
            print("_ ", end="")

            i += 1


        lista = []

        i = 0
        letra = input("\n\nIntroduce una letra o adivine la palabra completa: ")

        while k < 1:
           if letra.isdigit() == True:
               letra == input("\n\nletra o palabra invalidos, por favor digite una consonante, vocal o adivine la palabra completa: ")
           else:
               k += 1

        k = 0

        if letra.upper() == palabrasAhorcado[numKeyPalabras]:
        
            print("Felicidades, adivinaste la palabra a la primera, que pro")
            print("\t\t\t", end="")

            vicAhorcado += 1

            while i < cantidadLetras:

                palabraSeparada = list(palabrasAhorcado[numKeyPalabras])
            
                print(palabraSeparada[i], end=" ")

                i += 1

            puntajeAhorcado += len(palabra) + 10

            if puntajeAhorcado > recordAhorcado:
                recordAhorcado = puntajeAhorcado

            print("Puntaje final: ", puntajeAhorcado)
            opcion = input("Desea seguir jugando? (S: si, N: no): ")

            while k < 1:
                if opcion.upper() != 'S' and opcion.upper() != 'N':
                    opcion = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
                else:
                    k+= 1

            if opcion.upper() == 'S':
                ahorcadoInicio(palabrasAhorcado, puntajeAhorcado, recordAhorcado, letra, interacciones, lista, vicAhorcado, derAhorcado)

            if opcion.upper() == 'N':
                menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras) 

            i = 0    

        elif palabrasAhorcado[numKeyPalabras].count(letra.upper()) >= 1:
       
            puntajeAhorcado += 1

            lista.append(letra)

            funcionAhorcado2(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado)

        else:

            puntajeAhorcado -= 1
            contadorIntentos += 1
      
        if contadorIntentos == 1:
            ahorcadoIntento1(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado)

    def funcionAhorcado2(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado):
    
        print("\t\t\t____________")
        #print("\t\t\t            |")
        #print("\t\t\t           (_) ")
        #print("\t\t\t           /|\ ")
        #print("\t\t\t           / \ ") 

        print("\n\t\t\t", end="")

        i = 0
        k = 0

        palabra = list(palabrasAhorcado[numKeyPalabras])
    
        while i < cantidadLetras:

            while k < len(lista):

                if palabra[i] == lista[k].upper():
                    print(lista[k].upper(), end=" ")

                    k += 100000

                    interacciones += 1

                k += 1

            if interacciones <= 0:

                print("_ ", end="")

            interacciones = 0
            k = 0
            i += 1


        i = 0
        letra = input("\n\nIntroduce una letra o adivine la palabra completa: ")

        while k < 1:
            if letra.isdigit() == True:
               letra = input("\n\nletra o palabra invalidos, por favor digite una consonante, vocal o adivine la palabra completa: ")
            else:
               k += 1

        k = 0

        if letra.upper() == palabrasAhorcado[numKeyPalabras]:

            puntajeAhorcado += len(palabra)
            vicAhorcado += 1

            if puntajeAhorcado > recordAhorcado:
                recordAhorcado = puntajeAhorcado
        
            print("Puntaje final: ", puntajeAhorcado)
            opcion = input("Felicidades! Ganaste el juego, deseas jugar otra vez? (S: si, N: no) ")

            while k < 1:
                if opcion.upper() != 'S' and opcion.upper() != 'N':
                    opcion = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
                else:
                    k+= 1

            if opcion.upper() == 'S':
                ahorcadoInicio(palabrasAhorcado, puntajeAhorcado, recordAhorcado, letra, interacciones, lista, vicAhorcado, derAhorcado)

            if opcion.upper() == 'N':
                menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras) 

        elif palabrasAhorcado[numKeyPalabras].count(letra.upper()) >= 1:

            puntajeAhorcado += 1
       
            lista.append(letra)

            funcionAhorcado2(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado)

        else:

            puntajeAhorcado -= 1
            contadorIntentos += 1
      
        if contadorIntentos == 1:
            ahorcadoIntento1(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado)

    def ahorcadoIntento1(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado):
        print("\t\t\t____________")
        print("\t\t\t            |")
        #print("\t\t\t           (_) ")
        #print("\t\t\t           /|\ ")
        #print("\t\t\t           / \ ") 


        print("\n\t\t\t", end="")

        i = 0
        k = 0
    
        palabra = list(palabrasAhorcado[numKeyPalabras])

        while i < cantidadLetras:

            while k < len(lista):

                if palabra[i] == lista[k].upper():

                    print(lista[k].upper(), end=" ")

                    k += 100000

                    interacciones += 1

                k += 1

            if interacciones <= 0:

                print("_ ", end="")

            interacciones = 0
            k = 0
            i += 1


        i = 0
        letra = input("\n\nIntroduce una letra o adivine la palabra completa: ")

        while k < 1:
           if letra.isdigit() == True:
               letra = input("\n\nletra o palabra invalidos, por favor digite una consonante, vocal o adivine la palabra completa: ")
           else:
               k += 1

        k = 0

        if letra.upper() == palabrasAhorcado[numKeyPalabras]:

            puntajeAhorcado += len(palabra)
            vicAhorcado += 1

            if puntajeAhorcado > recordAhorcado:
                recordAhorcado = puntajeAhorcado
        
            print("Puntaje final: ", puntajeAhorcado)
            opcion = input("Felicidades! Ganaste el juego, deseas jugar otra vez? (S: si, N: no) ")

            while k < 1:
                if opcion.upper() != 'S' and opcion.upper() != 'N':
                    opcion = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
                else:
                    k+= 1

            if opcion.upper() == 'S':
                ahorcadoInicio(palabrasAhorcado, puntajeAhorcado, recordAhorcado, letra, interacciones, lista, vicAhorcado, derAhorcado)

            if opcion.upper() == 'N':
                menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras) 

        elif palabrasAhorcado[numKeyPalabras].count(letra.upper()) >= 1:

            puntajeAhorcado += 1
       
            lista.append(letra)

            ahorcadoIntento1(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado)

        else:

            puntajeAhorcado -= 1
            contadorIntentos += 1
      
        if contadorIntentos == 2:
            ahorcadoIntento2(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado)

    def ahorcadoIntento2(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado):
        print("\t\t\t____________")
        print("\t\t\t            |")
        print("\t\t\t           (_) ")
        #print("\t\t\t           /|\ ")
        #print("\t\t\t           / \ ") 


        print("\n\t\t\t", end="")

        i = 0
        k = 0
    
        palabra = list(palabrasAhorcado[numKeyPalabras])

        while i < cantidadLetras:

            while k < len(lista):

                if palabra[i] == lista[k].upper():

                    print(lista[k].upper(), end=" ")

                    k += 100000

                    interacciones += 1

                k += 1
 
            if interacciones <= 0:

                print("_ ", end="")

            interacciones = 0
            k = 0
            i += 1


        i = 0
        letra = input("\n\nIntroduce una letra o adivine la palabra completa: ")

        while k < 1:
           if letra.isdigit() == True:
                letra = input("\n\nletra o palabra invalidos, por favor digite una consonante, vocal o adivine la palabra completa: ")
           else:
                k += 1

        k = 0

        if letra.upper() == palabrasAhorcado[numKeyPalabras]:
        
            puntajeAhorcado += len(palabra)
            vicAhorcado += 1

            if puntajeAhorcado > recordAhorcado:
                recordAhorcado = puntajeAhorcado

            print("Puntaje final: ", puntajeAhorcado)
            opcion = input("Felicidades! Ganaste el juego, deseas jugar otra vez? (S: si, N: no) ")

            while k < 1:
                if opcion.upper() != 'S' and opcion.upper() != 'N':
                    opcion = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
                else:
                    k+= 1

            if opcion.upper() == 'S':
                ahorcadoInicio(palabrasAhorcado, puntajeAhorcado, recordAhorcado, letra, interacciones, lista, vicAhorcado, derAhorcado)

            if opcion.upper() == 'N':
                menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras) 

        elif palabrasAhorcado[numKeyPalabras].count(letra.upper()) >= 1:

            puntajeAhorcado += 1
       
            lista.append(letra)

            ahorcadoIntento2(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado)

        else:
  
            puntajeAhorcado -= 1
            contadorIntentos += 1
      
        if contadorIntentos == 3:
            ahorcadoIntento3(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado, derAhorcado)

    def ahorcadoIntento3(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado, derAhorcado):
        print("\t\t\t____________")
        print("\t\t\t            |")
        print("\t\t\t           (_) ")
        print("\t\t\t           /|\ ")
        #print("\t\t\t           / \ ") 


        print("\n\t\t\t", end="")

        i = 0
        k = 0
    
        palabra = list(palabrasAhorcado[numKeyPalabras])

        while i < cantidadLetras:

            while k < len(lista):

                if palabra[i] == lista[k].upper():

                    print(lista[k].upper(), end=" ")

                    k += 100000

                    interacciones += 1

                k += 1

            if interacciones <= 0:

                print("_ ", end="")

            interacciones = 0
            k = 0
            i += 1


        i = 0
        letra = input("\n\nIntroduce una letra o adivine la palabra completa: ")

        while k < 1:
           if letra.isdigit() == True:
               letra = input("\n\nletra o palabra invalidos, por favor digite una consonante, vocal o adivine la palabra completa: ")
           else:
               k += 1

        k = 0

        if letra.upper() == palabrasAhorcado[numKeyPalabras]:
        
            puntajeAhorcado += len(palabra)
            vicAhorcado += 1

            if puntajeAhorcado > recordAhorcado:
                recordAhorcado = puntajeAhorcado

            print("Puntaje final: ", puntajeAhorcado)
            opcion = input("Felicidades! Ganaste el juego, deseas jugar otra vez? (S: si, N: no) ")

            while k < 1:
                if opcion.upper() != 'S' and opcion.upper() != 'N':
                    opcion = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
                else:
                    k+= 1

            if opcion.upper() == 'S':
                ahorcadoInicio(palabrasAhorcado, puntajeAhorcado, recordAhorcado, letra, interacciones, lista, vicAhorcado, derAhorcado)

            if opcion.upper() == 'N':
                menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras) 

        elif palabrasAhorcado[numKeyPalabras].count(letra.upper()) >= 1:

            puntajeAhorcado += 1
       
            lista.append(letra)

            ahorcadoIntento3(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado, derAhorcado)

        else:

            puntajeAhorcado -= 1
            contadorIntentos += 1
      
        if contadorIntentos == 4:
            ahorcadoIntento4(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado, derAhorcado)

    def ahorcadoIntento4(palabrasAhorcado, numKeyPalabras, cantidadLetras, i, k, contadorIntentos, puntajeAhorcado, letra, palabra, interacciones, lista, recordAhorcado, vicAhorcado, derAhorcado):
        print("\t\t\t____________")
        print("\t\t\t            |")
        print("\t\t\t           (_) ")
        print("\t\t\t           /|\ ")
        print("\t\t\t           / \ ") 


        print("\n\t\t\t", end="")

        i = 0
        k = 0

        if puntajeAhorcado > recordAhorcado:
            recordAhorcado = puntajeAhorcado
    
        puntajeAhorcado = 0
        derAhorcado += 1

        palabra = list(palabrasAhorcado[numKeyPalabras])

        print("Fin del juego :( la palabra era: ", end=" ")
        while i < cantidadLetras:

            palabraSeparada = list(palabrasAhorcado[numKeyPalabras])
            
            print(palabraSeparada[i], end=" ")

            i += 1

        print("\nPuntación más alta: ", recordAhorcado)

        opcion = input("Desea seguir jugando? (S: si, N: no): ")

        while k < 1:
            if opcion.upper() != 'S' and opcion.upper() != 'N':
                opcion = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
            else:
                k+= 1

        if opcion.upper() == 'S':
            ahorcadoInicio(palabrasAhorcado, puntajeAhorcado, recordAhorcado, letra, interacciones, lista, vicAhorcado, derAhorcado)

        if opcion.upper() == 'N':
            menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras) 

    
    ahorcadoInicio(palabrasAhorcado, puntajeAhorcado, recordAhorcado, letra, interacciones, lista, vicAhorcado, derAhorcado)

def funcionPup(vicPupiletras, vicAhorcado, derAhorcado, recordAhorcado):
    print("\nBIENVENIDO AL JUEGO LLAMADO 'PUPILETRAS UPCINO' ")
    palabrasPup1=["TIU","UPC","CURSO","TUTOR","SEDE"]
    palabrasPup2=["AULA","BIKA","TRIKA","LIBRO","PROFE"]

    print(" ")

    def pupiletras1(palabrasPup1):
    
        a = 0

        lis1=['S','E','D','E','T','Z']
        lis2=['O','S','R','U','C','Q']
        lis3=['V','W','T','P','X','Z']
        lis4=['J','O','I','C','K','H']
        lis5=['R','Q','U','R','W','J']
        lis6=['O','F','A','V','X','Y']

        desarrolloPup(palabrasPup1, palabrasPup2, lis1, lis2, lis3, lis4, lis5, lis6)

    def pupiletras2(palabrasPup2):

        a = 0

        lis1=['P','H','G','D','N','L']
        lis2=['W','R','R','B','A','I']
        lis3=['A','W','O','U','L','B']
        lis4=['K','Q','L','F','K','R']
        lis5=['I','A','D','U','E','O']
        lis6=['B','A','K','I','R','T']

        desarrolloPup(palabrasPup1, palabrasPup2, lis1, lis2, lis3, lis4, lis5, lis6)


    def desarrolloPup(palabrasPup1, palabrasPup2, lis1, lis2, lis3, lis4, lis5, lis6):

        a = 0

        print("\t|", end="")

        while a < 6:
            print(lis1[a], end=" | ")
            a += 1
        print("\n\t|", end="")
        a = 0

        while a < 6:
            print(lis2[a], end =" | ")
            a += 1
        print("\n\t|",end="")
        a = 0

        while a < 6:
            print(lis3[a], end =" | ")
            a += 1
        print("\n\t|", end="")
        a = 0
    
        while a < 6:
            print(lis4[a], end =" | ")
            a += 1
        print("\n\t|",end="")
        a = 0

        while a < 6:
            print(lis5[a], end =" | ")
            a += 1
        print("\n\t|",end="")
        a = 0


        while a < 6:
            print(lis6[a], end =" | ")
            a += 1
        print("\n\t", end="")
        a=0

    numPupiletras = random.randint(1,2)

    if numPupiletras == 1:
    
        pupiletras1(palabrasPup1)

    if numPupiletras == 2:

        pupiletras2(palabrasPup2)

    def encontrarPalabras(palabrasPup1, palabrasPup2, vicPupiletras, numPupiletras):
        k = 0  

        if numPupiletras == 1:

            while len(palabrasPup1) > 0:
                palabraEncontrada = input("\nDigite una de las palabras: ").upper()
        
                if palabraEncontrada in palabrasPup1:
                    k += 1
                    print(f"\nFelicidades, encontraste la palabra {palabraEncontrada}. Palabras encontradas {k} de 5.")
                    palabrasPup1.remove(palabraEncontrada) 
                else:
                    print("\nLa palabra no es correcta o ya fue encontrada.")
        
                print("\n")
                pupiletras1(palabrasPup1)

            print("\nFelicidades! Has encontrado todas las palabras.")

            vicPupiletras += 1

            opcion = input("Desea seguir jugando? (S: si, N: no): ")

            while k < 1:
                if opcion.upper() != 'S' and opcion.upper() != 'N':
                    opcion = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
                else:
                    k+= 1

            numPupiletras = 0

            if opcion.upper() == 'S':
                funcionPup(vicPupiletras, vicAhorcado, derAhorcado, recordAhorcado)

            if opcion.upper() == 'N':
                menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras) 
        

        if numPupiletras == 2:
            while len(palabrasPup2) > 0:
                palabraEncontrada = input("\nDigite una de las palabras: ").upper()
        
                if palabraEncontrada in palabrasPup2:
                    k += 1
                    print(f"\nFelicidades, encontraste la palabra {palabraEncontrada}. Palabras encontradas {k} de 5.")
                    palabrasPup2.remove(palabraEncontrada) 
                else:
                    print("\nLa palabra no es correcta o ya fue encontrada.")
        
                print("\n")
                pupiletras2(palabrasPup2)

            print("\nFelicidades! Has encontrado todas las palabras.")

            vicPupiletras += 1

            opcion = input("Desea seguir jugando? (S: si, N: no): ")

            while k < 1:
                if opcion.upper() != 'S' and opcion.upper() != 'N':
                    opcion = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
                else:
                    k+= 1

            numPupiletras = 0

            if opcion.upper() == 'S':
                funcionPup(vicPupiletras, vicAhorcado, derAhorcado, recordAhorcado)

            if opcion.upper() == 'N':
                menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras) 
        
    encontrarPalabras(palabrasPup1, palabrasPup2, vicPupiletras, numPupiletras)

def menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras):

    u = 0
    k = 0

    print("\n\t|-        MENTE EN JUEGO        -|")
    print("\n\tOpcion 1: Ahorcados de la UPC")
    print("\tOpcion 2: Pupiletras UPCINO")
    print("\tOpcion 3: Mostrar reportes")
    print("\tOpcion 4: Salir del sistema")
    
    opcionMenu = int(input("\n\tIngrese la opcion a elegir ->: "))

    if opcionMenu < 1 or opcionMenu > 4:
        while u < 1:
            opcionMenu = int(input("\n\topcion no valida, intentelo nuevamente ->: "))

            if 0 < opcionMenu < 5:
                u += 1

    if opcionMenu == 1:

        print('\tReglas de "AHORCADOS DE LA UPC":')
        print("\t- El juego mostrará '_' por cada letra que contenga la palabra y el jugador deberá adivinar una letra de esa palabra o la palabra completa.")
        print("\t- El juego dibujará una cuerda, la cual irá añadiendo un elemento cada vez que el jugador falle.")
        print("\t- El sistema de puntaje sumará 10 puntos si el jugador adivina la palabra completa a la primera")
        print("\t  e irá añadiendo 1 punto por cada letra adivinada (si la palabra tiene varias letras iguales solo se contará 1 punto).")
        print("\t- Si el jugador gane se mostrará su puntaje y una pregunta por si desea seguir jugando o no.")
        print("\t- El jugador tendrá como máximo 4 intentos ya que una vez dibujado todo el cuerpo del personaje, este morirá.")
        print("\tBuena suerte y disfruta del juego!!!")

        opcionAhorcado = input("Estas listo? (S: si, N: no): ")

        while k < 1:
            if opcionAhorcado.upper() != 'S' and opcionAhorcado.upper() != 'N':
                opcionAhorcado = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
            else:
                k += 1

        if opcionAhorcado.upper() == 'S':

            funcionAhorcado(vicAhorcado, derAhorcado, recordAhorcado, vicPupiletras)

        if opcionAhorcado.upper() == 'N':

            menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras)
  
    elif opcionMenu == 2:

        print("\nReglas de 'PUPILETRAS UPECINO':")
        print("""
        1. El objetivo del juego es encontrar las palabras ocultas en una cuadrícula de letras.
        2. Existen dos modalidades de juego, cada una con un conjunto diferente de palabras:
           - Modalidad 1: Se busca una lista de palabras específicas (palabrasPup1).
           - Modalidad 2: Se busca otra lista de palabras (palabrasPup2).
        3. Se mostrará una cuadrícula de 6x6 letras, donde están ocultas 5 palabras que debes encontrar.
        4. Las palabras pueden estar colocadas de forma horizontal o vertical.
        5. El jugador debe ingresar las palabras que encuentre en la cuadrícula:
           - Si la palabra es correcta, se eliminará de la lista de palabras a encontrar.
           - Si la palabra ya fue encontrada o es incorrecta, se pedirá que lo intentes nuevamente.
        6. El juego termina cuando encuentres todas las palabras en la lista.
        7. Al finalizar, podrás decidir si deseas seguir jugando o salir del juego.
        8. Buena suerte y disfruta del juego!!!
        """)

        opcionPup = input("Estas listo? (S: si, N: no): ")

        while k < 1:
            if opcionPup.upper() != 'S' and opcionPup.upper() != 'N':
                opcionPup = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
            else:
                k += 1

        if opcionPup.upper() == 'S':

            funcionPup(vicPupiletras, vicAhorcado, derAhorcado, recordAhorcado)

        if opcionPup.upper() == 'N':

            menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras)

    elif opcionMenu == 3:
        print("\n\t\t|-        REPORTES        -|")
        print("\t- Ahorcados de la UPC:")
        print("\t\tRecord: ", recordAhorcado)
        print("\t\tNumero de victorias: ", vicAhorcado)
        print("\t\tNumero de derrotas: ", derAhorcado)
        print("\t- Pupiletras UPCINO:")
        print("\t\tNumero de victorias: ", vicPupiletras)

        opcion = input("Desea volver al menu principal? (S: si, N: no): ")

        while k < 1:
            if opcion.upper() != 'S' and opcion.upper() != 'N':
                opcion = input("opcion no valida, intentelo nuevamente, desea jugar nuevamente? (S: si, N: no) ")
            else:
                k += 1

        if opcion.upper() == 'S':

            menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras)

        if opcion.upper() == 'N':

            exit()

    elif opcionMenu == 4:
        exit()

menuPrincipal(recordAhorcado, vicAhorcado, derAhorcado, vicPupiletras)




