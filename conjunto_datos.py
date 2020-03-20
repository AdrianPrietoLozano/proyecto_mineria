import json
from atributo_numerico import AtributoNumerico
from atributo_categorico import AtributoCategorico
import pandas as pd
import math


class ConjuntoDatos:

    SIMBOLO_FALTANTE = "?"  # por default será ?
    TARGET = None

    def __init__(self, archivo_propiedades, conexion=None, query=None):
        self.archivo_propiedades = archivo_propiedades
        self.conexion = conexion
        self.query = query
        self.panda = None
        self.data = {} # aquí se guarda todo el archivo .json como un diccionario
        self.atributos = {}

        if self.conexion:
            self.__cargar_propiedades_desde_BD()
        else:
            self.__cargar_propiedades()

        ConjuntoDatos.SIMBOLO_FALTANTE = self.data["simbolo_faltante"]
        ConjuntoDatos.TARGET = self.data["target"]

    def __cargar_propiedades(self):
        with open(self.archivo_propiedades) as contenido:
            self.data = json.load(contenido) # combierte el .json a un diccionario

            if self.conexion != None and self.query != None:
                self.panda = pd.read_sql_query(self.query, self.conexion)
                pass
            else: # leer normalmente desde un un csv
                self.panda = pd.read_csv(self.getPathCsv(), skipinitialspace=True,
                    names=[c["nombre"] for c in self.data["atributos"]])

            # crea un diccionario de atributos, la llave es el nombre del atributo
            # y el valor una instancia de la clase AtributoNumerico o AtributCategorico 
            for atributo in self.data["atributos"]:
                tipo_atributo = atributo.get("tipo", None)

                if tipo_atributo == "numerico":
                    self.atributos[atributo["nombre"]] = AtributoNumerico(self.panda, self.atributos, atributo)
                else:
                    atributo["tipo"] = "categorico" # en caso de que no este definido el tipo entonces por defecto se define como categorico
                    self.atributos[atributo["nombre"]] = AtributoCategorico(self.panda, self.atributos, atributo)

            contenido.close()


    def __cargar_propiedades_desde_BD(self):
        with open(self.archivo_propiedades) as contenido:
            self.data = json.load(contenido) # combierte el .json a un diccionario
            self.data["atributos"] = []

            if self.conexion != None and self.query != None:
                self.panda = pd.read_sql_query(self.query, self.conexion)

                # crea un diccionario de atributos, la llave es el nombre del atributo
                # y el valor una instancia de la clase AtributoNumerico o AtributCategorico 
                for columna in self.panda.columns:
                    tipo = self.panda[columna].dtype
                    if tipo == "int64" or tipo == "float64":
                        atributo = {"nombre": columna, "tipo": "numerico", "dominio":""}
                        self.atributos[columna] = AtributoNumerico(self.panda, self.atributos, atributo)
                    else:
                        atributo = {"nombre": columna, "tipo": "categorico", "dominio":""}
                        self.atributos[columna] = AtributoCategorico(self.panda, self.atributos, atributo)

                    self.data["atributos"].append(atributo)

            contenido.close()

        self.conexion.close()

    def agregarAtributo(self, nombre, tipo, dominio):
        """Agrega un nuevo atributo al archivo de propiedades"""
        atributo = {"nombre": nombre, "tipo": tipo, "dominio": dominio}
        self.data["atributos"].append(atributo)

        if tipo == "numerico":
            self.atributos[nombre] = AtributoNumerico(self.panda, self.atributos, atributo)
        else:
            self.atributos[nombre] = AtributoCategorico(self.panda, self.atributos, atributo)


    def getPathCsv(self):
        return self.data.get("path_csv", None)

    def getTarget(self):
        return self.data.get("target", None)

    def setTarget(self, target):
        self.data["target"] = target
        ConjuntoDatos.TARGET = target

    def getSimboloFaltante(self):
        return self.data.get("simbolo_faltante", None)

    def setSimboloFaltante(self, simbolo):
        self.data["simbolo_faltante"] = simbolo
        ConjuntoDatos.SIMBOLO_FALTANTE = simbolo

    def getRuta(self):
        return self.data.get("ruta", None)

    def setRuta(self, ruta):
        self.data["ruta"] = ruta

    def setDescripcion(self, descripcion):
        self.data["descripcion"] = descripcion

    def getDescripcion(self):
        return self.data.get("descripcion", None)

    def getAtributo(self, nombre):
        return self.atributos.get(nombre, None)

    def getAtributos(self):
        return self.atributos.values()

    def getNombresAtributos(self):
        return list(self.atributos.keys())

    def getNumAtributos(self):
        return len(self.atributos)

    def getNumInstancias(self):
        return len(self.panda)

    def getIndiceAtributo(self, atributo):
        return self.panda.columns.get_loc(atributo)

    def eliminarAtributoDePropiedades(self, index):
        """Elimina el atributo que esta en index de la lista de atributos
        que estan en el archivo de propiedades"""
        self.data["atributos"].pop(index)

    def eliminarAtributoDeDiccionario(self, atributo):
        """Elimina el atributo del diccionario de atributos"""
        try:
            del self.atributos[atributo]
            return True
        except KeyError:
            return False

    def correlacionPearson(self, nom_atributo1, nom_atributo2):
        """Calcula la correlacion de pearson de dos atributos numéricos"""
        atributo1 = self.getAtributo(nom_atributo1)
        atributo2 = self.getAtributo(nom_atributo2)

        try: # si no se puede convertir a float significa que el atributo es categorico
            # quita los valores faltantes
            data_frame1 = self.quitarValoresFaltantes(nom_atributo1).astype("float64")
            data_frame2 = self.quitarValoresFaltantes(nom_atributo2).astype("float64")
        except:
            return None

        # para calcular la correlación de Pearson es necesario que los dos
        # atributos tengan la misma cantidad de elementos.
        if len(data_frame1) != len(data_frame2):
            return None

        # no se permite realizar el calculo si alguno de los atributos
        # no tiene valores
        if len(data_frame1) == 0 or len(data_frame2) == 0:
            return None

        media1 = atributo1.getMedia()
        media2 = atributo2.getMedia()
        
        desviacion1 = atributo1.getDesviacionEstandarManual()
        if nom_atributo1 == nom_atributo2: # si son el mismo atributo entonces tiene la misma desviación estándar
            desviacion2 = desviacion1
        else:
            desviacion2 = atributo2.getDesviacionEstandarManual()

        total = 0.0
        n = len(data_frame1)

        # itera a traves de las dos columnas, hacerlo de esta forma es mas rapido que si se hace por indices
        for val_1, val_2 in zip(data_frame1, data_frame2):
            total += val_1 * val_2

        total -= (n * media1 * media2)
        resultado = total / (n * desviacion1 * desviacion2)
        return round(resultado, 3) # redondea el resultado a 3 numeros después del punto

    def quitarValoresFaltantes(self, nom_atributo):
        """Retorna un DataFrame sin los valores faltantes"""
        return self.panda[nom_atributo].loc[self.panda[nom_atributo] != ConjuntoDatos.SIMBOLO_FALTANTE]

    def coeficienteTschuprow(self, nom_atributo1, nom_atributo2):
        """Calcula el coeficiente de contingencia de Tschuprow"""

        # crea un diccionario donde las llaves son los valores únicos del
        # primer atributo y los valores el número de veces que aparece ese valor en el dataset
        totales_a1 = {}
        for val in self.panda[nom_atributo1].unique(): # itera a traves de los valores únicos del atributo
            totales_a1[val] = 0 # todos se inicializan en 0
        
        # hace lo mismo que arriba solo que con el atributo 2
        totales_a2 = {}
        for val in self.panda[nom_atributo2].unique(): # itera a traves de los valores únicos del atributo
            totales_a2[val] = 0

        # crea un diccionario de diccionarios para contabilizar el número
        # de veces que aparce un par de valores en el dataset
        """
        ejemplo:
        {
            "sunny": {"True": 2, "False": 3},
            "rainy": {"True": 1, "False": 5}
            .
            .
        }
        """
        frecuencias = {}
        for i in self.panda[nom_atributo1].unique():
            frecuencias[i] = {}
            for j in self.panda[nom_atributo2].unique():
                frecuencias[i][j] = 0 # todo se inicializa en cero

        # itera a traves de los valores de las dos columnas para acumular las frecuencias
        for i, j in zip(self.panda[nom_atributo1], self.panda[nom_atributo2]):
            frecuencias[i][j] += 1
            totales_a1[i] += 1
            totales_a2[j] += 1

        n = self.getNumInstancias()
        chi_cuadrada = 0.0
        for i in totales_a1:
            for j in totales_a2:
                e = (totales_a1[i] * totales_a2[j]) / n
                frecuencia = frecuencias[i][j]
                val = pow((frecuencia - e), 2) / e
                chi_cuadrada += val

        c = len(totales_a1) - 1 # num de atributos diferentes en el primer atributo - 1
        r = len(totales_a2) - 1 # num de atributos diferentes en el segundo atributo - 1
        abajo = n * math.sqrt(c * r)

        return round(math.sqrt(chi_cuadrada / abajo), 4) # redondea a 4 digitos después del punto