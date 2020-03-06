import json
from atributo import Atributo
import pandas as pd

class ConjuntoDatos:
    def __init__(self, propiedades):
        self.propiedades = propiedades
        self.path = None
        self.descripcion = None
        self.target = None
        self.panda = None
        self.num_atributos = 0
        self.atributos = {}
        self.__cargar_propiedades()

    def __cargar_propiedades(self):
        with open(self.propiedades) as contenido:
            data = json.load(contenido)
            self.path = data["path_csv"]
            self.target = data["target"]
            self.descripcion = data["descripcion"]

            self.panda = pd.read_csv(self.path)

            for atributo in data["atributos"]:
                self.atributos[atributo["nombre"]] = Atributo(atributo["nombre"], atributo["tipo"], atributo["dominio"])

            self.num_atributos = len(self.atributos)

            contenido.close();

    def getAtributo(self, nombre):
        return self.atributos.get(nombre, None);

    def getAtributos(self):
        return self.atributos.values()

    def getNombresAtributos(self):
        return self.atributos.keys()

    def getNumAtributos(self):
        return self.num_atributos