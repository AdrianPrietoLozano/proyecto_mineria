import json
from atributo_numerico import AtributoNumerico
from atributo_categorico import AtributoCategorico
import pandas as pd


class ConjuntoDatos:

    SIMBOLO_FALTANTE = "?"  # por default será ?
    TARGET = None

    def __init__(self, archivo_propiedades):
        self.archivo_propiedades = archivo_propiedades
        self.panda = None
        self.data = {} # aquí se guarda todo el archivo .json como un diccionario
        self.atributos = {}
        self.__cargar_propiedades()

        ConjuntoDatos.SIMBOLO_FALTANTE = self.data["simbolo_faltante"]
        ConjuntoDatos.TARGET = self.data["target"]

    def __cargar_propiedades(self):
        with open(self.archivo_propiedades) as contenido:
            self.data = json.load(contenido) # combierte el .json a un diccionario

            self.panda = pd.read_csv(self.getPathCsv(), skipinitialspace=True,
                names=[c["nombre"] for c in self.data["atributos"]])

            # crea un diccionario de atributos, la llave es el nombre del atributo
            # y el valor una instancia de la clase AtributoNumerico o AtributCategorico 
            for atributo in self.data["atributos"]:
                if atributo["tipo"] == "numerico":
                    self.atributos[atributo["nombre"]] = AtributoNumerico(self.panda, self.atributos, atributo)
                else:
                    self.atributos[atributo["nombre"]] = AtributoCategorico(self.panda, self.atributos, atributo)

            contenido.close()

    def getPathCsv(self):
        return self.data.get("path_csv", None)

    def getTarget(self):
        return self.data.get("target", None)

    def setTarget(self, target):
        self.data["target"] = target

    def getSimboloFaltante(self):
        return self.data.get("simbolo_faltante", None)

    def getRuta(self):
        return self.data.get("ruta", None)

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

    def eliminarAtributoDeDiccionario(self, atributo):
        try:
            del self.atributos[atributo]
            return True
        except KeyError:
            return False

    def correlacionPearson(self, nom_atributo1, nom_atributo2):
        """
        x = pd.read_csv("actividad7.csv", skipinitialspace=True)
        media1 = x["Temperatura"].mean()
        media2 = x["Temperatura"].mean()
        desviacion1 = x["Temperatura"].std(ddof=0)
        desviacion2 = x["Temperatura"].std(ddof=0)
        n = len(x)

        print("media1:", media1)
        print("media2:", media2)
        print("des1:", desviacion1)
        print("des2:", desviacion2)
        print("n:", n)
        """

        
        atributo1 = self.getAtributo(nom_atributo1)
        atributo2 = self.getAtributo(nom_atributo2)

        if atributo1 == None or atributo2 == None or \
            atributo1.getTipo() != "numerico" or \
            atributo2.getTipo() != "numerico":
            return None

        media1 = atributo1.getMedia()
        media2 = atributo2.getMedia()
        n = self.getNumInstancias()
        desviacion1 = atributo1.getDesviacionEstandarManual()
        desviacion2 = atributo2.getDesviacionEstandarManual()

        total = 0.0
        for i in range(n):
            val_1 = self.panda[nom_atributo1][i]
            val_2 = self.panda[nom_atributo2][i]
            total += val_1 * val_2

        total -= (n * media1 * media2)
        resultado = total / (n * desviacion1 * desviacion2)
        return round(resultado, 3)
