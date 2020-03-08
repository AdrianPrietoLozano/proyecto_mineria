import json
from atributo import Atributo
import pandas as pd

simbolo = "hola"

class ConjuntoDatos:
    _simbolo_faltante = "?" # por default será ?
    _target = None

    def __init__(self, archivo_propiedades):
        self.archivo_propiedades = archivo_propiedades
        self.panda = None
        self.data = {} # aquí se guarda todo el archivo .json como un diccionario
        self.atributos = {}
        self.__cargar_propiedades()

        ConjuntoDatos._simbolo_faltante = self.data["simbolo_faltante"]
        ConjuntoDatos._target = self.data["target"]

    def __cargar_propiedades(self):
        with open(self.archivo_propiedades) as contenido:
            self.data = json.load(contenido) # combierte el .json a un diccionario

            self.panda = pd.read_csv(self.getPathCsv(), names=[c["nombre"] for c in self.data["atributos"]])

            # crea un diccionario de atributos, la llave es el nombre del atributo
            # y el valor una instancia de la clase Atributo 
            for atributo in self.data["atributos"]:
                self.atributos[atributo["nombre"]] = Atributo(self.panda, self.atributos, atributo)

            contenido.close();
            

    def getPathCsv(self):
        return self.data["path_csv"]

    def getTarget(self):
        return self.data["target"]

    def setDescripcion(self, descripcion):
        self.data["descripcion"] = descripcion

    def getAtributo(self, nombre):
        return self.atributos.get(nombre, None);

    def getAtributos(self):
        return self.atributos.values()

    def getNombresAtributos(self):
        return self.atributos.keys()

    def getNumAtributos(self):
        return len(self.atributos)

    def getNumInstancias(self):
        return len(self.panda)