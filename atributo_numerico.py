from atributo import Atributo
import math

class AtributoNumerico(Atributo):

    def __init__(self, panda, atributos, dic_datos):
    	Atributo.__init__(self, panda, atributos, dic_datos)

    def getModa(self):
        aux = self.quitarValoresFaltantes()
        # retorna una lista de las modas
        return list(aux.mode()) 

    def getMediana(self):
        try:
            aux = self.quitarValoresFaltantes() # excluye los valores faltantes
            return aux.astype("float64").median().round(4)
        except:
            return None

    def getMedia(self):
        try:
            aux = self.quitarValoresFaltantes() # excluye los valores faltantes
            return aux.astype("float64").mean().round(4)
        except:
            return None

    def getDesviacionEstandar(self):
        """Calcula la desviación estándar del atributo"""
        try:
            aux = self.quitarValoresFaltantes() # excluye los valores faltantes
            return aux.astype("float64").std().round(4)
        except:
            return None

    def getDesviacionEstandarManual(self):
        """Calcula la desviación estándar sin usar librería"""
        from conjunto_datos import ConjuntoDatos
        try:    
            media = self.getMedia()
#            nombre = self.getNombre()
            total = 0.0
            aux_data_frame = self.quitarValoresFaltantes().astype("float64") # excluye los valores faltantes
            n = len(aux_data_frame)

            for i in aux_data_frame: # i hace referencia a un elemento de nuestro dataframe, no a su indice
                val = pow((i - media), 2)
                total += val

            resultado = math.sqrt(total / n)
            return round(resultado, 4)
        except:
            return None


    def quitarValoresFaltantes(self):
        """Retorna un DataFrame sin los valores faltantes"""
        from conjunto_datos import ConjuntoDatos
        return self.panda[self.getNombre()].loc[self.panda[self.getNombre()] != ConjuntoDatos.SIMBOLO_FALTANTE]

    
    def boxPlot(self):
    	pass

