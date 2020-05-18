import pandas

def generar_frecuencias(data, target):
    """ Genera la tabla de frecuencias """
    frecuencias = {}
    for val in data[target].unique():
        frecuencias[val] = len(data[data[target] == val])

    return frecuencias

def obtenerMayor(frecuencias):
    # Se encuentra el umbral del target
    denominador = 0
    clase = ""
    numerador = 0
    for i in frecuencias:
        valor = frecuencias[i]
        denominador += valor
        if(numerador < valor):
            numerador = valor
            clase = i
    division = numerador / denominador
    return clase, division
