class Atributo:
    def __init__(self, nombre, tipo, dominio):
        self.nombre = nombre
        self.tipo = tipo
        self.dominio = dominio

    def getNombre(self):
        return self.nombre

    def getTipo(self):
    	return self.tipo

    def getDominio(self):
    	return self.dominio