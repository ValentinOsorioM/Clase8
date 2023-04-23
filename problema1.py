def suamar_5_enteros():
    # Definicion de variables
    lista = []
    contadorWhile = 0
    tamano = 5
    suma = 0

    # Ingresamos los numeros
    while contadorWhile < tamano:
        lista.append(int(input("Ingrese número " + str(contadorWhile+1) + ": ")))
        contadorWhile += 1

    # Sumamos los numeros
    contadorWhile = 0
    while contadorWhile < tamano:
        suma += lista[contadorWhile]
        contadorWhile += 1

    print("Los elementos de la lista son: ")
    for numero in lista:
        print(numero,end=', ')

    print("\nLa suma de todos sus elementos es: ")
    print(suma)