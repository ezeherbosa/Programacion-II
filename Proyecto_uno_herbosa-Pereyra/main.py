# Programación II: Primer Proyecto / Herbosa - Pereyra
# Tecnicatura universitaria en Programación UTN FRBB - Octubre 2021

import re
import random
import json
import xml.etree.cElementTree as ET
from os import system, name
from time import sleep

def clear():
    # Windows
    if name == 'nt':
        _ = system('cls')
    # Linux y Mac
    else:
        _ = system('clear')


def random_list_of_list():
    ldl = []
    for i in range(random.randint(0,5)):
        ldl.append(random.sample(range(10,30), random.randint(1,4)))
    return ldl

def welcome():
    output = """
    Programación II: Primer Proyecto / Herbosa - Pereyra
    ----------------------------------------------------------------
    Bienvenido al desallorro de ejercicios de Expresiones regulares,
    Recursión, Colecciones e Intercambio de datos JSON XML."""
    print(output)


def menu():
    menustr = """
    \tMENU DE EJERCICIOS\t\t\t[m] Menu  [s] Salir
    ----------------------------------------------------------------
        > Expresiones Regulares
            [1] Matriculas Argentinas
            [2] Numeros < 1900
            [3] EXTRA: Python Regex
        > Recursión
            [4] Codificar números
            [5] Aplanar lista de listas
            [6] Comparar 2 listas de num
            [7] División entera
            [8] EXTRA: Fibonacci
            [9] EXTRA: Sumar digitos de N
            [0] EXTRA: Sumar valores de lista
        > Colecciones
            [a] map, filter y reduce
            [b] Pi desde suma de N terminos
        > Formato de intercambios de datos
            [c] Estaciones Meteorológicas
    ----------------------------------------------------------------
    """
    print(menustr)


def select_option():
    return input("\n[>] ¿Qué ejercicio desea ver? [m] Menu [s] Salir: ")


def routing(ej):
    option = str(ej).lower()
    if option == "1":
        print("[1] Matriculas Argentinas")
        ej1_patentes_argentinas()
    elif option == "2":
        print("[2] Numeros < 1900")
        ej2_numeros_menor_1900()
    elif option == "3":
        print("[3] EXTRA: Python Regex")
        ej3_extra_python_regex()
    elif option == "4":
        print("[4] Codificar números")
        ej4_codificar_numeros()
    elif option == "5":
        print("[5] Aplanar lista de listas")
        ej5_aplanar_lista_de_listas()
    elif option == "6":
        print("[6] Comparar 2 listas de num")
        ej6_comparar_lista()
    elif option == "7":
        print("[7] División entera")
        ej7_division_entera_sin_division()
    elif option == "8":
        print("[8] EXTRA: Calculo de Fibonacci")
        ej8_calcular_fibonacci()
    elif option == "9":
        print("[9] EXTRA: Sumar digitos de N")
        ej9_sumar_digitos()
    elif option == "0":
        print("[0] EXTRA: Sumar elementos de lista")
        ej0_sumar_valores_de_lista()

    elif option == "a":
        print("[a] map, filter y reduce")
        eja_map_filter_reduce()
    elif option == "b":
        print("[b] Pi desde suma de N terminos")
        ejb_calcular_pi_aprox()
    elif option == "c":
        print("[c] Formatos de Intercambio de Datos: Estaciones Meteorológicas")
        ejc_estaciones_meteorologicas()
    elif option == "m":
        print("[m] Ver Menu")
        menu()
        elegir()
    elif option == "s":
        print("[s] Salir")
        print("[!] Gracias por utilizar nuestro programa")
        print("[#] Ezequiel Herbosa / Dante Pereyra - 2021")
    else:
        print('[x] ERROR: Elija una opcion válida del menu. \n')
        elegir()
    

def elegir():
    routing(select_option())


