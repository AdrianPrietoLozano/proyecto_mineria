from ventana_coeficiente_tschuprow_ui import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox


class VentanaCoeficienteTschuprow(QWidget, Ui_Form):
	def __init__(self, conjunto, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.conjunto = conjunto

		self.iniciar_combo_boxes()

		self.btnCalcular.clicked.connect(self.calcular)

	def iniciar_combo_boxes(self):
		"""LLena los combo boxes con los nombres de los atributos categoricos"""
		for atributo in self.conjunto.getAtributos():
			if atributo.getTipo() == "categorico":
				self.comboBox1.addItem(QIcon("iconos/categorico.ico"), atributo.getNombre())
				self.comboBox2.addItem(QIcon("iconos/categorico.ico"), atributo.getNombre())

		if self.comboBox1.count() == 0: # si no hay atributos categoricos se desactiva el boton calcular
			self.btnCalcular.setEnabled(False)

	def calcular(self):
		self.labelResultado.setText("calculando...")
		self.repaint() # para que se actualice la etiqueta

		atributo1 = self.comboBox1.currentText()
		atributo2 = self.comboBox2.currentText()

		# obtiene los tipos de cada atributo
		tipo_atributo1 = self.conjunto.panda[atributo1].dtype
		tipo_atributo2 = self.conjunto.panda[atributo2].dtype

		# comprueba que los dos atributos sean de tipo categoricos
		if tipo_atributo1 == "O" or tipo_atributo1 == "O":
			if tipo_atributo2 == "O" or tipo_atributo2 == "O":
				self.labelResultado.setText(str(self.conjunto.coeficienteTschuprow(atributo1, atributo2)))
			else:
				QMessageBox.critical(self, "Error",
				"El atributo " + atributo2 + " no es categorico");
				self.labelResultado.setText("N/A")
		else:
			QMessageBox.critical(self, "Error",
				"El atributo " + atributo1 + " no es categorico");
			self.labelResultado.setText("N/A")