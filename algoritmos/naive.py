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

    def calcular_frecuencias_target(self):
        """ Genera la tabla de frecuencias del atributo target"""
        """
        frecuencias = {}
        for val in self.data[self.target].unique():
            frec = len(self.data[(self.data[self.target] == val)])
            frecuencias[val] = frec

        return frecuencias
        """

        frecuencias = pandas.DataFrame(columns=["frecuencia", "probabilidad"],
            index=self.data[self.target].unique())
        num_filas = len(self.data)

        for i in frecuencias.index:
            frec = len(self.data[(self.data[self.target] == i)])
            frecuencias["frecuencia"][i] = frec
            frecuencias["probabilidad"][i] = frec / num_filas

        return frecuencias

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
            if np.issubdtype(self.data[atributo].dtype, np.number): # si es numérico
                probabilidades[atributo] = pandas.DataFrame(columns=["media", "desviacion"],
                                                            index=self.frecuencias[atributo].columns)
                for i in self.frecuencias[atributo].columns:
                    probabilidades[atributo].at[i, "media"] = self.frecuencias[atributo].at[0, i].mean()
                    probabilidades[atributo].at[i, "desviacion"] = self.frecuencias[atributo].at[0, i].std(ddof=1)

            else:
                probabilidades[atributo] = self.frecuencias[atributo].apply(lambda row: self.procesar(row), axis=1)

        return probabilidades


    def _generar_frecuencias(self, sumar=0):
        """ Genera la tabla de frecuencias """
        frecuencias = {}

        for atributo in self.data.columns:
            if atributo == self.target: # el target se debe omitir
                continue

            if np.issubdtype(self.data[atributo].dtype, np.number): # si el atributo es numérico
                frecuencias[atributo] = pandas.DataFrame(columns=self.data[self.target].unique())
                for i in self.data[self.target].unique():
                    frecuencias[atributo].at[0, i] = np.array(self.data[self.data[self.target] == i][atributo])
            else:
                frecuencias[atributo] = pandas.crosstab(columns=self.data[atributo].astype(str),
                        index=self.data[self.target].astype(str))

                if sumar != 0:
                    frecuencias[atributo] = frecuencias[atributo].apply(lambda x: x + sumar, axis=1)

        """
        if sumar != 0:
            for atributo in frecuencias:
                frecuencias[atributo] = frecuencias[atributo].apply(lambda x: x + sumar, axis=1)

        """

        return frecuencias


    def get_prediccion(self, instancia):
        """ Retorna un diccionario con las probabilidades del target para la fila dada """

        #total_valores_target = sum(self.frec_target.values())

        resultado = {}
        procedimiento_str = ""
        for i in self.frec_target.index:
            procedimiento_str += "Probabilidad de {}\n".format(i)
            probabilidad_total = 1.0
            for atributo, val in instancia.items():

                prob = 0
                if np.issubdtype(self.data[atributo].dtype, np.number):
                    media = self.probabilidades[atributo]["media"][i]
                    desviacion = self.probabilidades[atributo]["desviacion"][i]
                    prob = self._distribucion_normal(val, media, desviacion)
                else:
                    prob = self.probabilidades[atributo][val][i]

                #print(prob, end=" * ")
                procedimiento_str += "{} * ".format(prob)
                probabilidad_total *= prob

            
            prob_target = self.frec_target["probabilidad"][i]
            #print(prob_target, end=" = ")
            procedimiento_str += "{} = ".format(prob_target)
            probabilidad_total *= prob_target
            #print(probabilidad_total, "\n")
            procedimiento_str += "{}\n\n".format(probabilidad_total)
            
            resultado[i] = probabilidad_total

        #Normalización
        procedimiento_str += "\nNormalización\n"
        suma = sum(resultado.values())

        for val in resultado:
            #print(val, end=", ")
            procedimiento_str += "{},  ".format(val)
            normalizado = resultado[val] / suma
            #print(resultado[val], "/", suma, " = ", normalizado)
            procedimiento_str += "{} / {} = {}\n".format(resultado[val], suma, normalizado)
            resultado[val] = normalizado
        

        return resultado, procedimiento_str

"""
data = pandas.read_csv("iris_columnas.csv", skipinitialspace=True)
target = "sepal length"

naive_bayes = NaiveBayes(data, target)

print("FRECUENCIAS\n")
for key, val in naive_bayes.frecuencias.items():
    print(key, "\n", val, "\n")
print("-------------------------------------------------------------\n")

print("FRECUENCIAS DEL TARGET\n")
print(naive_bayes.frec_target)
print("-------------------------------------------------------------\n")

print("VEROSIMILITUDES\n")
for key, val in naive_bayes.probabilidades.items():
    print(key, "\n", val, "\n")
print("-------------------------------------------------------------\n")
"""

# ----------------------------------------------------------------------------------------

"""
data = pandas.read_csv("iris_columnas.csv", skipinitialspace=True)
target = "class"

naive_bayes = NaiveBayes(data, target)

print(naive_bayes.frecuencias)
print(naive_bayes.frec_target)
print(naive_bayes.frecuencias.update(naive_bayes.frec_target))

#frecuencias = generar_frecuencias_pandas(data, target, sumar=0)
#frec_target = calcular_frecuencias_target(data, target)
#probabilidades = calcular_probabilidades_pandas(frecuencias)

print("FRECUENCIAS\n")
for key, val in naive_bayes.frecuencias.items():
    print(key, "\n", val, "\n")
print("-------------------------------------------------------------\n")

print("FRECUENCIAS DEL TARGET\n")
print(naive_bayes.frec_target)
print("-------------------------------------------------------------\n")

print("VEROSIMILITUDES\n")
for key, val in naive_bayes.probabilidades.items():
    print(key, "\n", val, "\n")
print("-------------------------------------------------------------\n")

#print(naive_bayes.predecir({"City": "Dallas", "Gender": "Female", "Income": 100000}))

fila = {"sepal length": 5.5, "sepal width":2.6, "petal length":4.4, "petal width": 1.2}

resultado, procedimiento = naive_bayes.predecir(fila)
print("Probabilidad final por clase")
print(resultado)

print("\nLa clase mas probables es:", max(resultado, key=resultado.get))

"""
"""

#fila = {"Outlook": "Sunny", "Temp": "Cool", "Humidity": "High", "Windy": "True"}
#fila = {"Compra": "vhigh", "Mantenimiento": "med", "Puertas": "2","Personas": "more"}
fila = {"City": "Dallas", "Gender": "Female"}

print("Instancia probada")
print(fila, "\n")

resultado = naive_bayes(fila, probabilidades, frec_target)
print("Probabilidad final por clase")
print(resultado)

print("\nLa clase mas probables es:", max(resultado, key=resultado.get))
"""