def ej1_patentes_argentinas():
    enunciado = """
    1. Las matrículas de las aeronaves en Argentina tienen el siguiente formato de acuerdo a su tipo (donde abc significa 3 letras mayúsculas y 123 3 dígitos):
        LV-abc\t\tUso general
        LQ-abc\t\tGubernamental
        LV-X123\t\tExperimentales
        LV-S123\t\tAeronave deportiva liviana
        LV-SX123\tAeronave deportiva liviana experimental

        Matrículas válidas:
        LV-QWE
        LQ-ABE
        LV-X443
        LV-S586
        LV-SX334
        
        Matrículas inválidas:
        LA-123
        LX-ABC
        LV
        LV-344

    Implemente una expresión regular para validar matrículas argentinas.
    """
    solucion = """
    SOLUCION: \\bL[VQ]-[A-Z][A-Z][A-Z]|LV-(X\d\d\d|S\d\d\d|SX\d\d\d)\\b 

    Explicacion: usamos \\b para definir el principio y fin de la patente, usando como ancla los espacios y puntuacion.
    Tomamos en cuenta las similaridades, las diferencias como asi todos los casos que quedan excluidos.
    Desarrollamos el caso de las de uso general y las gubernamentales: L[QV]-[A-Z][A-Z][A-Z]
    Luego desarrollamos los 3 casos de las experimentales y livianas juntas: LV- más las opciones para cada una, separadas por un OR (|)
    """
    print(enunciado)
    input("Presione [ENTER] para ver la solucion...")
    print(solucion)
    elegir()


def ej2_numeros_menor_1900():
    enunciado = """
    2. Diseñe una ER para validar cadenas de números naturales menores a 1900.
    """
    solucion = """
        SOLUCION: \\b(1[0-8]|[0-9])?[0-9]?[0-9]\\b

    Explicacion: usamos \\b para definir el principio y fin del numero, usando como ancla los espacios y puntuacion.
    N tiene 4 cifras / la primera es 1 / la segunda es entre 0 y 8 / 2 numeros cualquiera
    Combinamos los casos de los numeros de 3 o 4 cifras con un OR (|) entre 1 más cualquier cifra entre 0 y 8 ó una cifra 0-9
    Como el caso minimo es un numero de 1 cifra, el resto de las cifras las ponemos con ? porque pueden estar o no.
    """

    print(enunciado)
    input("Presione [ENTER] para ver la solucion...")
    print(solucion)
    elegir()


def ej3_extra_python_regex():
    descripcion = """
    Python tiene un paquete incorporado llamado re, que se puede importar para trabajar con expresiones regulares:
    
        import re

    El módulo re ofrece un conjunto de funciones que nos permite buscar una cadena para una coincidencia:
    
        findall\t\tDevuelve una lista que contiene todas las coincidencias
        search\t\tDevuelve un objeto Match si hubo alguna coincidencia
        split\t\tDevuelve una lista donde la cadena se ha dividido en cada coincidencia
        sub\t\tReemplaza una o más coincidencias con una cadena
    """
    research = """
    Por ejemplo, vamos a utilizar la funcion re.search() para averiguar si el número que le pediremos que ingrese, es menor a 1900.
    En código esto se implementaría:

        re.search(r'\\b(1[0-8]|[0-9])?[0-9]?[0-9]\\b', input_usuario)
    
    Esta función se llama con 2 parametros: re.search([REGEX], [STRING]) donde [REGEX] es la expresión regular
    y [STRING] es la cadena donde se buscará.

    La r delante del [REGEX] evita que el interprete de Python la modifique en caso de usar caracteres de escape como \\
    """
    print(descripcion)
    input("Presione [ENTER] para ver una demostracion...")
    print(research)
    input("Presione [ENTER] para probar re.search()...")
    
    # Loop para ejecutarlo multiples veces
    while True:
        print("\n[#] Numero ENTERO es menor a 1900?\n------------------------------------------")
        numero = input("[>] Ingrese un numero ENTERO o [s] para salir: ")
        if not numero.isnumeric():
            if numero == "s":
                break
            else:
                print("[x] Debe ingresar un numero ENTERO")


        if re.search(r'\b(1[0-8]|[0-9])?[0-9]?[0-9]\b', numero):
            print("[v] Ingresó un numero entero MENOR a 1900")
        else:
            print("[^] Ingreso un numero entero IGUAL O MAYOR a 1900")
        sleep(1)

    print("\n[!] Aprendimos un poco más sobre el módulo re!\n")
    elegir()


