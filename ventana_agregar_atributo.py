from ventana_agregar_atributo_ui import *
from PyQt5.QtWidgets import QWidget, QMessageBox


class VentanaAgregarAtributo(QWidget, Ui_Form):
	def __init__(self, conjunto, modelo_tabla, signal, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.conjunto = conjunto
		self.modelo_tabla = modelo_tabla
		self.signal_atributo_agregado = signal

		self.btnAceptar.clicked.connect(self.agregar_atributo)

		# cierra la ventana al dar clic en el boton
		self.btnCancelar.clicked.connect(lambda x: self.close())

	def agregar_atributo(self):
		nombre_atributo = self.lineEditNombre.text()
		if self.comboBoxTipo.currentIndex() == 0:
			tipo = "numerico"
		else:
			tipo = "categorico"
		dominio = self.lineEditDominio.text()

		if nombre_atributo in self.conjunto.getNombresAtributos(): # si el nombre del atributo ya existe
			QMessageBox.information(self, "Error", "El atributo " + nombre_atributo + " ya existe")
		elif nombre_atributo == "": # el nombre del atriuto no puede estar vacío
			QMessageBox.information(self, "Error", "El nombre del atributo no puede estar vacío")
		else:
			insertado = self.modelo_tabla.insertarColumnaAlFinal(nombre_atributo)

			if insertado: # si se agrego el atributo correctamente
				self.conjunto.agregarAtributo(nombre_atributo, tipo, dominio)
				self.signal_atributo_agregado.emit(nombre_atributo)
				self.close()
			else:
				QMessageBox.information(self, "Error", "Ocurrio un error al insertar el atributo")	