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
        self.dic_datos["tipo"] = tipo

    # aqui debe verificarse que toda la columna cumpla con el nuevo dominio
    def setDominio(self, dominio):
        self.dic_datos["dominio"] = dominio

    def getNombre(self):
        return self.dic_datos["nombre"]

    def getTipo(self):
    	return self.dic_datos["tipo"]

    def getDominio(self):
    	return self.dic_datos["dominio"]