def ej4_codificar_numeros():
    enunciado = """
    Codificar un número entero de la siguiente manera cada dígito par sustituirlo por 1, cada dígito impar
    por 2. Puede pasar el número a otras representaciones para resolver el ejercicio.
    Ejemplo: El número 46579222 deberá codificarse como 11222111.
    """
    solucion = """
    Caso BASE: codificamos 1 cifra (retornamos 1 si es par y 2 si es impar)
    Caso RECURSIVO: codificamos 1 cifra + codificamos el resto de la lista
    """
    print(enunciado)
    input("Presione [ENTER] para ver la solución...")
    print(solucion)
    # Loop para ejecutarlo multiples veces
    while True:
        numero = input("[>] Ingrese un numero entero o [s] salir: ")
        if not numero.isnumeric():
            if numero == "s":
                break
            else:
                print("[x] Debe ingresar un numero ENTERO")
        else:
            codificado = ej4_codificar(numero)
            print("[=] Convertido: {codificado} \n".format(codificado=codificado))
    elegir()


def ej4_codificar(str_numero):
    # Caso Base: el str_numero se recibe vacío = False
    if not str_numero:
        return ''
    
    cifra_actual = int(str_numero[0])
    if cifra_actual % 2 == 0:
        codificado = '1'
    else:
        codificado = '2'
    return codificado + ej4_codificar(str_numero[1:])


def ej5_aplanar_lista_de_listas():
    enunciado = """
    Convertir una lista de listas en una sola lista que tenga todos los elementos de las listas originales.
    Ejemplo: Si L = [ [1, 2, 3], [4, 5, 6], [7], [8] ] la lista resultante deberá ser L2 = [1,2,3,4,5,6,7,8]
    """
    solucion = """
    Caso BASE: Lista de listas  = []
    Caso RECURSIVO: Aplanar 1 elemento de la lista + Aplanar el resto de la lista
    """
    print(enunciado)
    input("Presione [ENTER] para ver la solución...")
    print(solucion)
    # Loop para ejecutarlo multiples veces
    while True:
        ldl = random_list_of_list()
        print("\n[+] Lista de listas: {ldl}".format(ldl=ldl))
        resultado = ej5_aplanar(ldl)
        print("[=] Lista aplanada: {resultado} \n".format(resultado=resultado))

        a = input("[>] Presione ENTER para ver otra lista - [s] salir: ")
        if a == "s":
            break
    elegir()


def ej5_aplanar(lista):
    # Caso base:  lista = []
    if lista == []:
        return []
    pop = lista.pop()
    return ej5_aplanar(lista) + pop


def ej6_comparar_lista():
    enunciado = """
    Decidir si dos listas de números enteros son iguales
    """
    solucion = """
    Caso BASE: Ambas listas están vacias.
    Caso RECURSIVO: Comparamos numero por numero comparar toda la cadena.
    """
    print(enunciado)
    print(solucion)

    lista_uno = [1,2,3,4,5,6]
    lista_dos = [1,2,3,4,5,6]

    print(lista_uno)
    print(lista_dos)

    def comparar_lista(primer_lista,segunda_lista):
        # Caso base:  lista = []
        if primer_lista == [] and primer_lista == segunda_lista:
            return []
        else:
            if primer_lista[0] == segunda_lista[0]:
                return comparar_lista(primer_lista[1:],segunda_lista[1:])

     #ejemplo con listas iguales
    comparacion = comparar_lista(lista_uno,lista_dos)

    if comparar_lista(lista_uno,lista_dos) == []:
        print("las listas son iguales.")
    else:
        print("las listas son diferentes.")

    #ejemplo con listas distintas.

    lista_dos = [13,22,3]

    print(lista_uno)
    print(lista_dos)

    if comparar_lista(lista_uno,lista_dos) == []:
        print("las listas son iguales.")
    else:
        print("las listas son diferentes.")




def ej7_division_entera_sin_division():
    enunciado = """
    Realizar la división entera entre dos números enteros positivos A y B, (B ≠ 0).
    Ayuda: Pensar la división entera como sucesión de restas
    """
    solucion = """
    Caso BASE: Si A < B, la division entera de A/B => 0
    Caso RECURSIVO: Division entera A/B + Division entera del resto
    """
    print(enunciado)
    input("Presione [ENTER] para ver la solución...")
    print(solucion)
    # Loop para ejecutarlo multiples veces
    while True:
        a = input("[>] Ingrese un numero entero como DIVIDENDO A (A/b) - [s] salir: ")
        if not a.isnumeric():
            if a == "s":
                break
            else:
                print("[x] El dividendo debe ser un numero ENTERO")
        else:
            b = input("[>] Ingrese un numero entero como DIVISOR B (a/B) - [s] salir: ")
            if not b.isnumeric():
                if b == "s":
                    break
                else:
                    print("[x] El divisor debe ser un numero ENTERO")
            else:
                resultado = ej7_division_entera(int(a), int(b))
                print("[=] Division entera: {resultado} \n".format(resultado=resultado))
    elegir()


