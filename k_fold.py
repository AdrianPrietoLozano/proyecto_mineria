import numpy as np
import pandas
from algoritmos.knn import KNN
from algoritmos.naive import NaiveBayes
import algoritmos.one_r

class KFoldCrossValidation:

    def __init__(self, data, target, k=2, positivo=None, negativo=None):
        self.data = data.sample(frac=1) # mezcla los datos
        self.target = target
        self.k = k
        self.positivo = positivo
        self.negativo = negativo

        self.pos_target = self.data.columns.get_loc(self.target)
        self.unicos_target = self.data[self.target].unique()

        # comprueba si el target tiene 2 posibles valores o más
        if len(self.unicos_target) == 2:
            self.es_multi_clase = False
        else:
            self.es_multi_clase = True

    def setK(self, k):
        self.k = k

    def setValorPositivo(self, valor):
        self.positivo = valor

    def setValorNegativo(self, valor):
        self.negativo = valor

    def iniciar_validacion(self):
        if self.es_multi_clase:
            return self.validation_multi_clases()
        else:
            return self.validation_dos_clases()
            

    def validation_dos_clases(self):
        """ Método para validar cuando los posibles valores de la clase son dos """

        # divide el DataFrame en k folds
        data_split = np.array_split(self.data, self.k)

        columnas = ["Exactitud", "Sensibilidad", "Especificidad"]
        tabla = pandas.DataFrame(columns=columnas,
                                index=["KNN", "Naive Bayes", "One-R"])

        tabla_naive = pandas.DataFrame(columns=columnas)
        tabla_knn = pandas.DataFrame(columns=columnas)
        tabla_one = pandas.DataFrame(columns=columnas)

        for i in range(self.k):
            probar = data_split[i]
            entrenar = pandas.concat(data_split[:i] + data_split[i+1:])

            tabla_naive.loc[i] = self.validationNaiveBayes(entrenar, probar)
            tabla_knn.loc[i] = self.validationKNN(entrenar, probar)
            tabla_one.loc[i] = self.validationOneR(entrenar, probar)

        tabla.loc["KNN"] = tabla_knn.mean().round(4)
        tabla.loc["Naive Bayes"] = tabla_naive.mean().round(4)
        tabla.loc["One-R"] = tabla_one.mean().round(4)

        return tabla


    def validation_multi_clases(self):
        data_split = np.array_split(self.data, self.k)

        columnas = ["Precision", "Sensibilidad"]
        tablas = {
            "Naive Bayes": pandas.DataFrame(0, columns=columnas, index=self.unicos_target),
            "KNN": pandas.DataFrame(0, columns=columnas, index=self.unicos_target),
            "One-R": pandas.DataFrame(0, columns=columnas, index=self.unicos_target)
        }

        # exactitudes promedio por algoritmo
        exactitudes = {
            "Naive Bayes": 0.0,
            "KNN": 0.0,
            "One-R": 0.0
        }

        for i in range(self.k):
            probar = data_split[i]
            entrenar = pandas.concat(data_split[:i] + data_split[i+1:])

            matriz, exactitud = self.validationNaiveBayes(entrenar, probar)
            exactitudes["Naive Bayes"] += exactitud
            tablas["Naive Bayes"] += matriz

            matriz, exactitud = self.validationKNN(entrenar, probar)
            exactitudes["KNN"] += exactitud
            tablas["KNN"] += matriz

            matriz, exactitud = self.validationOneR(entrenar, probar)
            exactitudes["One-R"] += exactitud
            tablas["One-R"] += matriz

        # calcula promedio de cada tabla de cada algoritmo
        for tabla in tablas.values():
            tabla /= self.k

        # calcula exactitud promedio de cada algoritmo
        for i in exactitudes:
            exactitudes[i] /= self.k

        return tablas, exactitudes


    def validationKNN(self, entrenamiento, prueba):
        matriz = pandas.DataFrame(0, columns=self.unicos_target, index=self.unicos_target)

        knn = KNN(entrenamiento, self.target)
        for i in prueba.values:
            prediccion = knn.get_prediccion(np.delete(i, self.pos_target))[0]
            real = i[self.pos_target] # valor real del conjunto de prueba
            matriz[prediccion][real] += 1

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
            except:
                pass

        return self._procesar_matriz(matriz)


    def _procesar_matriz(self, matriz):
        """ Dependiendo de si es multiclase o no es procesa la matriz """

        # (suma de la diagonal) / (suma de toda la matriz)
        exactitud = np.trace(matriz) / matriz.sum().sum()

        if not self.es_multi_clase: # si no es multiclase
            sensibilidad = matriz[self.positivo][self.positivo] / matriz[self.positivo].sum()
            especificidad = matriz[self.negativo][self.negativo] / matriz[self.negativo].sum()

            return [exactitud, sensibilidad, especificidad]

        else: # si es multiclase
            tabla = pandas.DataFrame(columns=["Precision", "Sensibilidad"],
                index=self.unicos_target)

            # para cada posible valor del target calcula la precision y sensibilidad
            for i in matriz.index:
                precision = matriz[i][i] / matriz.loc[i].sum() # fila
                sensibilidad = matriz[i][i] / matriz[i].sum() # columna
                tabla.loc[i] = [precision, sensibilidad]

            return tabla, exactitud


        
"""
data = pandas.read_csv("randomOneRKnn.csv", skipinitialspace=True)
target = "Sail"

print("inicio")
fold = KFoldCrossValidation(data, target, 2, "yes", "no")
print(fold.iniciar_validacion())
"""