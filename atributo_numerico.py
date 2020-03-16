from atributo import Atributo


class AtributoNumerico(Atributo):

    def __init__(self, panda, atributos, dic_datos):
    	Atributo.__init__(self, panda, atributos, dic_datos)

    def getModa(self): # tal vez sea necesario validar los valores nulos
    	try:
    		return self.panda[self.getNombre()].mode() # hay problemas con este
    	except:
    		return None

    def getMediana(self): # tal vez sea necesario validar los valores nulos
    	try:
    		return round(self.panda[self.getNombre()].median(), 2)
    	except:
    		return None

    def getMedia(self): # tal vez sea necesario validar los valores nulos
    	try:
    		return round(self.panda[self.getNombre()].mean(), 2)
    	except:
    		return None

    def getDesviacionEstandar(self):
        try:
            return round(self.panda[self.getNombre()].std(), 2)
        except:
            return None

    def boxPlot(self):
    	pass

