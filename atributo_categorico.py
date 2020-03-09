from atributo import Atributo


class AtributoCategorico(Atributo):

	def __init__(self, panda, atributos, dic_datos):
		Atributo.__init__(self, panda, atributos, dic_datos)

	def histograma(self):
		pass
