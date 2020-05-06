import pandas

def generar_frecuencias(data, target):
    """ Genera la tabla de frecuencias """
    frecuencias = {}
    for val in data[target].unique():
        frecuencias[val] = len(data[data[target] == val])

    return frecuencias

def obtenerMayor(frecuencias):
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


"""
def zeroR(data):
    #data = pandas.read_csv("tabla2.csv", skipinitialspace=True)
    target = input("ingresa el target: ")
    print(f"Target Seleccionado:{target}")

    try:
        frecuencias = generar_frecuencias(data, target)
        
        print("FRECUENCIA")
        print(frecuencias)
        print()
        print("---------------------------------------------------------------")
        print("Obtener Mayor")
        clase, division = obtenerMayor(frecuencias)
        print("El mayor es:",clase)
        print("El resultado de la operacion es:", division)
        
        print()
        os.system("pause")
        os.system("cls")

    except:
        print("El target no es valido, pruebe con otro")
        print()
        os.system("pause")
        os.system("cls")

"""