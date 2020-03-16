from ventana_eliminar_instancias_ui import *
from PyQt5.QtWidgets import QWidget, QMessageBox


class VentanaEliminarInstancias(QWidget, Ui_Form):
	def __init__(self, modelo_tabla, signal, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.signal_instancia_eliminada = signal # señal para cuando se eliminen las instancias
		self.modelo = modelo_tabla

		# evento clic del boton eliminar
		self.btnEliminar.clicked.connect(self.eliminar_instancias)

		# cierra la ventana al dar clic en el boton cerrar
		self.btnCerrar.clicked.connect(lambda x: self.close())

	def eliminar_instancias(self):
		"""Inicia el proceso"""
		rows = self.textEdit.toPlainText().split(", ")

		try:
			rows = list(map(int, rows)) # convertir cada valor de la lista a int
		except:
			print("Asegurate de que solo ingresaste numeros")
			return

		num_eliminadas = self.modelo.eliminarMultiplesFilas(rows)

		if num_eliminadas > 0:
			self.signal_instancia_eliminada.emit() # emitir señal para actualizar etiquetas
			QMessageBox.information(self, "Instancias eliminadas",
				"Se eliminaron " + str(num_eliminadas) + " instancias");