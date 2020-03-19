import json
from atributo_numerico import AtributoNumerico
from atributo_categorico import AtributoCategorico
import pandas as pd


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

        print(self.data)

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

    def eliminarAtributoDeDiccionario(self, atributo):
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
        atributo1 = self.getAtributo(nom_atributo1)
        atributo2 = self.getAtributo(nom_atributo2)

        if atributo1 == None or atributo2 == None or \
            atributo1.getTipo() != "categorico" or \
            atributo2.getTipo() != "categorico":
            return None

        #TODO: Coeficiente Tschuprow aún no terminado
    
    #TODO: Falta por realizar chiCuadrada
    def chiCuadrada(self, nom_atributo1, nom_atributo2):
        pass
