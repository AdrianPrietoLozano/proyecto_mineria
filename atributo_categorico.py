from atributo import Atributo


class AtributoCategorico(Atributo):

	def __init__(self, panda, atributos, dic_datos):
		Atributo.__init__(self, panda, atributos, dic_datos)

	#TODO: Falta por hacer histograma
	#TODO: Si el target esta definido, debemos hacer un histograma por clase en la misma imagen
	# Si un atributo numerico se convierte en categorico, no hay que permitirlo
	def histograma(self):
		pass
