from ventana_correlacion_pearson_ui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox


class VentanaCorrelacionPearson(QWidget, Ui_Form):
	def __init__(self, conjunto, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.conjunto = conjunto

		self.iniciar_combo_boxes()

		self.btnCalcular.clicked.connect(self.calcular)

	def iniciar_combo_boxes(self):
		"""LLena los combo boxes con los nombres de los atributos numericos"""
		for atributo in self.conjunto.getAtributos():
			if atributo.getTipo() == "numerico":
				self.comboBox1.addItem(QIcon("iconos/numerico.ico"), atributo.getNombre())
				self.comboBox2.addItem(QIcon("iconos/numerico.ico"), atributo.getNombre())

		if self.comboBox1.count() == 0: # si no hay atributos numericos
			self.btnCalcular.setEnabled(False)

	def calcular(self):
		self.labelResultado.setText("calculando...")
		self.repaint() # para que se actualice la etiqueta

		atributo1 = self.comboBox1.currentText()
		atributo2 = self.comboBox2.currentText()

		tipo_atributo1 = self.conjunto.panda[atributo1].dtype
		tipo_atributo2 = self.conjunto.panda[atributo2].dtype
		if tipo_atributo1 == "float64" or tipo_atributo1 == "int64":
			if tipo_atributo2 == "float64" or tipo_atributo2 == "int64":
				self.labelResultado.setText(str(self.conjunto.correlacionPearson(atributo1, atributo2)))
			else:
				QMessageBox.critical(self, "Error",
				"El atributo " + atributo2 + " no es numerico");
				self.labelResultado.setText("N/A")
		else:
			QMessageBox.critical(self, "Error",
				"El atributo " + atributo1 + " no es numerico");
			self.labelResultado.setText("N/A")