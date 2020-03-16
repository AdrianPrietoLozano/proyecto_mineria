from atributo import Atributo
import math

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
    		return round(self.panda[self.getNombre()].median(), 4)
    	except:
    		return None

    def getMedia(self): # tal vez sea necesario validar los valores nulos
    	try:
    		return round(self.panda[self.getNombre()].mean(), 4)
    	except:
    		return None

    def getDesviacionEstandar(self):
        """Calcula la desviación estándar del atributo"""
        try:
            return round(self.panda[self.getNombre()].std(), 4)
        except:
            return None

    def getDesviacionEstandarManual(self):
        """Calcula la desviación estándar sin usar librería"""
        try:
            media = self.getMedia()
            n = len(self.panda)
            nombre = self.getNombre()

            total = 0.0
            for i in range(n):
                val = pow((self.panda[nombre].iloc[i] - media), 2)
                total += val

            resultado = math.sqrt(total / n)
            return round(resultado, 4)
            
        except:
            return None


    def boxPlot(self):
    	pass

