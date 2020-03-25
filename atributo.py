class Atributo:
    # Constructur que recibe panda (DataFrame), los atributos y el diccionario con el que se trabajara
    def __init__(self, panda, atributos, dic_datos):
        self.panda = panda
        self.atributos = atributos
        self.dic_datos = dic_datos

    # Cambiar el nombre al atributo / columna
    def setNombre(self, nombre):
        self.panda.rename(columns={self.getNombre(): nombre}, inplace=True) # Cambia el nombre directo del pandas
        self.atributos[nombre] = self.atributos.pop(self.getNombre()) # reemplaza la clave de un valor
        self.dic_datos["nombre"] = nombre # Solo se cambia el nombre

    # Cambiar el tipo de dato que tiene
    def setTipo(self, tipo):
        from atributo_numerico import AtributoNumerico # Importamos la clase AtributoNumerico del archivo atributo_numerico
        from atributo_categorico import AtributoCategorico # Importamos la clase AtributoCategorico del archivo atributo_categorico

        if tipo != self.getTipo(): # Sí el tipo pasado por parametro es distinto del tipo actual, entra
            self.dic_datos["tipo"] = tipo
            if tipo == "categorico": # Sí el tipo es categorico, reemplaza la instancia por uno categorico
                self.atributos[self.getNombre()] = AtributoCategorico(self.panda, self.atributos, self.dic_datos)
            else: # Lo mismo que lo de arriba, pero en numerico
                self.atributos[self.getNombre()] = AtributoNumerico(self.panda, self.atributos, self.dic_datos)


    # Establecemos el dominio, definido por el parametro
    def setDominio(self, dominio):
        self.dic_datos["dominio"] = dominio

    # Obtenemos los elementos
    def getNombre(self):
        return self.dic_datos.get("nombre", None) # Sí el nombre no esta definido, retorna none

    def getTipo(self):
        return self.dic_datos.get("tipo", None)

    def getDominio(self):
        return self.dic_datos.get("dominio", "") # Sí el nombre no esta definido, retorna una cadena vacia

    def getValoresFueraDominio(self):
        """Retorna una lista con los ids de las instancias fuera de domino para este atributo"""

        return list(self.panda[self.panda[self.getNombre()].astype(str).str.match(self.getDominio()) == False].index)

    def getValoresFaltantes(self):
        """Retorna una lista con los ids de las instancias con valores faltantes para este atributo"""
        from conjunto_datos import ConjuntoDatos
        return list(self.panda.loc[self.panda[self.getNombre()].astype(str) == ConjuntoDatos.SIMBOLO_FALTANTE].index)
       