def ej7_division_entera(a, b):
    # Caso base:  A < B => 0
    if a < b:
        return 0
    resto = a - b
    return 1 + ej7_division_entera(resto, b)


def calcular_fibonacci(x):
            if x == 0:
                return 0
            elif x == 1:
                return 1
            else:
                return calcular_fibonacci(x - 1) + calcular_fibonacci(x - 2)


def ej8_calcular_fibonacci():
    enunciado = """
    Calcular fibonacci para n terminos con un algoritmo recursivo
    """
    solucion = """
    Caso BASE: cuando n = 0, fibonacci es = 0 || cuando n = 1, fibonacci es = 1
    Caso RECURSIVO: N = (n-1) + (n-2)
    """
    print(enunciado)
    input("Presione [ENTER] para ver la solución...")
    print(solucion)

    while True:
        n = int(input("[>] Ingrese un entero para realizar el calculo de Fibonacci: "))
        print(calcular_fibonacci(n))
        continuar = input("[?] Quiere calcular otro numero? S/N: ".lower())
        if continuar == "n":
            break
    elegir()


def sumar_digitos(x):
            if x < 10:
                return x
            else:
                return int(sumar_digitos(x / 10) + sumar_digitos(x % 10))


def ej9_sumar_digitos():
    enunciado = """
    Sumar los digitos de un numero entero con un algoritmo recursivo
    """
    solucion = """
    Caso BASE: El numero tiene un solo digito (n<10).
    Caso RECURSIVO: aplicando division y modulo descomponemos el numero, sumamos la unidad obtenida y el resto.
    """
    print(enunciado)
    input("Presione [ENTER] para ver la solución...")
    print(solucion)

    while True:
        x = int(input("[>] Ingrese un numero entero para sumar sus digitos: "))
        print(sumar_digitos(x))
        continuar = input("[?] Quiere calcular otro numero? S/N: ".lower())
        if continuar == "n":
            break
    elegir()

def sumar_elementos_lista(lista):
        if lista == []:
            return 0
        else:
            return lista[0] + sumar_elementos_lista(lista[1:])

def ej0_sumar_valores_de_lista():
    enunciado = """
    Sumar valores de una lista con un algoritmo recursivo
    """
    solucion = """
    Caso BASE: La lista, es una lista vacia.
    Caso RECURSIVO: sumamos el primer elemento de la lista, con el primer elemento de la lista restante.
    """
    print(enunciado)
    input("Presione [ENTER] para ver la solución...")
    print(solucion)

    print("Ejemplo: sumar_elementos_lista([1,1,1,1])")
    print(sumar_elementos_lista([1, 1, 1, 1]))
    print("")
    input("Presione [ENTER] para ver el sigiuiente ejemplo...\n")
    print("Ejemplo: sumar_elementos_lista([1,2,3,4,5])")
    print(sumar_elementos_lista([1,2,3,4,5]))
    print("")
    input("Presione [ENTER] para ver el sigiuiente ejemplo...\n")
    print("Ejemplo: sumar_elementos_lista([7,5,9])")
    print(sumar_elementos_lista([7,5,9]))
    elegir()


