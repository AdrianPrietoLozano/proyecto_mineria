
import pandas, json
import numpy as np
import math
from holdOut import HoldOut


def main_HoldOut(data, target, bandera_cat_num, algoritmo, iteraciones, arrayOrden):

    # Creamos la instancia de holdOut
    h_Out = HoldOut(data, target)

    # Obtenemos los tamaños
    h_Out.tamaniosEntrenamientoPrueba(70, 30)


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
    
    return exactitudFinal, dataframeFinal

def numerico_HoldOut(data, target, iteraciones):
    h_Out = HoldOut(data, target)
    h_Out.tamaniosEntrenamientoPrueba(70, 30)
    arrayErrorCuadratico = []
    for i in range(0, iteraciones):
        valor = h_Out.errorCuadraticoMedio()
        arrayErrorCuadratico.append(valor)
    resultado = h_Out.promedioConTamanio(arrayErrorCuadratico)
    tabla = pandas.DataFrame(columns=["Error cuadrático medio"], index=["KNN"])
    tabla.loc["KNN"] = resultado
    return tabla

