import pandas, json
import numpy as np
import math

from algoritmos.naive import NaiveBayes
from algoritmos.one_r import *
from algoritmos.knn import KNN


class HoldOut:
    def __init__(self, data, target):
        self.data = data
        self.target = target
        self.tamanioData = len(data)

        self.tamanioEntrenamiento = 0
        self.tamanioPrueba = 0

        self.dataEntrenamiento = data
        self.dataPrueba = data

        self.arrayEntrenamientoReal = []
        self.arrayPruebaReal = []
        
    
    def porcentaje(self, percent, total):
        return (percent * total) / 100.0
    
    def parteEntera(self, tamanio):
        b = str(tamanio).split(".")
        parte_entera = int(b[0])
        #print(parte_entera)
        numeroMayor = parte_entera + 0.6
        if tamanio >= numeroMayor:
            #print("Simon")
            tamanio = parte_entera + 1
        else:
            #print("Nel")
            tamanio = parte_entera
        return tamanio

    def tamaniosEntrenamientoPrueba(self, entrenamiento, prueba):
        self.tamanioEntrenamiento = self.porcentaje(entrenamiento, self.tamanioData)
        auxTamanio = self.tamanioEntrenamiento
        self.tamanioEntrenamiento = self.parteEntera(auxTamanio)

        self.tamanioPrueba = self.porcentaje(prueba, self.tamanioData)
        auxTamanio = self.tamanioPrueba
        self.tamanioPrueba = self.parteEntera(auxTamanio)


    def nuevoDataframe(self, nuevoDataframe):
        self.data = nuevoDataframe
    
    def inicializarArrayEntrenamientoPrueba(self):
        self.dataEntrenamiento = self.data.head(self.tamanioEntrenamiento)
        self.dataPrueba = self.data.tail(self.tamanioPrueba)
    
    def inicializarArrayEntrenamientoPruebaReal(self):
        self.arrayEntrenamientoReal = self.obtenerValoresTarget(self.dataEntrenamiento, self.target)
        self.arrayPruebaReal = self.obtenerValoresTarget(self.dataPrueba, self.target)
        return self.arrayEntrenamientoReal, self.arrayPruebaReal
    
    # Se le pasa el dataset completo, sin borrar el target
    def obtenerValoresTarget(self, dataset, target):
        arreglo = []
        for i in dataset[target]:
            #print(i)
            arreglo.append(i)
        return arreglo
    
    
    


    

    def obtenerNumerosMatriz(self, arrayResultado, arrayReal):
        diccionario = {}
        for i, j in zip(arrayResultado,arrayReal):
            contador = 0
            valorRes = i
            valorReal = j
            for k, n in zip(arrayResultado,arrayReal):
                auxRes = k
                auxReal = n
                if valorRes == auxRes:
                    if valorReal == auxReal:
                        #print("Si es igual uwu")
                        contador += 1
            llave = valorRes + '/' + valorReal
            diccionario[llave] = contador
        return diccionario
    
    def nuevoOrden(self, data, target):
        datosUnicos = []
        datosUnicos = pandas.unique(data[target]).tolist()
        print("El orden de las clases es el siguiente:")
        self.recorridoArreglo(datosUnicos)
        print("Favor de seleccionar el orden que desea")
        print("Ejemplo de orden, 0: Cat, 1: Fish, 2: Turtle")
        print("Nosotros solo pondremos el orden que queremos separado por comas")
        print("Ejemplo de seleccion: 1,0,2")
        print()
        orden = input("Orden deseado: ")
        arrayOrden = self.separarComas(orden, datosUnicos)
        return arrayOrden
    
    def recorridoArreglo(self, arreglo):
        for i in range (0, len(arreglo)):
            aux = arreglo[i]
            print(str(i) + ": " + aux)
        print()
    
    def separarComas(self, palabra, arreglo):
        newOrder = []
        auxPalabra = palabra.split(",")
        for i in auxPalabra:
            aux = arreglo[int(i)]
            newOrder.append(aux)
        return newOrder
    
    # Creacion de la matriz n x n en 0
    def crearMatrizConfusion(self, arreglo):
        tamanioArray = len(arreglo)
        df = pandas.DataFrame(0, columns=arreglo, index=arreglo)
        return df

    def buscarDiccionario(self, diccionario, llave):
        retornoValor = 0
        for clave, valor in diccionario.items():
            #print(clave, ":", valor)
            if clave == llave:
                retornoValor = valor
                return retornoValor
        #print("No se encontro el valor")
        return retornoValor

    def llenarMatrizConfusion(self, dataframe, diccionario):
        for i in range(0, len(dataframe)):
            for j in range(0, len(dataframe)):
                nombreFila = dataframe.index[i]
                nombreColumna = dataframe.columns[j]
                llave = nombreFila + "/" + nombreColumna #yes/yes
                valor = self.buscarDiccionario(diccionario, llave)
                # No se por qué se invierten, antes estaba asi:
                #dataframe[nombreFila][nombreColumna] = valor
                dataframe[nombreColumna][nombreFila] = valor
                #print("Nuevo valor:", valor)
        return dataframe


    def obtenerExactitud(self, dataframe):
        exactitud = np.trace(dataframe) / dataframe.sum().sum()
        return exactitud
    
    def sumarArreglo(self, arreglo):
        valor = 0
        for i in arreglo:
            valor += i
        return valor
    
    def convertirFila_Array(self, dataframe, clase):
        arreglo = []
        for i in dataframe:
            aux = dataframe[i][clase]
            arreglo.append(aux)
        return arreglo

    def recall_or_precision(self, dataframe, columna, bandera):
        # Recall = 0
        dividendo = 0.0
        if bandera == 0:
            dividendo = dataframe[columna].sum()
        # Precision = 1
        if bandera == 1:
            arreglo = self.convertirFila_Array(dataframe, columna)
            dividendo = self.sumarArreglo(arreglo)
        return dividendo
    
    def division_Recall_Precision(self, dataframe, fila, columna, bandera):
        divisor = dataframe[fila][columna]
        #print("Divisor:", divisor)
        dividendo = self.recall_or_precision(dataframe, columna, bandera)
        if dividendo == 0:
            dividendo = 0.00001
        #print("Dividendo:", dividendo)
        division = divisor / dividendo
        return division
    
    def obtenerRecalls_Precisiones(self, dataframe, bandera):
        diccionario = {}
        for i in range(0, len(dataframe)):
            nombreFila = dataframe.index[i]
            nombreColumna = dataframe.columns[i]
            # Recall = 0
            if bandera == 0:
                valor = self.division_Recall_Precision(dataframe, nombreFila, nombreColumna, bandera)
            # Precisión = 1
            if bandera == 1:
                valor = self.division_Recall_Precision(dataframe, nombreFila, nombreColumna, bandera)
            diccionario[nombreFila] = valor
        return diccionario
    
    def promediar(self, valor1, valor2):
        divisor = valor1 + valor2
        dividendo = 2
        promedio = divisor / dividendo
        return promedio
    
    # Obtiene el promedio entre dos diccionarios y retorna el diccionario final
    def promediarConDiccionario(self, entrenamiento, prueba):
        newDiccionario = {}
        for llaveEntre, valorEntre in entrenamiento.items():
            for llavePrue, valorPrue in prueba.items():
                if llaveEntre == llavePrue:
                    promedio = self.promediar(valorEntre, valorPrue)
                    newDiccionario[llaveEntre] = promedio
        return newDiccionario


    def promedioConTamanio(self, arreglo):
        divisor = 0.0
        for i in arreglo:
            divisor += i
        dividendo = len(arreglo)
        promedio = divisor / dividendo
        return promedio
    
    # Obtiene el promedio de todos los diccionarios que se iteraron (sea sensibilidad o precisión)
    def promedioConTamanio_Diccionarios(self, arregloDic):
        clasesUnicas = pandas.unique(self.data[self.target]).tolist()
        diccionario = {}
        for clase in clasesUnicas: # Recorrde el arreglo de los valores unicos de la clase
            arregloClase = []    
            for i in arregloDic: # Recorrde el arreglo de todos los diccionarios
                diccionario = i
                for clave, valor in diccionario.items(): # Recorremos los valores de nuestro diccionario
                    if clave == clase: # Sí la clave es igual a la clase que esta en el primer for, entra
                        arregloClase.append(valor) # Lo agregamos a nuestra lista de clases
            promedio = self.promedioConTamanio(arregloClase) # Promediamos los valores que coinciden con clase
            diccionario[clase] = promedio # Agregamos el valor final a nuestro diccionario
        return diccionario
    
    def combinarRecall_Precision(self, dicRecall, dicPrecision):
        df_recall = pandas.DataFrame.from_dict(dicRecall, orient="index")
        df_recall.columns = ['Sensibilidad']
        #print(df_recall)
        #print()
        df_precision = pandas.DataFrame.from_dict(dicPrecision, orient="index")
        df_precision.columns = ['Precisión']
        #print(df_precision)
        #print()
        df_recall = pandas.concat([df_precision, df_recall], axis=1,)
        #print(df_recall)
        #print()
        return df_recall
















    # -------------------------------------------------------


    # Naive Bayes
    def resultadoModeloNaive(self):
        resultadoPrueba = []
        resultadoEntrenamiento = []

        realPrueba = []
        realEntrenamiento = []

        self.inicializarArrayEntrenamientoPrueba()
        realEntrenamiento, realPrueba = self.inicializarArrayEntrenamientoPruebaReal()
    
        entrenamiento = self.data.head(self.tamanioEntrenamiento)
        prueba = self.data.tail(self.tamanioPrueba)

        prueba.drop(self.target, inplace=True, axis=1)
        entrenamiento.drop(self.target, inplace=True, axis=1)

        naive_bayes = NaiveBayes(self.dataEntrenamiento, self.target)

        for i in prueba.values:
            diccionario = {}
            for j,k in zip(prueba.columns,i):
                diccionario[j] = k
            resultado, palabra = naive_bayes.get_prediccion(diccionario)
            #print("El segundo return de palabra:", palabra)
            #print(max(resultado,key=resultado.get))
            resultadoPrueba.append(max(resultado,key=resultado.get))

        naive_bayes = NaiveBayes(self.dataPrueba, self.target)

        for i in entrenamiento.values:
            diccionario = {}
            for j,k in zip(entrenamiento.columns,i):
                diccionario[j] = k
            resultado, palabra = naive_bayes.get_prediccion(diccionario)
            #print("El segundo return de palabra:", palabra)
            #print(max(resultado,key=resultado.get))
            resultadoEntrenamiento.append(max(resultado,key=resultado.get))

        return resultadoEntrenamiento, resultadoPrueba, realEntrenamiento, realPrueba


    # -------------------------------------------------------

    # One R
    def resultadoModeloOneR(self):

        # Creacion de las listas de resultados
        resultadoEntrenamiento = []
        resultadoPrueba = []
        
        # Creación de las listas del data real
        realEntrenamiento = []
        realPrueba = []

        # Inicializamos las listas con los valores de clase reales
        self.inicializarArrayEntrenamientoPrueba()
        realEntrenamiento, realPrueba = self.inicializarArrayEntrenamientoPruebaReal()

        # Inicializamos la información que se utilizará en dataframe
        entrenamiento = self.data.head(self.tamanioEntrenamiento)
        prueba = self.data.tail(self.tamanioPrueba)

        # ---------------------------------------------------------------
        # Proceso con Entrenamiento

        frecuencias = generar_frecuencias(entrenamiento, self.target)
        reglas = generar_reglas(frecuencias)
        menor = encontrar_error_menor(reglas)

        # Todos los valores de la regla menor resultante
        resultadoEntrenamiento = entrenamiento[menor].tolist()
        
        # Obtenemos todos los valores de predicción en target de nuestra regla
        for llave, valor in reglas[menor]["regla"].items():
            auxValor = valor[0]
            for m in range(0, len(resultadoEntrenamiento)):
                auxLlave = resultadoEntrenamiento[m]
                if auxLlave == llave:
                    resultadoEntrenamiento[m] = auxValor
        

        # ---------------------------------------------------------------
        # Proceso con Prueba

        frecuencias = generar_frecuencias(prueba, self.target)
        reglas = generar_reglas(frecuencias)
        menor = encontrar_error_menor(reglas)

        # Todos los valores de la regla menor resultante
        resultadoPrueba = prueba[menor].tolist()
        
        for llave, valor in reglas[menor]["regla"].items():
            auxValor = valor[0]
            for m in range(0, len(resultadoPrueba)):
                auxLlave = resultadoPrueba[m]
                if auxLlave == llave:
                    resultadoPrueba[m] = auxValor

        return resultadoEntrenamiento, resultadoPrueba, realEntrenamiento, realPrueba

    # -------------------------------------------------------

    # KNN

    def resultadoModeloKNN_Categorico(self):

        # Creacion de las listas de resultados
        resultadoEntrenamiento = []
        resultadoPrueba = []
        
        # Creación de las listas del data real
        realEntrenamiento = []
        realPrueba = []

        # Inicializamos las listas con los valores de clase reales
        self.inicializarArrayEntrenamientoPrueba()
        realEntrenamiento, realPrueba = self.inicializarArrayEntrenamientoPruebaReal()

        # Inicializamos la información que se utilizará en dataframe
        entrenamiento = self.data.head(self.tamanioEntrenamiento)
        prueba = self.data.tail(self.tamanioPrueba)

        # ---------------------------------------------------------------
        # Proceso con Prueba
        pos_target = self.data.columns.get_loc(self.target)
        knn = KNN(entrenamiento, self.target)
        for i in prueba.values:
            prediccion = knn.get_prediccion(np.delete(i, pos_target))[0]
            real = i[pos_target] # valor real del conjunto de prueba
            #print(prediccion, real)
            resultadoPrueba.append(prediccion)

        # ---------------------------------------------------------------
        # Proceso con Entrenamiento
        pos_target = self.data.columns.get_loc(self.target)
        knn = KNN(prueba, self.target)
        for i in entrenamiento.values:
            prediccion = knn.get_prediccion(np.delete(i, pos_target))[0]
            real = i[pos_target] # valor real del conjunto de prueba
            #print(prediccion, real)
            resultadoEntrenamiento.append(prediccion)
        

        return resultadoEntrenamiento, resultadoPrueba, realEntrenamiento, realPrueba

    

    # -------------------------------------------------------

    def tipoTarget(self):
        es_regresion = 0
        if np.issubdtype(self.data[self.target].dtype, np.number):
            es_regresion = 1
        return es_regresion



    def procesoCompleto(self, algoritmo, bandera_cat_num, arrayOrden):
        # Inicializamos las dos matrices
        dataMatrizConfusionEntrenamiento = self.crearMatrizConfusion(arrayOrden)
        dataMatrizConfusionPrueba = self.crearMatrizConfusion(arrayOrden)

        # Creamos un dataset random
        auxData = self.data.sample(frac=1)
        self.nuevoDataframe(auxData)

        # Inicializamos los arreglos de los resultados obtenidos
        resultadoEntrenamiento = []
        resultadoPrueba = []

        # Inicializamos los arreglos de los resultados reales del dataframe
        realEntrenamiento = []
        realPrueba = []
        
        # Inicializamos los arreglos de los resultados obtenidos
        if algoritmo == "Naive Bayes":
            resultadoEntrenamiento, resultadoPrueba, realEntrenamiento, realPrueba = self.resultadoModeloNaive()

        if algoritmo == "One R":
            resultadoEntrenamiento, resultadoPrueba, realEntrenamiento, realPrueba = self.resultadoModeloOneR()
        
        if algoritmo == "KNN":
            resultadoEntrenamiento, resultadoPrueba, realEntrenamiento, realPrueba = self.resultadoModeloKNN_Categorico()



        # Creamos las repeticiones de cada clase
        diccionarioEntrenamiento = {}
        diccionarioPrueba = {}
        diccionarioEntrenamiento = self.obtenerNumerosMatriz(resultadoEntrenamiento, realEntrenamiento)
        diccionarioPrueba = self.obtenerNumerosMatriz(resultadoPrueba, realPrueba)
        
        # Creamos nuestra matriz de confusión vacia
        dataMatrizConfusionEntrenamiento = self.crearMatrizConfusion(arrayOrden)
        dataMatrizConfusionPrueba = self.crearMatrizConfusion(arrayOrden)

        # Llenamos los valores con las repeticiones
        matrizConfusionEntrenamientoValores = self.llenarMatrizConfusion(dataMatrizConfusionEntrenamiento, diccionarioEntrenamiento)
        matrizConfusionPruebaValores = self.llenarMatrizConfusion(dataMatrizConfusionPrueba, diccionarioPrueba)

        # Obtenemos la Exactitud
        exactitudEntrenamiento = self.obtenerExactitud(matrizConfusionEntrenamientoValores)
        exactitudPrueba = self.obtenerExactitud(matrizConfusionPruebaValores)

        # Procedimiento Recall y Precisión
        # Recall = 0
        # Precisión = 1

        # Recall
        entrenamientoDicRecalls = self.obtenerRecalls_Precisiones(matrizConfusionEntrenamientoValores, 0)
        pruebaDicRecalls = self.obtenerRecalls_Precisiones(matrizConfusionPruebaValores, 0)

        # Precisón
        entrenamientoDicPrecision = self.obtenerRecalls_Precisiones(matrizConfusionEntrenamientoValores, 1)
        pruebaDicPrecision = self.obtenerRecalls_Precisiones(matrizConfusionPruebaValores, 1)

        # Obtenemos sus promedios
        promedioExactitud = self.promediar(exactitudEntrenamiento, exactitudPrueba)
        promedioRecall = self.promediarConDiccionario(entrenamientoDicRecalls, pruebaDicRecalls)
        promedioPrecision = self.promediarConDiccionario(entrenamientoDicPrecision, pruebaDicPrecision)

        return promedioExactitud, promedioRecall, promedioPrecision
    
    def errorCuadraticoMedio(self):
        auxData = self.data.sample(frac=1)
        self.nuevoDataframe(auxData)
        
        entrenamiento = self.data.head(self.tamanioEntrenamiento)
        prueba = self.data.tail(self.tamanioPrueba)
        self.pos_target = self.data.columns.get_loc(self.target)

        suma_errores = 0.0
        knn = KNN(entrenamiento, self.target)
        for i in prueba.values:
            prediccion = knn.get_prediccion(np.delete(i, self.pos_target))[0]
            real = i[self.pos_target] # valor real del conjunto de prueba
            suma_errores += ((real - prediccion)**2)

        return suma_errores / len(prueba)

