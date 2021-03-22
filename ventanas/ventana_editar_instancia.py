from ventana_editar_instancia_ui import *
from PyQt5.QtWidgets import QWidget
from conjunto_datos import ConjuntoDatos


class VentanaEditarInstancia(QWidget, Ui_Form):
	def __init__(self, id_instancia, conjunto, modelo_tabla, signal, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.id_instancia = id_instancia
		self.conjunto = conjunto
		self.modelo_tabla = modelo_tabla
		self.signal_instancia_editada = signal

		self.labelId.setText("ID: " + str(id_instancia))
		self.btnEditar.clicked.connect(self.editar_instancia)

		self.agregar_campos()

	def editar_instancia(self):
		"""agrega una instancia la modelo y emite la señal a la ventana principal"""
		instancia = []
		for i in self.conjunto.getNombresAtributos():
			edit = self.findChild(QtWidgets.QLineEdit, "edit_" + i)
			val = edit.text()
			tipo_dato = self.conjunto.panda[i].dtype

			if val == "": # si un valor se deja en blaco se reemplaza por valor faltante
				val = ConjuntoDatos.SIMBOLO_FALTANTE

			# conversion de tipos
			if tipo_dato == "int64":
				val = self.convertir_a_entero(val)
			elif tipo_dato == "float64":
				val = self.convertir_a_flotante(val)

			instancia.append(val)

		self.conjunto.panda.loc[self.id_instancia] = instancia
		self.signal_instancia_editada.emit() # emitir señal para actualizar etiquetas
		self.close()

	def agregar_campos(self):
		"""Genera los campos dinamicamente y los muestra"""
		nom_atributos = self.conjunto.getNombresAtributos()

		# Crea QLineEdit y QLabel dinamicamente
		for i in range(len(nom_atributos)):
			label = QtWidgets.QLabel(self.formLayoutWidget)
			label.setText(nom_atributos[i])
			edit = QtWidgets.QLineEdit(self.formLayoutWidget)
			edit.setObjectName("edit_" + nom_atributos[i])
			edit.setText(str(self.conjunto.panda.loc[self.id_instancia][i]))

			self.formLayout.setWidget(i, QtWidgets.QFormLayout.LabelRole, label)
			self.formLayout.setWidget(i, QtWidgets.QFormLayout.FieldRole, edit)

		self.scrollAreaWidgetContents.setLayout(self.formLayout)

	def convertir_a_entero(self, val):
		try:
			return int(val)
		except:
			return val

	def convertir_a_flotante(self, val):
		try:
			return float(val)
		except:
			return val



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    v = AgregarInstancia()
    v.show()
    app.exec_()