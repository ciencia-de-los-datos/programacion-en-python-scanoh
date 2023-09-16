"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    with open(r'data.csv', 'r') as file:
        for line in file:
            values = line.strip().split('\t')
            if len(values) >= 2:
                suma += int(values[1])
    return suma 


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    conteo_letras = {}

    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split('\t')
        if parts:
            primera_letra = parts[0][0] 
            if primera_letra in conteo_letras:
                conteo_letras[primera_letra] += 1
            else:
                conteo_letras[primera_letra] = 1

    resultado_02 = sorted(conteo_letras.items())
    return resultado_02


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    registros_por_mes = {}
    with open('data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                fecha = parts[2]
                mes = fecha.split('-')[1]
                if mes in registros_por_mes:
                    registros_por_mes[mes] += 1
                else:
                    registros_por_mes[mes] = 1

    resultado_04 = sorted(registros_por_mes.items())

    return resultado_04


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    max_min_por_letra = {}

    with open(r'data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 2:
                letra = parts[0]
                valor = int(parts[1])
                if letra in max_min_por_letra:
                    max_min_por_letra[letra][0] = max(max_min_por_letra[letra][0], valor)
                    max_min_por_letra[letra][1] = min(max_min_por_letra[letra][1], valor)
                else:
                    max_min_por_letra[letra] = [valor, valor]

    resultado_05 = [(letra, max_min[0], max_min[1]) for letra, max_min in max_min_por_letra.items()]
    resultado_05 = sorted(resultado_05, key=lambda x: x[0])

    return resultado_05


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    min_max_por_clave = {}

    with open(r'data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:
                columna5 = parts[4]
                elementos = columna5.split(',')
                for elemento in elementos:
                    if ':' in elemento:
                        clave, valor_str = elemento.split(':')
                        valor = int(valor_str)
                        if clave in min_max_por_clave:
                            min_max_por_clave[clave][0] = min(min_max_por_clave[clave][0], valor)
                            min_max_por_clave[clave][1] = max(min_max_por_clave[clave][1], valor)
                        else:
                           
                            min_max_por_clave[clave] = [valor, valor]

    resultado_06 = [(clave, min_max[0], min_max[1]) for clave, min_max in min_max_por_clave.items()]
    resultado_06 = sorted(resultado_06, key=lambda x: x[0])

    return resultado_06


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    asociaciones = {}
    with open(r'data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) > 2:
            valor_columna_2 = int(parts[1])
            letra_columna_1 = parts[0]
            
            if valor_columna_2 in asociaciones:
                asociaciones[valor_columna_2].append(letra_columna_1)
            else:
                asociaciones[valor_columna_2] = [letra_columna_1]

    respuesta_07 = list(asociaciones.items())
    respuesta_07 = sorted(respuesta_07, key=lambda x: x[0])

    return respuesta_07


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    asociaciones = {}
    with open(r'data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) > 2:
            valor_columna_2 = int(parts[1])
            letra_columna_1 = parts[0]
            
            if valor_columna_2 in asociaciones:
                if letra_columna_1 not in asociaciones[valor_columna_2]:
                    asociaciones[valor_columna_2].append(letra_columna_1)
            else:
                asociaciones[valor_columna_2] = [letra_columna_1]
        for key in asociaciones:
            asociaciones[key] = sorted(asociaciones[key])

    respuesta_08 = list(asociaciones.items())
    respuesta_08 = sorted(respuesta_08, key=lambda x: x[0])

    return respuesta_08


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    contar_clave = {}

    with open(r'data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:
                columna5 = parts[4]
                elementos = columna5.split(',')
                for elemento in elementos:
                    if ':' in elemento:
                        clave, _ = elemento.split(':')
                        if clave in contar_clave:
                            contar_clave[clave] += 1
                        else:
                            contar_clave[clave] = 1

    resultado_09 = sorted(contar_clave.items(), key=lambda x: x[0])
    resultado_09 = dict(sorted(contar_clave.items()))

    return resultado_09


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    resultado_10 = []

    with open(r'data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:
                letra_columna_1 = parts[0]
                elementos_columna_4 = parts[3].split(',')
                elementos_columna_5 = parts[4].split(',')
                cantidad_elementos = (len(elementos_columna_4), len(elementos_columna_5))

                tupla = (letra_columna_1, *cantidad_elementos)
                resultado_10.append(tupla)

    return resultado_10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_por_letra = {}

    with open(r'data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:
                columna_2 = int(parts[1])
                letras_columna_4 = parts[3].split(',')
                for letra in letras_columna_4:
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += columna_2
                    else:
                        suma_por_letra[letra] = columna_2

    resultado_11 = dict(sorted(suma_por_letra.items()))

    return resultado_11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_por_letra = {}

    with open(r'data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:
                letra_columna_1 = parts[0]
                elementos_columna_5 = parts[4].split(',')
                suma = 0

                for elemento in elementos_columna_5:
                    clave, valor_str = elemento.split(':')
                    valor = int(valor_str)
                    suma += valor

                if letra_columna_1 in suma_por_letra:
                    suma_por_letra[letra_columna_1] += suma
                else:
                    suma_por_letra[letra_columna_1] = suma

    resultado_12 = dict(sorted(suma_por_letra.items()))

    return resultado_12