# Obtenemos todas las clases
# Recorremos esa lista de clases
# recorremos la lista de diccionario
# Inicializamos una variable de diccionario

# Recorremos el diccionario en busca del target 
# que se esta iterando

# Cuando la clave coincida con target, tendremos 
# el valor

# 



















    def procesoCompletoNaiveBayesConPrint(self, arrayOrden):
        # Inicializamos las dos matrices
        dataMatrizConfusionEntrenamiento = self.crearMatrizConfusion(arrayOrden)
        dataMatrizConfusionPrueba = self.crearMatrizConfusion(arrayOrden)

        # Creamos un dataset random
        #print("Dataset sin random")
        #print(self.data)
        #print()
        auxData = self.data.sample(frac=1)
        #print("Dataset con random")
        #print(auxData)
        #print()
        self.nuevoDataframe(auxData)
        #print("Dataset cambiado con random")
        #print(self.data)
        #print()

        # Inicializamos los arreglos de los resultados obtenidos
        resultadoEntrenamiento = []
        resultadoPrueba = []

        # Inicializamos los arreglos de los resultados reales del dataframe
        realEntrenamiento = []
        realPrueba = []
        
        # Inicializamos los arreglos de los resultados obtenidos
        resultadoEntrenamiento, resultadoPrueba, realEntrenamiento, realPrueba = self.resultadoModeloNaive()

        """
        print(auxData)
        print("Resultado")
        print(resultadoEntrenamiento)
        print(resultadoPrueba)
        print("Real")
        print(realEntrenamiento)
        print(realPrueba)
        """

        # Creamos las repeticiones de cada clase

        diccionarioEntrenamiento = {}
        diccionarioPrueba = {}
        

        diccionarioEntrenamiento = self.obtenerNumerosMatriz(resultadoEntrenamiento, realEntrenamiento)
        diccionarioPrueba = self.obtenerNumerosMatriz(resultadoPrueba, realPrueba)
        
        """
        print()
        print("Diccionario Entrenamiento")
        print(json.dumps(diccionarioEntrenamiento, indent=2))
        print()
        print("Diccionario Prueba")
        print(json.dumps(diccionarioPrueba, indent=2))
        print()
        print()
        """
        
        dataMatrizConfusionEntrenamiento = self.crearMatrizConfusion(arrayOrden)
        dataMatrizConfusionPrueba = self.crearMatrizConfusion(arrayOrden)

        
        matrizConfusionEntrenamientoValores = self.llenarMatrizConfusion(dataMatrizConfusionEntrenamiento, diccionarioEntrenamiento)
        print("Matriz de Confusion: Entrenamiento")
        print(matrizConfusionEntrenamientoValores)
        print()
        matrizConfusionPruebaValores = self.llenarMatrizConfusion(dataMatrizConfusionPrueba, diccionarioPrueba)
        print("Matriz de Confusion: Prueba")
        print(matrizConfusionPruebaValores)
        print()
        

        # bandera en 0 = Entrenamiento
        # bandera en 1 = Prueba
        exactitudEntrenamiento = self.obtenerExactitud(matrizConfusionEntrenamientoValores)

        print("Exactitud de Entrenamiento")
        print(exactitudEntrenamiento)
        print()

        exactitudPrueba = self.obtenerExactitud(matrizConfusionPruebaValores)

        print("Exactitud de Prueba")
        print(exactitudPrueba)
        print()

        # Recall = 0
        # Precisión = 1
        entrenamientoDicRecalls = self.obtenerRecalls_Precisiones(matrizConfusionEntrenamientoValores, 0)
        print()
        print(json.dumps(entrenamientoDicRecalls, indent=2))
        print()

        pruebaDicRecalls = self.obtenerRecalls_Precisiones(matrizConfusionPruebaValores, 0)
        print()
        print(json.dumps(pruebaDicRecalls, indent=2))
        print()

        entrenamientoDicPrecision = self.obtenerRecalls_Precisiones(matrizConfusionEntrenamientoValores, 1)
        print()
        print(json.dumps(entrenamientoDicPrecision, indent=2))
        print()

        pruebaDicPrecision = self.obtenerRecalls_Precisiones(matrizConfusionPruebaValores, 1)
        print()
        print(json.dumps(pruebaDicPrecision, indent=2))
        print()
        print()

        promedioExactitud = self.promediar(exactitudEntrenamiento, exactitudPrueba)
        promedioRecall = self.promediarConDiccionario(entrenamientoDicRecalls, pruebaDicRecalls)
        promedioPrecision = self.promediarConDiccionario(entrenamientoDicPrecision, pruebaDicPrecision)
        
        print("Exactitud Promedio:", promedioExactitud)
        print("Recall Promedio")
        print(json.dumps(promedioRecall, indent=2))
        print("Precision Promedio")
        print(json.dumps(promedioPrecision, indent=2))
        print()

    
            

