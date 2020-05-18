import pandas
import numpy as np
import math


class NaiveBayes:

    def __init__(self, data, target):
        self.data = data
        self.target = target
        self.frecuencias = self._generar_frecuencias(sumar=1)
        self.frec_target = self.calcular_frecuencias_target()
        self.probabilidades = self._calcular_probabilidades()

    # Lo que hace One R y saca las frecuencias del target y sus probabilidades
    def calcular_frecuencias_target(self):

        frecuencias = pandas.DataFrame(columns=["frecuencia", "probabilidad"],
            index=self.data[self.target].unique())
        num_filas = len(self.data)

        for i in frecuencias.index:
            frec = len(self.data[(self.data[self.target] == i)])
            frecuencias["frecuencia"][i] = frec
            frecuencias["probabilidad"][i] = frec / num_filas

        return frecuencias

    # Calcular la distribución normal
    def _distribucion_normal(self, x, media, desviacion):

        resultado = 1 / (math.sqrt(2 * math.pi) * desviacion)
        exponente = -( (x - media)**2 / (desviacion**2 * 2) )
        resultado *= pow(math.e, exponente)

        return resultado


    def procesar(self, row):
        """ Dada una fila calcula la probabilidad de cada uno de los valores """
        suma = row.sum()

        return row.apply(lambda x: x / suma)
        


    def _calcular_probabilidades(self):
        """ Genera las tablas de verosimilitudes """
        probabilidades = {}

        for atributo in self.frecuencias:
            # Se calcula la media y la desviación estandar
            if np.issubdtype(self.data[atributo].dtype, np.number): # si es numérico
                probabilidades[atributo] = pandas.DataFrame(columns=["media", "desviacion"],
                                                            index=self.frecuencias[atributo].columns)
                for i in self.frecuencias[atributo].columns:
                    probabilidades[atributo].at[i, "media"] = self.frecuencias[atributo].at[0, i].mean() # Media
                    probabilidades[atributo].at[i, "desviacion"] = self.frecuencias[atributo].at[0, i].std(ddof=1) # Desviación

            else:
                probabilidades[atributo] = self.frecuencias[atributo].apply(lambda row: self.procesar(row), axis=1) # Devuelve la tabla de probabilidades / verosimilitudes

        return probabilidades


    def _generar_frecuencias(self, sumar=0):
        """ Genera la tabla de frecuencias """
        frecuencias = {}

        for atributo in self.data.columns:
            if atributo == self.target: # el target se debe omitir
                continue
            
            # Se obtiene una lista de los valores numericos
            if np.issubdtype(self.data[atributo].dtype, np.number): # si el atributo es numérico
                frecuencias[atributo] = pandas.DataFrame(columns=self.data[self.target].unique())
                for i in self.data[self.target].unique():
                    frecuencias[atributo].at[0, i] = np.array(self.data[self.data[self.target] == i][atributo])
            
            # Se obtiene una tabla de frecuencias
            else:
                frecuencias[atributo] = pandas.crosstab(columns=self.data[atributo].astype(str),
                        index=self.data[self.target].astype(str))

                if sumar != 0:
                    frecuencias[atributo] = frecuencias[atributo].apply(lambda x: x + sumar, axis=1)

        return frecuencias


    def get_prediccion(self, instancia):
        """ Retorna un diccionario con las probabilidades del target para la fila dada """

        resultado = {}
        procedimiento_str = ""
        for i in self.frec_target.index:
            procedimiento_str += "Probabilidad de {}\n".format(i)
            probabilidad_total = 1.0
            for atributo, val in instancia.items():

                prob = 0
                try:
                    if np.issubdtype(self.data[atributo].dtype, np.number):
                        media = self.probabilidades[atributo]["media"][i]
                        desviacion = self.probabilidades[atributo]["desviacion"][i]
                        prob = self._distribucion_normal(val, media, desviacion) # Se calcula la distribución normal
                    else:
                        prob = self.probabilidades[atributo][val][i]
                except Exception as e:
                    prob = 0.0001
                
                procedimiento_str += "{} * ".format(prob)
                probabilidad_total *= prob

            
            prob_target = self.frec_target["probabilidad"][i]
            procedimiento_str += "{} = ".format(prob_target)
            probabilidad_total *= prob_target
            procedimiento_str += "{}\n\n".format(probabilidad_total)
            
            resultado[i] = probabilidad_total

        #Normalización
        procedimiento_str += "\nNormalización\n"
        suma = sum(resultado.values())

        for val in resultado:
            procedimiento_str += "{},  ".format(val)
            normalizado = resultado[val] / suma
            procedimiento_str += "{} / {} = {}\n".format(resultado[val], suma, normalizado)
            resultado[val] = normalizado
        

        return resultado, procedimiento_str
