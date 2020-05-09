import numpy as np
import pandas
from knn import KNN
from naive import NaiveBayes
import one_r

class KFoldCrossValidation:

    def __init__(self, data, target, k=2):
        self.data = data.sample(frac=1) # mezcla los datos
        self.target = target
        self.k = k
        self.pos_target = self.data.columns.get_loc(self.target)

    def setK(self, k):
        self.k = k

    def validation(self):
        data_split = np.array_split(self.data, self.k)
        unique_target = self.data[self.target].unique()

        columnas = ["Exactitud", "Sensibilidad", "Especificidad"]
        tabla = pandas.DataFrame(columns=columnas,
                                index=["KNN", "Naive Bayes", "One-R"])

        tabla_naive = pandas.DataFrame(columns=columnas)
        tabla_knn = pandas.DataFrame(columns=columnas)
        tabla_one = pandas.DataFrame(columns=columnas)

        for i in range(self.k):
            probar = data_split[i]
            entrenar = pandas.concat(data_split[:i] + data_split[i+1:])

            tabla_naive.loc[i] = self.validationNaiveBayes(entrenar, probar, unique_target)
            tabla_knn.loc[i] = self.validationKNN(entrenar, probar, unique_target)
            tabla_one.loc[i] = self.validationOneR(entrenar, probar, unique_target)

        tabla.loc["KNN"] = tabla_knn.mean().round(4)
        tabla.loc["Naive Bayes"] = tabla_naive.mean().round(4)
        tabla.loc["One-R"] = tabla_one.mean().round(4)

        return tabla



    def validationKNN(self, entrenamiento, prueba, unicos_target):
        matriz = pandas.DataFrame(0, columns=unicos_target, index=unicos_target)

        knn = KNN(entrenamiento, self.target)
        for i in prueba.values:
            prediccion = knn.get_prediccion(np.delete(i, self.pos_target))[0]
            real = i[self.pos_target]
            matriz[prediccion][real] += 1

        exactitud = np.trace(matriz) / matriz.sum().sum()

        # ESTO DEBE CAMBIARSE YA QUE SOLO FUNCIONA CUANDO EL TARGET TIENE DOS VALORES ÚNICOS
        sensibilidad = matriz.iloc[0, 0] / matriz.iloc[:, 0].sum()
        especificidad = matriz.iloc[1, 1] / matriz.iloc[:, 1].sum()

        return [exactitud, sensibilidad, especificidad]
            

    def validationNaiveBayes(self, entrenamiento, prueba, unicos_target):
        matriz = pandas.DataFrame(0, columns=unicos_target, index=unicos_target)

        naive_bayes = NaiveBayes(entrenamiento, self.target)
        for i, row in prueba.iterrows():
            prediccion = naive_bayes.get_prediccion(row.drop(self.target))[0]
            prediccion = max(prediccion, key=prediccion.get)
            real = row[self.target]
            matriz[prediccion][real] += 1
        
        exactitud = np.trace(matriz) / matriz.sum().sum()
        # ESTO DEBE CAMBIARSE YA QUE SOLO FUNCIONA CUANDO EL TARGET TIENE DOS VALORES ÚNICOS
        sensibilidad = matriz.iloc[0, 0] / matriz.iloc[:, 0].sum()
        especificidad = matriz.iloc[1, 1] / matriz.iloc[:, 1].sum()

        return [exactitud, sensibilidad, especificidad]

    def validationOneR(self, entrenamiento, prueba, unicos_target):
        matriz = pandas.DataFrame(0, columns=unicos_target, index=unicos_target)

        frecuencias = one_r.generar_frecuencias(entrenamiento, self.target)
        reglas = one_r.generar_reglas(frecuencias)
        menor = one_r.encontrar_error_menor(reglas)
        
        for i, row in prueba.iterrows():
            val = row[menor]
            try: # puede darse el caso de que una llave no exista. ¿qué se debe hacer?
                prediccion = reglas[menor]["regla"][val][0]
                real = row[self.target]
                matriz[prediccion][real] += 1
            except:
                pass

        exactitud = np.trace(matriz) / matriz.sum().sum()
        # ESTO DEBE CAMBIARSE YA QUE SOLO FUNCIONA CUANDO EL TARGET TIENE DOS VALORES ÚNICOS
        sensibilidad = matriz.iloc[0, 0] / matriz.iloc[:, 0].sum()
        especificidad = matriz.iloc[1, 1] / matriz.iloc[:, 1].sum()

        return [exactitud, sensibilidad, especificidad]
        


"""
data = pandas.read_csv("iris_columnas.csv", skipinitialspace=True)
target = "class"

print("inicio")
fold = KFoldCrossValidation(data, target, 2)
fold.validation()
"""