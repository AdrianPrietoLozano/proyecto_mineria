import pandas, json


def generar_frecuencias(data, target, sumar=0):
    frecuencias = {}

    for atributo in data.columns:
        if atributo == target: # el target se debe omitir
            continue

        frecuencias[atributo] = pandas.crosstab(columns=data[atributo].astype(str), index=data[target].astype(str))

    
    if sumar != 0:
        for atributo in frecuencias:
            frecuencias[atributo] = frecuencias[atributo].apply(lambda x: x + sumar, axis=1)

    return frecuencias



# recibe como parámetro un diccionario con las frecuencias (lo que retorna la función generar_frecuencias)
def generar_reglas(frecuencias):

    reglas = {}

    for atributo in frecuencias:
        reglas[atributo] = {}
        reglas[atributo]["regla"] = {}

        numerador_error_total = 0
        denominador_error_total = 0
        for val in frecuencias[atributo].columns:
            
            mayor = frecuencias[atributo][val].idxmax() # encuentra el index de la fila con el mayor elemento
            total = frecuencias[atributo][val].sum()

            numerador = total - frecuencias[atributo][val][mayor]
            numerador_error_total += numerador
            denominador_error_total += total

            reglas[atributo]["regla"][val] = [mayor, str(numerador) + "/" + str(total)]

        reglas[atributo]["error_total"] = numerador_error_total / denominador_error_total

    return reglas




# el parámetro reglas es un diccionario con las reglas (lo que retorna la función generar_reglas)
def encontrar_error_menor(reglas):
    """ Retorna el nombre del atributo que tiene el error menor """
    menor = list(reglas.keys())[0]

    for atributo in reglas:
        if reglas[atributo]["error_total"] < reglas[menor]["error_total"]:
            menor = atributo

    return menor
