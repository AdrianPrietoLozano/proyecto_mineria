from ventana_moda_ui import *
from PyQt5.QtWidgets import QWidget


class VentanaModa(QWidget, Ui_Form):
	def __init__(self, modas, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		texto_modas = ""
		for moda in modas:
			texto_modas += str(moda) + ", "
		texto_modas = texto_modas[:-2] # quita la última coma
		
		self.textModa.setPlainText(texto_modas)

		# cierra la ventana al dar clic en el boton
		self.btnCerrar.clicked.connect(lambda x: self.close())