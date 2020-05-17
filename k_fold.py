import numpy as np
import pandas
from algoritmos.knn import KNN
from algoritmos.naive import NaiveBayes
import algoritmos.one_r

class KFoldCrossValidation:

    def __init__(self, data, target, k, algoritmo, positivo=None, negativo=None):
        self.data = data.sample(frac=1) # mezcla los datos
        self.target = target
        self.k = k
        self.algoritmo = algoritmo
        self.positivo = positivo
        self.negativo = negativo

        self.es_regresion = False
        if np.issubdtype(self.data[self.target].dtype, np.number):
            self.es_regresion = True
            if algoritmo == "One R" or algoritmo == "Naive Bayes":
                raise ValueError("Solo KNN funciona con problemas de regresion")

        self.pos_target = self.data.columns.get_loc(self.target)
        self.unicos_target = self.data[self.target].unique()

        # comprueba si el target tiene 2 posibles valores o más
        if len(self.unicos_target) == 2:
            self.es_multi_clase = False
        else:
            self.es_multi_clase = True

    def iniciar_validacion(self):
        if self.es_regresion:
            return self.validacion_regresion_knn()
        if self.es_multi_clase:
            return self.validation_multi_clases()
        else:
            return self.validation_dos_clases()
            
    def _funcion_validacion(self):
        """ Dependiendo del algoritmo, retorna la función a usar para la validación """
        if self.algoritmo == "KNN":
            funcion_validacion = self.validationKNN
        elif self.algoritmo == "Naive Bayes":
            funcion_validacion = self.validationNaiveBayes
        else:
            funcion_validacion = self.validationOneR

        return funcion_validacion

    def validation_dos_clases(self):
        """ Método para validar cuando los posibles valores de la clase son dos """

        # divide el DataFrame en k folds
        data_split = np.array_split(self.data, self.k)

        columnas = ["Exactitud", "Sensibilidad", "Especificidad"]
        tabla = pandas.DataFrame(columns=columnas)
        tabla_algoritmo = pandas.DataFrame(columns=columnas)

        funcion_validacion = self._funcion_validacion()

        for i in range(self.k):
            probar = data_split[i]
            entrenar = pandas.concat(data_split[:i] + data_split[i+1:])
            tabla_algoritmo.loc[i] = funcion_validacion(entrenar, probar)

        # saca promedio
        tabla.loc[self.algoritmo] = tabla_algoritmo.mean(skipna=False).round(4)

        return tabla


    def validation_multi_clases(self):
        # divide el dataset en k conjuntos
        data_split = np.array_split(self.data, self.k)

        columnas = ["Precisión", "Sensibilidad"]
        tabla = pandas.DataFrame(0, columns=columnas, index=self.unicos_target)
        exactitud_final = 0.0

        funcion_validacion = self._funcion_validacion()

        for i in range(self.k):
            probar = data_split[i] # datos de prueba
            entrenar = pandas.concat(data_split[:i] + data_split[i+1:]) # datos de entrenamiento

            matriz, exactitud = funcion_validacion(entrenar, probar)
            exactitud_final += exactitud
            tabla += matriz

        tabla /= self.k # saca promedio
        exactitud_final /= self.k # exactiud promedio final

        return tabla, round(exactitud_final, 4)


    def validationKNN(self, entrenamiento, prueba):
        matriz = pandas.DataFrame(0, columns=self.unicos_target, index=self.unicos_target)

        suma_errores = 0.0
        knn = KNN(entrenamiento, self.target)
        for i in prueba.values:
            prediccion = knn.get_prediccion(np.delete(i, self.pos_target))[0]
            real = i[self.pos_target] # valor real del conjunto de prueba
            if self.es_regresion:
                suma_errores += ((real - prediccion)**2)
            else:
                matriz[prediccion][real] += 1

        if self.es_regresion:
            return suma_errores / len(prueba) # error cuadrático médio
        else:
            return self._procesar_matriz(matriz)  

    def validationNaiveBayes(self, entrenamiento, prueba):
        matriz = pandas.DataFrame(0, columns=self.unicos_target, index=self.unicos_target)

        naive_bayes = NaiveBayes(entrenamiento, self.target)
        for i, row in prueba.iterrows():
            prediccion = naive_bayes.get_prediccion(row.drop(self.target))[0]
            prediccion = max(prediccion, key=prediccion.get)
            real = row[self.target] # valor real del conjunto de prueba
            matriz[prediccion][real] += 1

        return self._procesar_matriz(matriz)

    def validationOneR(self, entrenamiento, prueba):
        matriz = pandas.DataFrame(0, columns=self.unicos_target, index=self.unicos_target)

        frecuencias = algoritmos.one_r.generar_frecuencias(entrenamiento, self.target)
        reglas = algoritmos.one_r.generar_reglas(frecuencias)
        menor = algoritmos.one_r.encontrar_error_menor(reglas)
        
        for i, row in prueba.iterrows():
            val = row[menor]
            try: # puede darse el caso de que una llave no exista. ¿qué se debe hacer?
                prediccion = reglas[menor]["regla"][val][0]
                real = row[self.target] # valor real del conjunto de prueba
                matriz[prediccion][real] += 1
            except Exception as e:
                pass

        return self._procesar_matriz(matriz)


    def _procesar_matriz(self, matriz):
        """ Dependiendo de si es multiclase o no es procesa la matriz """

        # (suma de la diagonal) / (suma de toda la matriz)
        exactitud = np.trace(matriz) / matriz.sum().sum()

        if not self.es_multi_clase: # si no es multiclase
            try:
                sensibilidad = int(matriz[self.positivo][self.positivo]) / int(matriz[self.positivo].sum())
            except ZeroDivisionError:
                sensibilidad = 0

            try:
                especificidad = int(matriz[self.negativo][self.negativo]) / int(matriz[self.negativo].sum())
            except ZeroDivisionError:
                especificidad = 0

            print(exactitud, sensibilidad, especificidad)
            return [exactitud, sensibilidad, especificidad]

        else: # si es multiclase
            tabla = pandas.DataFrame(columns=["Precisión", "Sensibilidad"],
                index=self.unicos_target)

            # para cada posible valor del target calcula la precision y sensibilidad
            for i in matriz.index:
                precision = matriz[i][i] / matriz.loc[i].sum() # fila
                sensibilidad = matriz[i][i] / matriz[i].sum() # columna
                tabla.loc[i] = [precision, sensibilidad]

            return tabla, exactitud

    def validacion_regresion_knn(self):
        # divide el DataFrame en k folds
        data_split = np.array_split(self.data, self.k)
        tabla = pandas.DataFrame(columns=["Error cuadrático medio"], index=["KNN"])

        suma_errores_cuadraticos = 0.0
        for i in range(self.k):
            probar = data_split[i]
            entrenar = pandas.concat(data_split[:i] + data_split[i+1:])
            suma_errores_cuadraticos += self.validationKNN(entrenar, probar)
            print(suma_errores_cuadraticos)

        # saca promedio
        tabla.loc["KNN"] = round(suma_errores_cuadraticos / self.k, 4)

        return tabla


        
"""
data = pandas.read_csv("algoritmos/iris_columnas.csv", skipinitialspace=True)
target = "sepal length"

fold = KFoldCrossValidation(data, target, 10, "KNN")
print(fold.validacion_regresion_knn())
"""