def eja_map_filter_reduce():
    enunciado = """
    Explicar en pocas palabras y utilizando diagramas las operaciones de map, filter y reduce.
    Proponga ejemplos de cada uno (conceptuales, no necesariamente en código).
    """

    explica_map = """  
           + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
           |                                <MAP>                                  |
           |                                                                       |
           |     La funcion MAP se utiliza para modificar secuencias de elementos. |
           | map() recibe dos parametros, el primer parametro será una funcion     |
           | mientras que el segundo será una lista de elementos.                  |
           |                                                                       |
           |     map() aplicara a cada elemento de la lista, la transformacion     |
           | que ordene la funcion indicada en el primer parametro.                |
           | Retornando finalmente una lista con los elementos transformados.      |
           + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - + 
           + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - + 
           | ejemplo funcion map:                                                    |
           |      funcion = (i * 4) / 2                                              |
           |     secuencia = [3,15,2,8,12]                                           |
           |                            retorna                                      |
           |     map(funcion,secuencia)  ---->    [6,30,4,16,24]     //se modifican  |
           |                                     los valores orignales de secuencia  |
           + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
    """
    explica_filter = """  
          
          + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +  
          |                                 <FILTER>                                          |
          |                                                                                   |
          |      La función filter() toma una secuencia de elementos y filtara                |
          |  aquellos que cumplan con una determinada condicion que se le indique.            |
          |  La funcion filter a diferencia de map, retorna una lista sin alterar             |
          |  los elementos originales.                                                        |
          |                                                                                   |
          |      Filter tambien recibe dos parametros, el primero sera                        |
          |  una funcion logica, el segundo, una secuencia de elementos.                      |
          |                                                                                   |
          |  ejemplo funcion filter():                                                        |
          |      funcion = return i > 20                                                      |
          |      secuencia = [6,30,4,16,24]                                                   |
          |                                                                                   | 
          |      filter(funcion,secuencia)  ---->    [30,24]  // los valores filtrados no se  | 
          |                                retorna             eliminan de la lista original  |
          + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +                                
    """
    explica_reduce = """  
           + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +   
           |                                 <REDUCE>                                        | 
           |                                                                                 |
           |     La funcion reduce() tambien recibe dos parametros, una funcion que          |
           | indique el criterio para comparar los distintos elementos, y en segundo         |
           | lugar, la secuencia de elementos que es necesario procesar.                     |
           |                                                                                 |  
           |     reduce() efectua una comparacion en base a la funcion que se le indique,    |
           | tomando en primer instancia a los dos primeros elementos de la secuencia,       |
           | el resultado de esa primer ejecucion sera el que se utilizara para comparar con |
           | el elemento siguiente den la secuencia.                                         |
           |     El proceso se repite de forma recurrente y de esta manera es como todos los |
           |     terminos son evaluados con el fin de obtener un ultimo y unico resultado.   |  
           + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - + 
           |                    ---    ---  ||  ---    ---                                   |
           |                   | A |  | B | || | C |  | D |                                  |
           |                    ---    ---  ||  ---    ---                                   |
           |                       \  /          |                                           |
           |                        \/           |                                           |
           |                       +---+       +---+       ||   +---+                        |
           |                       | A |       | C |       ||   | D |                        |
           |                       +---+       +---+       ||   +---+                        |
           |                           \       /                 /                           | 
           |                            \     /                 /                            |
           |                             +---+              +---+                            |
           |                             | A |              | D |                            |
           |                             +---+              +---+                            |
           |                                   \           /                                 |
           |                                    \_________/                                  |
           |                                         |                                       |
           |                                       +---+                                     |
           |                                       | D |                                     |
           |                                       +---+                                     |
           |                                                                                 |
           + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
    """

    print(enunciado)
    while True:
        funcion = input("[>] Que funcion desea ver? [m] map [f] filter [r] reduce [s] salir: ")
        if funcion == 'm':
            print(explica_map)
        elif funcion == 'f':
            print(explica_filter)
        elif funcion == 'r':
            print(explica_reduce)
        elif funcion == 's':
            break
        else:
            print("[x] Debe ingresar una opcion válida")
    elegir()


def ejb_calcular_pi_aprox():
    enunciado = """
    Implemente un algoritmo sin usar estructuras repetitivas para calcular una aproximación de pi con N términos.
    Utilizando la sumatoria de i terminos con la formula (4*(-1)^i) / ((2*i)+1)
    """
    solucion = """
    Utilizando la función map(), podemos procesar una lista de 0 hasta n terminos con una funcion lambda que procese
    la formula (4*(-1)^i) / ((2*i)+1) y luego sumar todos los elementos de la lista con la funcion sum()"""

    print(enunciado)
    input("Presione [ENTER] para ver la solución...")
    print(solucion)

    while True:
        print("\n[𝝅] Vamos a calcular el numero Pi a través de una sumatoria de términos!")
        n = int(input("[>] Ingrese la cantidad de términos de la sumatoria: "))

        lista = [*range(0, n+1)]
        mapeado = list(map(lambda i: (4*(-1)**i) / ((2*i)+1), lista))
        sumatoria = sum(mapeado)

        print("Lista: " + str(lista))
        print("Map(): " + str(mapeado))
        print("Sum(): " + str(sumatoria))

        otra_vez = input("[?] Quiere probar nuevamente? [s] Si [n] No: ")
        if otra_vez == 'n':
            break
    elegir()

