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