
import pandas, json
import numpy as np
import math
from holdOut import HoldOut

#data = pandas.read_csv("iris.csv", skipinitialspace=True)
#target = "class"



#Iniciamos el proceso

# Leemos nuestro csv

# Vere si el orden también, aunque si se necesitara
def main_HoldOut(data, target, bandera_cat_num, algoritmo, iteraciones, arrayOrden):

    # Creamos la instancia de holdOut
    h_Out = HoldOut(data, target)

    #bandera_cat_num = h_Out.tipoTarget()

    # Obtenemos los tamaños
    h_Out.tamaniosEntrenamientoPrueba(70, 30)

    # Creación del orden de la matriz de confusión
    #arrayOrden = h_Out.nuevoOrden(data, target)
    #print("El orden que se seguira sera:", arrayOrden)


    # --------------------------------------
    # A partir de aquí, es el bucle

    arrayExactitud = []
    arrayRecall = []
    arrayPrecision = []

    for i in range(0, iteraciones):
        auxExactitud, auxRecall, auxPrecision = h_Out.procesoCompleto(algoritmo, bandera_cat_num, arrayOrden)
        arrayExactitud.append(auxExactitud)
        arrayRecall.append(auxRecall)
        arrayPrecision.append(auxPrecision)

    exactitudFinal = h_Out.promedioConTamanio(arrayExactitud)


    recallFinal = h_Out.promedioConTamanio_Diccionarios(arrayRecall)
    precisionFinal = h_Out.promedioConTamanio_Diccionarios(arrayPrecision)
    dataframeFinal = h_Out.combinarRecall_Precision(recallFinal, precisionFinal)

    #print("Exactitud Final: ", exactitudFinal)
    #print("Dataframe Final: ")
    #print(dataframeFinal)
    #print()
    return exactitudFinal, dataframeFinal

#data = pandas.read_csv("tabla1.csv", skipinitialspace=True)
#target = "Sail"

#data = pandas.read_csv("iris.csv", skipinitialspace=True)
#target = "class"

#data = pandas.read_csv("randomOneRKnn.csv", skipinitialspace=True)
#target = "Sail"

#algoritmo = "Naive Bayes"
#algoritmo = "One R"
#algoritmo = "KNN"

#iteraciones = 10

#main_HoldOut(data, target, algoritmo, iteraciones)


"""

if algoritmo == "Naive Bayes":
resultadoEntrenamiento, resultadoPrueba, realEntrenamiento, realPrueba = self.resultadoModeloNaive()

if algoritmo == "One R":
print("Alo")

if algoritmo == "KNN":

"""


#opcionOneR()