def ejc_estaciones_meteorologicas():
    enunciado = """
    Se necesita diseñar un formato para intercambiar datos de estaciones meteorológicas. El sistema tiene N estaciones cada una
    con su localización (latitud y longitud) y un nombre alfanumérico. Las estaciones pueden tener diferentes combinaciones de
    sensores entre: humedad, dirección del viento, velocidad del viento, temperatura (que puede estar en grados celsius o fahrenheit)
    y presión atmosférica. No todas las estaciones tienen todos los sensores, pero al menos tienen uno. Los sensores deben almacenar
    por separado la magnitud leída de su unidad de medición.Además cada estación almacena el voltaje en milivolts de su batería una
    vez por segundo y el formato de archivo debe mantener las últimas 20 mediciones.
    Diseñar un formato XML y uno JSON para intercambiar datos del sistema. Cree dos documentos para almacenar la misma información.
    """
    submenu = """
    ------------------------------------------------
    Menu
    ------------------------------------------------
    Se le consultara que base desea usar:
        [j] JSON
        [x] XML

    Y luego podrá elegir de las siguientes acciones:
        [1] Buscar estacion
        [2] Ver estacion con menos bateria
        [3] Ver archivo
    -----------------------------------------------
    """
    enunciado1 = """
    1. A partir del nombre de la estación, computar la cantidad de sensores disponible y mostrar por pantalla los diferentes sensores,
    cada uno deberá mostrar el tipo y la variable medida, por ejemplo:
        Cantidad de sensores de la estación “Sur10”: 3
        Temperatura: 10०C
        Humedad: 1013 hpa
        Velocidad Viento: 30km/h
    """
    enunciado2 = """
    2. Calcular cuál es la estación con menos batería, es decir, la estación con menor valor promedio de voltaje.

    Elija solo una representación (XML o JSON) para implementar las soluciones de 1 y 2.
    Opcional: Implemente la solución utilizando la representación restante.
    """

    # Carga DB JSON
    with open('estaciones.json', encoding='utf-8') as file_json:
        db_json = json.load(file_json)

    # Carga DB XML
    file_xml = ET.parse("estaciones-v2.xml")
    db_xml = file_xml.getroot()

    print(enunciado)
    input("Presione [ENTER] para ver la continuar...")
    print(submenu)

    while True:
        # Elige un formato de base de datos
        formato = input("[>] Que formato quiere usar? [j] JSON [x] XML - [s] salir: ")
        if formato == "j":
            print("[j] Ver JSON\n")
            fname = "JSON"
        elif formato == "x":
            print("[x] Ver XML\n")
            fname = "XML"
        elif formato == "s":
            print("[s] Saliendo de Estaciones Meteorologicas...")
            break
        else:
            print("[!] ERROR: Ingrese una opcion valida!\n")
        
        if formato == "j" or formato == "x":
            # Elegir accion
            while True:
                action = input("[>] [{fname}] Que desea hacer? [1] Buscar estacion [2] Ver Bateria [3] Ver Base - [s] salir: ".format(fname=fname))
                if action == "1" and formato == "j":
                    print("[1] [JSON] Buscar Estacion\n")
                    print(enunciado1)
                    ejc1_extra_listado_estaciones(formato, db_json)
                    ejc1_buscar_estacion(formato, db_json)
                elif action == "2" and formato == "j":
                    print("[2] [JSON] Ver Estación con menos Batería\n")
                    print(enunciado2)
                    ejc2_ver_bateria(formato, db_json)
                elif action == "3" and formato == "j":
                    print("[3] [JSON] Ver Base de Datos\n")
                    print(db_json)
                elif action == "s" and formato == "j":
                    print("[s] [JSON] Saliendo de acciones\n")
                    break
                elif action == "1" and formato == "x":
                    print("[1] [XML] Buscar Estacion\n")
                    print(enunciado1)
                    ejc1_extra_listado_estaciones(formato, db_xml)
                    ejc1_buscar_estacion(formato, db_xml)
                elif action == "2" and formato == "x":
                    print("[2] [XML] Ver Estación con menos Batería\n")
                    print(enunciado2)
                    ejc2_ver_bateria(formato, db_xml)
                elif action == "3" and formato == "x":
                    print("[3] [XML] Ver Base de Datos\n")
                    with open("estaciones.xml", 'r', encoding="utf-8") as f:
                        print(f.read())
                elif action == "s" and formato == "x":
                    print("[s] [XML] Saliendo de acciones\n")
                    break
                else:
                    print("[!] ERROR: Ingrese una opcion valida!\n")
    elegir()


