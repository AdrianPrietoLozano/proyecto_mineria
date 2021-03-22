from ventana_descripcion_ui import *
from PyQt5.QtWidgets import QWidget
from conjunto_datos import ConjuntoDatos


class VentanaDescripcion(QWidget, Ui_Form):
	def __init__(self, conjunto_datos, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.conjunto = conjunto_datos

		self.textDescripcion.setPlainText(self.conjunto.getDescripcion())

		self.btnActualizar.clicked.connect(self.actualizar_descripcion)

	def actualizar_descripcion(self):
		self.conjunto.setDescripcion(self.textDescripcion.toPlainText())
		print(self.conjunto.data)

		self.close()