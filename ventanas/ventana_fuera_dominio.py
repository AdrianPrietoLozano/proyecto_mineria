from ventana_fuera_dominio_ui import *
from PyQt5.QtWidgets import QWidget


class VentanaFueraDominio(QWidget, Ui_Form):
	def __init__(self, val_faltantes, nom_atributo, *args, **kwargs):
		QtWidgets.QWidget.__init__(self, *args, **kwargs)
		self.setupUi(self)

		self.labelDescripcion.setText(self.labelDescripcion.text() + nom_atributo)

		texto_faltantes = ""
		for val in val_faltantes:
			texto_faltantes += str(val) + ", "
		texto_faltantes = texto_faltantes[:-2] # quita la última coma
		
		self.textEdit.setPlainText(texto_faltantes)

		# copia al portapapeles al dar clic en el boton
		self.btnCopiar.clicked.connect(self.copiar_texto)

		# cierra la ventana al dar clic en el boton
		self.btnCerrar.clicked.connect(lambda x: self.close())

	def copiar_texto(self):
		"""Copia el texto del QPlanTextEdit al portapapeles"""
		self.textEdit.selectAll()
		self.textEdit.copy()