import pandas
import math
import numpy as np

class KNN:

    def __init__(self, data, target, k = 5):
        self.data = data
        self.k = k
        self.target = target

    def set_k(self, k):
        self.k = k

    def _distancia_entre_numericos(self, lista1, lista2): # Utilizamos la distancia Euclidiana
        """ Calcula la distancia entre dos listas numericas """
        distancia = 0.0
        for val1, val2 in zip(lista1, lista2):
            distancia += math.pow((val1 - val2), 2)

        return math.sqrt(distancia)

    def _distancia_entre_categoricos(self, lista1, lista2): # Utilizamos la distancia de Hamming
        """ Calcula la distancia entre dos listas categoricas """
        distancia = 0
        for val1, val2 in zip(lista1, lista2):
            if val1 != val2:
                distancia += 1

        return distancia

    def _generar_distancias(self, fila, tipo):
        """ Genera la tabla de distancias entre la fila dada y cada una de las filas del DataFrame """
        if tipo == "numerico":
            funcion_distancia = self._distancia_entre_numericos
        else:
            funcion_distancia = self._distancia_entre_categoricos

        pos_target = self.data.columns.get_loc(self.target)

        distancias = self.data.copy() # hace una copia independiente del DataFrame
        distancias["distancia"] = distancias.apply(lambda row: funcion_distancia(fila, np.delete(row.values, pos_target)), axis=1) # Itera sobre cada fila del dataframe

        return distancias
        

    def get_prediccion(self, fila):

        if np.issubdtype(pandas.Series(fila).dtype, np.number):
            tipo = "numerico"
        else:
            tipo = "categorico"


        distancias = self._generar_distancias(fila, tipo)

        distancias.sort_values("distancia", inplace=True) # ordena de menor a mayor

        # si el target es númerico
        if np.issubdtype(self.data[self.target], np.number):
            resultado = distancias[:self.k][self.target].mean() # retorna el promedio
        else: # si el target es categorico
            resultado = distancias[:self.k][self.target].mode()[0] # retorna el valor mas frecuenta del target (CLASIFICACIÓN)

        return resultado, distancias[:self.k]