def ejc1_buscar_estacion(formato, db):
    # buscar estacion en base al nombre
    nombre = input("[>] Ingrese el nombre de la estacion: ").capitalize()

    # Formato JSON
    if formato == "j":
        match = []
        estaciones = db["estaciones"]
        for estacion in db["estaciones"]:
            if nombre == estacion["nombre"]:
                match = estacion
        if not match:
            print("[!] ERROR: No se encontró una estación con el nombre {nombre}".format(nombre=nombre))
        else:
            cantidad_sensores = len(match["sensores"])
            print("\n\tEstación {nombre}\t\t\tSensores: {cantidad_sensores}".format(nombre=nombre, cantidad_sensores=cantidad_sensores))
            print("\t------------------------------------------------")
            for sensor in match["sensores"]:
                print("\t\t{nombre}: {valor} {unidad}".format(nombre=sensor["nombre"], valor=sensor["valor"], unidad=sensor["unidad"]))
            print("\t------------------------------------------------\n")
    # Formato XML
    elif formato == "x":
        estaciones = db.findall("estaciones")
        for estacion in estaciones:
            if nombre == estacion.find("nombre").text:
                match = estacion
        if not match:
            print("[!] ERROR: No se encontró una estación con el nombre {nombre}".format(nombre=nombre))
        else:
            cantidad_sensores = len(match.findall("sensores/sensor"))
            print("\n\tEstación {nombre}\t\t\tSensores: {cantidad_sensores}".format(nombre=nombre, cantidad_sensores=cantidad_sensores))
            print("\t------------------------------------------------")
            for sensor in match.findall("sensores/sensor"):
                nombre = sensor.find("nombre").text
                valor = sensor.find("valor").text
                unidad = sensor.find("unidad").text
                print("\t\t{nombre}: {valor} {unidad}".format(nombre=nombre, valor=valor, unidad=unidad))
            print("\t------------------------------------------------\n")

def ejc1_extra_listado_estaciones(formato, db):
    print("\tListado de Estaciones:")
    print("\t----------------------------")
    # Formato JSON
    if formato == "j":
        estaciones = db["estaciones"]
        for estacion in db["estaciones"]:
            print("\t" + estacion["nombre"])        
    # Formato XML
    else:
        estaciones = db.findall("estaciones")
        for estacion in estaciones:
            print("\t" + estacion.find("nombre").text)

    print("\t----------------------------")


def ejc2_ver_bateria(formato, db):
    # retorna estación con menor promedio de batería
    menor_promedio = 100
    menor_nombre = ''
    if formato == "j":
        # Formato JSON
        estaciones = db["estaciones"]
        for estacion in estaciones:
            bateria = estacion["bateria"]
            nombre = estacion["nombre"]
            promedio = sum(bateria) / len(bateria)
            if promedio < menor_promedio:
                menor_promedio = promedio
                menor_nombre = nombre
    elif formato == "x":
        # Formato XML
        estaciones = db.findall("estaciones")
        for estacion in estaciones:
            nombre = estacion.find("nombre").text
            str_bateria = bateria.find("valor").text

            list_bateria = str_bateria.split(',')
            bateria = [int(n) for n in list_bateria]
            promedio = sum(bateria) / len(bateria)
            if promedio < menor_promedio:
                menor_promedio = promedio
                menor_nombre = nombre
    
    if not menor_nombre:
        print("[!] ERROR: No se encontró la estación con menor promedio de bateria\n")
    else:
        print("[-] Bateria: La estación {nombre} es la que menor batería tiene con un promedio de {promedio}\n".format(nombre=nombre, promedio=promedio))

# ----------------------------------------------------
# Programa principal
welcome()
menu()
# Seleccion inicial
routing(select_option())


# To Do
# ----------------------------------------------------
# 🆖 Clear Screen: No funciona bien en Pycharm
# 🆖 Emprolijar ejercicio 6, insertarlo al menu de navegacion.
# 🆗 Pausa antes de la solucion para los ej Expresion Regular
