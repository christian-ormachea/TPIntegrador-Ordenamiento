from time import perf_counter
import random
import os


### BUSQUEDA LINEAL ###

def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

### BUSQUEDA BINARIA ###

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

### ORDENAMIENTO BURBUJA ###

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

### INSERCION ###

def insertion_sort(lista):
  for i in range(1, len(lista)):
    key = lista[i]
    j = i-1
    while j >=0 and key < lista[j] :
        lista[j+1] = lista[j]
        j -= 1
    lista[j+1] = key

### SELECCION ###

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        # Se busca el índice del elemento mínimo
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        # Se intercambia el elemento mínimo con el elemento actual
        lista[i], lista[min_index] = lista[min_index], lista[i]

### QUICKSORT ###

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = random.choice(lista)
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
### MENU DE OPCIONES ###

def menu_eleccion():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" ***** Bienvenido al Programa para buscar tu metodo mas eficiente para la busqueda o ordenamiento de datos ***** ")
    print(" <------------------MENU------------------> ")
    print(" 1 - ******** BUSQUEDA ******** ")
    print(" --- Busqueda Lineal")
    print(" --- Busqueda Binaria")
    print(" 2 - ******** ORDENAMIENTO ******** ")
    print(" --- Ordenamiento Burbuja")
    print(" --- Insercion")
    print(" --- Seleccion")
    print(" --- Quicksort")
    print(" 3 --- Salir")

    return int(input("Ingrese su metodo deseado --> "))


def opciones_elegidas(opcion):
    if opcion == 1: 
        
        #BUSQUEDA
        # Se elije el tamaño de la lista
        tamaño_lista = int(input(" Ingrese la cantidad de valores que quiere calcular el tiempo de busqueda hasta 1000000 -->"))
        lista = random.sample(range(1, 10000000), tamaño_lista) 


        # Se Elije un objetivo aleatorio a buscar
        objetivo = random.choice(lista)


        # Se mide los tiempos de demora de la Busqueda lineal 
        inicio_tlineal = perf_counter()
        resultado_lineal = busqueda_lineal(lista, objetivo)
        fin_tlineal = perf_counter()
        tiempo_lineal = fin_tlineal - inicio_tlineal
        print(f"El resultado de la Búsqueda Lineal es {resultado_lineal}, y se tardo {tiempo_lineal:.6f} segundos")

        # Se mide los tiempos de demora de la Busqueda Binaria
        lista_ordenada = sorted(lista)
        inicio_tbinario = perf_counter()
        resultado_binario = busqueda_binaria(lista_ordenada, objetivo)
        fin_tbinario = perf_counter()
        tiempo_binario = fin_tbinario - inicio_tbinario
        print(f"El resultado de la Búsqueda Binaria es {resultado_binario}, y se tardo {tiempo_binario:.6f} segundos")

        print("*************************************************************************")
        
        # Comparacion
        if tiempo_binario > tiempo_lineal:
            print(f" El metodo mas eficiente para su necesidad es la busqueda lineal con {tiempo_lineal:.6f} segundos")
        else:
            print(f" El metodo mas eficiente para su necesidad es la busqueda binaria con {tiempo_binario:.6f} segundos")

    elif opcion == 2:
        
        #ordenadores

        # Se elije el tamaño de la lista
        tamaño_lista = int(input(" Ingrese la cantidad de valores aleatorios que quiere ordenar hasta 1000000 --> "))
        lista = random.sample(range(1, 10000000), tamaño_lista) 


        # Se mide los tiempos de demora con bubblesort
        inicio_tiempo_bubble = perf_counter()
        bubble_sort(lista)
        fin_tiempo_bubble = perf_counter()
        tiempo_bubble = fin_tiempo_bubble - inicio_tiempo_bubble
        print(f" Ordenamiento con bubblesort en {tiempo_bubble:.6f} segundos")
        
        # Se mide los tiempos de demora con insertion
        inicio_tiempo_insertion = perf_counter()
        insertion_sort(lista)
        fin_tiempo_insertion = perf_counter()
        tiempo_insertion = fin_tiempo_insertion - inicio_tiempo_insertion
        print(f" Ordenamiento con insertion en {tiempo_insertion:.6f} segundos")

        # Se mide los tiempos de demora con selection
        inicio_tiempo_selection = perf_counter()
        selection_sort(lista)
        fin_tiempo_selection = perf_counter()
        tiempo_selection = fin_tiempo_selection - inicio_tiempo_selection
        print(f" Ordenamiento con selection en {tiempo_selection:.6f} segundos")

        # Se mide los tiempos de demora con Quicksort
        inicio_tiempo_quicksort = perf_counter()
        quicksort(lista)
        fin_tiempo_quicksort = perf_counter()
        tiempo_quicksort = fin_tiempo_quicksort - inicio_tiempo_quicksort
        print(f" Ordenamiento con quicksort en {tiempo_quicksort:.6f} segundos")

        print("*************************************************************************")

        # Comparacion
        if tiempo_bubble < tiempo_insertion and tiempo_bubble < tiempo_selection and tiempo_bubble < tiempo_quicksort:
            print(f" El metodo mas eficiente para su necesidad es el metodo bubblesort con {tiempo_bubble:.6f} segundos")
        elif  tiempo_insertion < tiempo_selection and tiempo_insertion < tiempo_quicksort:
            print(f" El metodo mas eficiente para su necesidad es el metodo insertion con {tiempo_insertion:.6f} segundos")
        elif  tiempo_selection < tiempo_quicksort:
            print(f" El metodo mas eficiente para su necesidad es el metodo selection con {tiempo_selection:.6f} segundos")
        else:
            print(f" El metodo mas eficiente para su necesidad es el metodo quicksport con {tiempo_bubble:.6f} segundos")

    elif opcion == 3:

        print("XXXXXXXXXX fin del programa XXXXXXXXXX ")
    else:
        print(" XXXXXXXX Error XXXXXXXX ")
    


# Codigo principal

opcion_elegida = menu_eleccion()

opciones_elegidas(opcion_elegida)