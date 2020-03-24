from atributo import Atributo


class AtributoCategorico(Atributo):

	def __init__(self, panda, atributos, dic_datos):
		Atributo.__init__(self, panda, atributos, dic_datos)

	# Si un atributo numerico se convierte en categorico, no hay que permitirlo
	def histograma(self):
		pass
