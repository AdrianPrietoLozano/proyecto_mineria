class Atributo:
    def __init__(self, panda, atributos, dic_datos):
        self.panda = panda
        self.atributos = atributos
        self.dic_datos = dic_datos

    def setNombre(self, nombre):
        self.panda.rename(columns={self.getNombre(): nombre}, inplace=True)
        self.atributos[nombre] = self.atributos.pop(self.getNombre()) # reemplaza la clave de un valor
        self.dic_datos["nombre"] = nombre

    def setTipo(self, tipo):
        from atributo_numerico import AtributoNumerico
        from atributo_categorico import AtributoCategorico

        if tipo != self.getTipo():
            self.dic_datos["tipo"] = tipo
            if tipo == "categorico":
                self.atributos[self.getNombre()] = AtributoCategorico(self.panda, self.atributos, self.dic_datos)
            else:
                self.atributos[self.getNombre()] = AtributoNumerico(self.panda, self.atributos, self.dic_datos)



    def setDominio(self, dominio):
        self.dic_datos["dominio"] = dominio

    def getNombre(self):
        return self.dic_datos.get("nombre", None)

    def getTipo(self):
        return self.dic_datos.get("tipo", None)

    def getDominio(self):
        return self.dic_datos.get("dominio", "")

    def getValoresFueraDominio(self):
        """Retorna una lista con los ids de las instancias fuera de domino para este atributo"""

        return list(self.panda[self.panda[self.getNombre()].astype(str).str.match(self.getDominio()) == False].index)

    def getValoresFaltantes(self):
        """Retorna una lista con los ids de las instancias con valores faltantes para este atributo"""
        from conjunto_datos import ConjuntoDatos
        return list(self.panda.loc[self.panda[self.getNombre()].astype(str) == ConjuntoDatos.SIMBOLO_FALTANTE].index)
       
