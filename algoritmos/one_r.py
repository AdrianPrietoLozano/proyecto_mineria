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
            reglas[atributo]["regla"][val] = {}
            mayor = frecuencias[atributo][val].idxmax() # encuentra el index de la fila con el mayor elemento
            total = frecuencias[atributo][val].sum()

            numerador = total - frecuencias[atributo][val][mayor]
            numerador_error_total += numerador
            denominador_error_total += total

            reglas[atributo]["regla"][val][mayor] = str(numerador) + "/" + str(total)

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



"""
data = pandas.read_csv("adult.csv", skipinitialspace=True)
target = "y"
data.drop(["id", "fnlwgt"], axis=1, inplace=True)

frecuencias = generar_frecuencias_pandas(data, target)

for frecuencia in frecuencias.values():
    print(frecuencia)


reglas = generar_reglas(frecuencias)


print("---------------------------------------------------------------")
print("FRECUENCIAS")
#imprimirDiccionarioFrecuencia(frecuencias)
#print(frecuencias)
        

print()
print("---------------------------------------------------------------")
print("REGLAS")
#print(reglas)
print(json.dumps(reglas, indent=2))
#print(json.dumps())
print("---------------------------------------------------------------")
menor = encontrar_error_menor(reglas)
print("RESULTADO FINAL")
print(menor)
for i in reglas[menor]["regla"]:
    print("\t", i, "-> ", end="")
    for j in reglas[menor]["regla"][i]:
        print(j)
"""

"""
IMPRIMIR TABLAS CON TABULATE

print(frecuencias)

headers = [""] + list(data[target].unique())

for i in frecuencias:
    print("\n\n", i)
    datos = []
    for j in frecuencias[i]:
        fila = [j]
        for k in frecuencias[i][j].values():
            fila.append(k)
        datos.append(fila)

    print(tabulate(datos, headers, tablefmt="pretty"))

"""

"""
def imprimirDiccionarioFrecuencia(diccionario):
    for i in diccionario:
        print(i + ': ')
        for j in diccionario[i]:
            print('    ', j + ': ')
            for k,v in diccionario[i][j].items():
                print('        ', k + ':', v)
            print()
        print()
    print("Se termino de imprimir")


def imprimirDiccionarioReglas(diccionario):
    for i in diccionario:
        print(i, ': ')
        for j in diccionario[i]:
            print(' ', j, ': ')
            for k,v in diccionario[i][j].items():
                print(' ', k, ': ', v)
            print()
        print()
    print("Se termino de imprimir")
"""